#!/usr/bin/env python3

import cmd
import sys

# Only needed to run examples without installing files
sys.path.append("..")
from files import *

class Shell(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

        # /home/user $: command
        # I hate this prompt, but I get confused if it looks like
        # my normal shell prompt.
        self.prompt = Path.join(Path.current().path[-2:]) + " $: "

    def do_cd(self, arg="~"):
        Path.current(Path(arg))
        self.prompt = Path.join(Path.current().path[-2:]) + " $: "

    def help_cd(self):
        print("USAGE: cd [dir]")
        print("\tChange current directory to dir. Default directory: ~")

    def do_pwd(self):
        print(str(Path.current()))

    def help_pwd(self):
        print("USAGE: pwd")
        print("\tPrint current directory")

    def do_ls(self, dir=None):
        if not dir:
            dir = Path.current()
        else:
            dir = Path(dir)

        j = 1
        for i in Dir(dir):
            if isinstance(i, Dir):
                print((i.name + "/").ljust(19), end="")
            else:
                print(i.name.ljust(19), end="")

            if j % 4 == 0:
                print()

            j += 1

        print()

    def help_ls(self):
        print("USAGE: ls [dir]")
        print("List all files in current directory")

    def do_rm(self, file):
        Path(file).get().delete()

    def help_rm(self):
        print("USAGE: rm [file|dir]")
        print("Delete file or directory")
        print("Note that this is recursive, and will delete directories")
        print("Think of it as similar to rm -rf")

    def do_creat(self, file):
        File(file).create()

    def help_creat(self):
        print("USAGE: creat [file]")
        print("Create file")

    def do_mv(self, files):
        files = files.split()
        Path(files[0]).get().move(Path(files[1]))

    def help_mv(self):
        print("USAGE: mv src dest")
        print("Move a file or directory from src to dest")

    def do_cp(self, files):
        files = files.split()
        Path(files[0]).get().copy(Path(files[1]))

    def help_cp(self):
        print("USAGE: cp src dest")
        print("Copy the file or directory src to dest. Works recursively for directories.")

    def do_ln(self, files):
        files = files.split()
        type = "hard"

        if "-s" in files:
            type = "soft"
            del files[files.index("-s")]

        Path(files[0]).link(Path(files[1]), type)

    def do_unlink(self, files):
        self.do_rm(files)

    def help_unlink(self):
        print("USAGE: unlink link")
        print("Removes a link. Its the same as rm.")

    def do_cat(self, files):
        files = files.split()
        for i in files:
            i = Path(i)
            if "file" in i.type():
                print(i.get().open().read())

    def help_cat(self):
        print("USAGE: cat file1 [file2 file3 file4 ...]")
        print("Print contents of all arguments to the console.")

    def do_echo(self, files):
        files = files.split()

        to = []
        to_app = []

        while ">" in files:
            i = files.index(">")

            to.append(files[i+1])
            del files[i:i+2]
            
        while ">>" in files:
            i = files.index(">>")
            
            to_app.append(files[i+1])
            del files[i:i+2]

        message = " ".join(files)

        if to == [] and to_app == []:
            print(message)
        else:
            for i in to:
                File(i).open("w").write(message + "\n")
            for i in to_app:
                File(i).open("a").write(message + "\n")

    def do_EOF(self):
        sys.exit(0)
        
    def emptyline(self):
        pass

    def default(self, args=""):
        print("Unrecognized command: {0}".format(args))

if __name__ == "__main__":
    sh = Shell()

    if len(sys.argv) == 1:
        sh.cmdloop()
    else:
        verbose = False
        args = list(sys.argv[1:])
        if "-v" in sys.argv:
            verbose = True
            del args[args.index("-v")]
        for i in args:
            for line in File(i).open():
                if verbose:
                    print(line[:-1])
                sh.onecmd(line[:-1])
