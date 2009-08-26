:mod:`files`\ .\ :class:`Dir` -- File manipulation
===================================================

.. currentmodule:: files

.. class:: Dir([path])
   :noindex:

   The :class:`Dir` class provides functions for common opperations on
   directories, such as moving, deleting, and traversing a directory.

   If *path* is passed, the :class:`Dir` object represents the object at that
   path. *path* may be a string or a :class:`Path` object.  Otherwise, a new
   temporary directory is created.

   .. method:: Dir.access([mode])
               Dir.last_access()
               Dir.last_change()
               Dir.ctime()
               Dir.move(new)
               Dir.rename(new)
               Dir.chown([uid, gid])
               Dir.chmod([user="", group="", other="", *extra])
               Dir.chflags(*flags)

      All of these methods are the same as those of the :class:`File` class.
      Please consult that documentation for a description.

   .. method:: Dir.files()

      Return a list of :class:`Path` objects representing files or directories
      in the current directory. Use ``[o.get() for o in dir.files()]`` to get
      the :class:`File` or :class:`Dir` objects in ``dir``. The returned paths
      will be sorted alphabetically with directories first.

   .. method:: Dir.create([mode=0o777])

      Creates the current directory. If possible, give it permissions as given
      in *mode*. This will create any parent directories as necessary.

   .. method:: Dir.delete()

      Delete the current directory `and all files and directories in it`.
      Careful!

   .. method:: Dir.copy(dest[, symlinks=True])

      Copy all files in the current directory to *dest*, which can be a string,
      :class:`Path`, or :class:`Dir`. If *symlinks* is ``False``, symbolic
      links will not be followed.

   .. method:: Dir.walk(top[, topdown=True, onerror=None, followlinks=False])

      Consult the :meth:``os.walk`` documentation.

   .. attribute:: Dir.name

      Same as :attr:`File.name`. Consult the :class:`File` documentation.

:class:`Dir` objects can be compared with ``<`` and ``>`` to sort them
alphabetically. They can also be compared with :class:`File` objects (and they
will always be greater).

:class:`Dir` objects can be used as the subject of a ``for`` loop, such as::

   for i in d:
       print(i.get().name)

