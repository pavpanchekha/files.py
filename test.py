#!/usr/bin/env python3

import unittest
from files import *
import os
import subprocess
import time

class TestPath(unittest.TestCase):
    def setUp(self):
        os.chdir("/tmp/")
    
    def test_init(self):
        # General path creation
        self.assert_(Path("/usr/bin") == "/usr/bin")

        # Variable expansion
        self.assert_(Path("~") == os.path.expanduser("~"))
        self.assert_(Path("$HOME") == os.path.expanduser("~"))
        self.assert_(Path("${HOME}") == os.path.expanduser("~"))

        if os.name == "nt":
            pass # Figure out how to test %var% expansion

        # Relative paths
        self.assert_(Path(".") == "/tmp")

        # Path-from-Path
        self.assert_(Path(".") == Path(Path(".")))

    def test_ops(self):
        p1 = Path("/usr")

        # Test addition
        self.assert_(p1 + "bin" == "/usr/bin")
        self.assert_(p1 + "local/bin" == "/usr/local/bin")

        # Test length
        self.assert_(len(p1) == 2)
        self.assert_(len(p1 + "local/bin") == 4)

        # Test bool
        self.assert_(p1)
        self.assert_(not Path("/asdfabvasdfvasbg"))
        self.assert_(p1.exists)

    def test_list(self):
        p1 = Path("/usr/local/bin")

        self.assert_(p1[1] == "/usr")
        self.assert_(p1[3] == p1)

        p1[3] = "share"
        self.assert_(p1 == "/usr/local/share")
        p1[3] = "share/somelib"
        self.assert_(p1 == "/usr/local/share/somelib")
        p1[2:] = "share/somelib"
        self.assert_(p1 == "/usr/share/somelib")

        del p1[3]
        self.assert_(p1 == "/usr/share")
        del p1[1:]
        self.assert_(p1 == "/")

        p1 = Path("/usr/local/bin")
        self.assert_(p1[-1] == "/usr/local/bin")
        self.assert_(p1[-3] == "/usr")

        p1[-1] = "share"
        self.assert_(p1 == "/usr/local/share")
        p1[-2] = "testfolder/test2"
        self.assert_(p1 == "/usr/testfolder/test2/share")
        p1[-3:-1] = "bin"
        self.assert_(p1 == "/usr/bin/share")

    def test_repr(self):
        p1 = Path("/usr/local/bin")
        self.assert_(str(p1) == "/usr/local/bin")
        self.assert_(repr(p1) == "Path(/usr/local/bin)")

    def test_with(self):
        p1 = Path("/usr")
#        with p1:
#            self.assert_(Path("share") == "/usr/share")

    def test_link(self):
        p1 = Path("/usr")

        self.assert_(p1.type() == ["dir"])

        p2 = Path("testlink")
        p2.link(p1)
        self.assert_(p2.type() == ["dir", "link"])
        self.assert_(os.path.realpath(str(p2)) == "/usr")
        self.assert_(p2.real() == "/usr")
        os.system("unlink /tmp/testlink")

        p1.link_from(p2)
        self.assert_(p2.type() == ["dir", "link"])
        self.assert_(os.path.realpath(str(p2)) == "/usr")
        self.assert_(p2.real() == "/usr")
        os.system("unlink /tmp/testlink")

    def test_get(self):
        self.assert_(isinstance(Path("/usr").get(), Dir))
        self.assert_(isinstance(Path("/var/log/kern.log").get(), File))

class TestFSObject(unittest.TestCase):
    def setUp(self):
        Path.current("/tmp")
        self.file = open("test", "w") # create new file

    def tearDown(self):
        if Path("/tmp/test"):
            os.remove("/tmp/test")
        if Path("/tmp/bob"):
            os.remove("/tmp/bob")
    
    def test_access(self):
        subprocess.call(["chmod", "0400", "test"])
        f = File("test")
        self.assert_(f.access("r"))
        self.assert_(not f.access("w"))
        self.assert_(not f.access("x"))

        subprocess.call(["chmod", "0100", "test"])
        self.assert_(not f.access("r"))
        self.assert_(not f.access("w"))
        self.assert_(f.access("x"))
        self.assert_(not f.access("rw"))
        self.assert_(not f.access("rwx"))
        
        subprocess.call(["chmod", "0700", "test"])
        self.assert_(f.access("rwx"))

    def test_times(self):
        t = time.time()

        # These tests are pretty weak, but I can't think of
        # anything better without manually slowing down
        # the test suite.
        
        f = File("test")
        self.assert_(-1 < f.last_access() - t < 1)
        self.assert_(-1 < f.last_change() - t < 1)
        self.assert_(-1 < f.ctime() - t < 1)

    def test_rename(self):
        f = File("test")
        f.rename("bob")
        self.assert_(Path("/tmp/bob"))
        self.assert_(not Path("/tmp/test"))

    def test_chmod(self):
        f = File("test")
        f.chmod("rwx")
        self.assert_(f.access("rwx"))

        f.chmod("r")
        self.assert_(f.access("r"))
        self.assert_(not f.access("w"))

    # As much as I would like to test chown
    # I'm too lazy to program the asking for
    # su in order to test if I really did change
    # the uid and such.

    # Same for chflags

    def test_eq(self):
        f = File("test")
        
        f.path.link_from("bob", "hard")
        self.assert_(File("test") == File("bob"))

    def test_move(self):
        open("bob", "w").close()
        os.mkdir("testdir")
        FSObject("bob").move("testdir/test")
        self.assert_(Path("testdir/test"))
        self.assert_(not Path("bob"))
        shutil.rmtree("testdir")

class TestFile(unittest.TestCase):
    def setUp(self):
        Path.current("/tmp")
        open("test", "w").close() # create new file

    def tearDown(self):
        if Path("/tmp/test"):
            os.remove("/tmp/test")
        if Path("/tmp/bob"):
            os.remove("/tmp/bob")

    def test_temp(self):
        f = File()
        self.assert_(str(f.path).startswith("/tmp"))
        self.assert_(f.path)
        q = f.open("w")
        q.write("Hello, World!")
        q.close()
        self.assert_(f.size() > 0)

    def test_create_delete(self):
        f = File("test")
        f.delete()
        self.assert_(not f.path)
        f.create()
        self.assert_(f.path)

    def test_copy(self):
        f = File("test")
        fo = f.open("w")
        fo.write("Hello, World!")
        fo.close()

        f.copy("bob")
        fo = f.open("r")
        go = File("bob").open("r")
        self.assert_(go.read() == fo.read())

class TestDir(unittest.TestCase):
    def setUp(self):
        Path.current("/tmp")

    def tearDown(self):
        if Path("/tmp/testdir"):
            shutil.rmtree("/tmp/testdir")
        if Path("/tmp/bobdir"):
            shutil.rmtree("/tmp/bobdir")

    def test_create_delete(self):
        d = Dir("testdir")
        d.create()
        self.assert_(Path("testdir"))
        d.delete()
        self.assert_(not Path("testdir"))

        d.create(384) #0o600
        self.assert_(not d.access("x"))

    def test_files(self):
        d = Dir("testdir")
        d.create()
        File("testdir/t1.test").create()
        File("testdir/t2.test").create()

        self.assert_(len(list(d.files())) == 2)

        t = []
        for f in d:
            t.append(f.name)

        self.assert_(t == ["t1.test", "t2.test"])

    def test_copy(self):
        d = Dir("testdir")
        d.create()
        File("testdir/t1.test").create()
        File("testdir/t2.test").create()
        
        d.copy("bobdir")
        self.assert_(list(map(lambda x: x.name, d.files())) == list(map(lambda x: x.name, Dir("bobdir").files())))

if __name__ == "__main__":
    unittest.main()
