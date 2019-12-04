
.. _HOWTO_MODULES_LOAD_MULTIPLATFORM:

Howto Load Modules on Multiple Python Platforms
-----------------------------------------------

The *yapyutils.modules.loader* module provides for the explicit import of modules as files.
This covers all supported platforms and implementations, see :ref:`TESTED_OS_PYTHON`.

   .. parsed-literal::
   
      import_name, module_file_path = get_modulelocation(module_name)
      
      load_module(module_name, module_file_path)
   
      # imports and inserts into *sys.modules*
      
      loaded_module.function1()
   
A more advanced search provides subpaths for a mor comprehensive search.
The resulting import name could now be different from the provided input name,
as the returned names are relative to the matched *sys.path* entry.
The resulting *import_name* results in the the key entry within the
*sys.modules* map. 

   .. parsed-literal::
   
      basename = "/my/path/"
      relpaths = ["sub/path0", "sub/path1"]
      
      import_name, module_file_path = get_modulelocation(module_name, basename, relpaths)
      
      loaded_module = load_module(import_name, module_file_path)
   
      # imports and inserts into *sys.modules*
   
      loaded_module.function1()

This module provides a special case for dynamic configuration and load of components.
The feature is not covered by *__future__* and *future.utils*, nor by the standard conversion 
tools such as *py2to3*.
The software stack location is above the layers of *__future__* and *future.utils*,
but below the applications including infrastructure applications.
Thus extends these.
 
