:mod:`files`\ .\ :class:`Path` -- Path manipulation
===================================================

.. currentmodule:: files

.. class:: Path(path)
   :noindex:

   The :class:`Path` class provides functions for manipulating paths.

   *path* should be a string, list, tuple, or :class:`Path` object. Most
   likely, it will be a string, which creates a new :class:`Path` object that
   represents that path. An example would be ``Path("/usr/bin")``.

   Note that all new :class:`Path` objects automatically:
   
    * Expand ``~`` and ``~user``
    * Expand ``$ENV_VAR`` and ``%WINDOWS_MUST_BE_DIFFERENT%`` variables
    * Make the path absolute
    * Remove double slashes (``a//b``), ``.``\ 's, and ``..``\ 's
    * Normalizes case, if necessary.

   Symbolic links are not, however, removed from the path.

   The :class:`Path` object can be used in *many* ways. Assuming ``path`` is
   :class:`Path` object:
   
    * ``path + "dir/dir"`` -- Paths can be added to strings to yield new paths
    * ``if path: ...`` -- Paths are ``True`` if they exist
    * ``len(path); path[i]`` -- Paths can be used as a list. Note that for a
      Unix environment, ``Path[0]`` will be ``Path(/)``. This can be a bit
      confusing. For example, ``Path("/usr/local/bin")[2]`` is
      ``Path(/usr/local)``. Its as if :class:`Path` objects use one-based
      indexing, and you can think of it that way if you want.

      ``path[-1] = "bob"`` also works, as does
      ``path[1:4] = "usr/local/share"``. So does ``del path[2]``.
    * ``"file" in path`` -- Is a file in that path?
    * ``str(path)`` -- Returns the path in string form. This always does not
      contain the final slash.
    * ``with path: ...`` -- This will change directory to path before
      entering the with loop, and change back afterwards.

   Of course, a :class:``Path`` object also has some useful methods. These
   are detailed below.

   .. method:: Path.real()

      Returns the :class:`Path` object corresponding to the real path of the
      file or directory. This will resolve symbolic links.

   .. method:: Path.get()

      Returns the :class:`File` or :class:`Dir` object corresponding to the
      path.

   .. method:: Path.exists()

      Returns ``True`` if the path exists, ``False`` if it does not.

   .. method:: Path.type()

      Returns a list that may contain any of ``"file"``, ``"dir"``,
      ``"link"``, or ``"mount"``. ``"mount"`` denotes a mount point on
      Unix-like systems.

   .. method:: Path.link(dest[, type="soft"])

      Links the current path to *dest*. If *type* is ``"soft"``, a symlink is
      created. Otherwise, a hardlink is made.

   .. method:: Path.link_from(src[, type="soft"])

      Links *src* to the current path. *type* is identical to above.

   .. staticmethod:: Path.split(path)

      Splits *path* (a string) into a list of directories.
      For example, ``"/home/pavpan/"`` becomes ``["/", "home", "pavpan"]``
      Wonder what happens to the drive letter on Windows...

   .. staticmethod:: Path.join(path)

      Joins *path* (a list) into a path string.
      For example, ``["/", "home", "pavpan"]`` becomes ``"/home/pavpan"``.
      The final slash is always omitted.

   .. staticmethod:: Path.current([path=None])

      If *path* (a string or :class:`Path`) is passed, changes the current
      directory to *path*. Otherwise, returns the current path, as a
      :class:`Path`.

   .. staticmethod:: Path.setroot(path)
   
      Changes the root directory (``"/"``) to *path* (a string or
      :class:`Path`)

   
