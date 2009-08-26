:mod:`files`\ .\ :class:`File` -- File manipulation
===================================================

.. currentmodule:: files

.. class:: File([path])
   :noindex:

   The :class:`File` class provides functions for common opperations on files,
   such as moving, deleting, and changing the permissions of a file.

   If *path* is passed, the :class:`File` object represents the object at that
   path. *path* may be a string or a :class:`Path` object.  Otherwise, a new
   temporary file is created.

   .. method:: File.access([mode])

      If *mode* is not provided, returns a string that might contain ``r``,
      ``w``, or ``x``. These correspond to read, write, and execute
      permissions `for the current user`.

      If *mode* is given, it may contain ``r``, ``w``, or ``x``. The returned
      value will be ``True`` if the `current user` has `all` of the given
      permissions and ``False`` otherwise.

   .. method:: File.last_access()
               File.last_change()
               File.ctime()

      All of these methods return the epoch (Unix) time of the last access and
      change of the file, and the system's ctime (Which differs between Unix
      and Windows).

   .. method:: File.move(new)

      Moves the file to the location defined by *new* which can be a string,
      a :class:`Path` object, or another :class:`File` object.

   .. method:: File.rename(new)

      Renames the file to have the name *new*. Note that *new* should not
      contain any slashes: :meth:`move` should be used move files to new
      directories.

   .. method:: File.chown([uid, gid])

      Changes file ownership to the given User ID (*uid*) and Group ID (*gid*).
      If either is not passed, that part of the ownership is unchanged.

   .. method:: chmod(user="", group="", other="", *extra)

      Change the file permissions to those given, where each of *user*,      
      *group*, and *other* are strings containing (perhaps) ``r``, ``w``, and
      ``x``. The arguments ``"uid"``, ``"gid"``, and ``"vtx"`` may also be
      passed to set those permission bits.

   .. method:: File.chflags(*flags)

      The arguments passed may contain any of:

       * ``"no dump"``
       * ``"immutable"``
       * ``"append"``
       * ``"opaque"``
       * ``"no unlink"``
       * ``"archived"``
       * ``"system immutable"``
       * ``"system append"``
       * ``"system no unlink"``
       * ``"snapshot"``

      Consult the :program:`chflags` manpage for a description of these. If you
      don't know what they are, chances are you'll never have to call this
      function.

   .. method:: File.open([mode="r"])

      Open the file to recieve a file-like object. The mode is *mode*

   .. method:: File.size()

      Get the size of the file.

   .. method:: File.create()

      Create an empty file at the path represented by this :class:`File` object
      if it does not exist already.

   .. method:: File.delete()

      Delete (unlink) the file

   .. method:: File.copy(dest)

      Copy this file to the place represented by *dest*, which may be a string,
      a :class:`Path` object, or a :class:`File` object.

Two :class:`File`\ 's may be compared with the ``==`` operator to determine if
they are the same file (resolving hard links) and with the ``<`` and ``>``
operators to sort them alphabetically.

   .. attribute:: File.name

      The name of the file, including the extension. Setting it will result
      in the file being renamed.
