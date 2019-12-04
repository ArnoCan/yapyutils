
*********
Blueprint
*********

.. _REFERENCE_ARCHITECTURE:

The package '*yapyutils*' provides some basic wrapper for *Python* related functions which vary over the 
syntax releases as well as the implementations.
The interfaces are meant to cover the incompatibilities in advance of the upper layers.
These functions are loaceted within teh software stack at the language level, but above the
features supported by thw common libararies such as *__future__* or *six* / *future.utils*.

yapyutils.conf
--------------

The subpackage *yapyutils.conf* provides configuration setups by abstraction.
The package utilizes *yapyutils.data* for the access to configuration data, which is represented 
within the runtime memory by a *JSON* structure.
The data could be transparently loaded - without required syntax extensions * and processed
based on the canonical data format.
The data coudl be loaded from mixed formats, e.g. when continously evolving and migrating from legacy
systems to modern IT landscapes.

yapyutils.files
---------------
Provides support for explicit search of files.
This covers all supported platforms and implementations - *Python2.7*, (*Python3*), and *Python3.5+* /
*CPython*, *IPython*, *IronPython*, *Jython*, and *PyPy*.
See :ref:`Platform Support <PlatformSupport>`.

   .. parsed-literal::
   
      file_name, file_path = get_filelocation(file_name)
      
   
A more advanced search:

   .. parsed-literal::
   
      basename = "/my/path/"
      relpaths = ["sub/path0", "sub/path1"]
      
      import_name, module_file_path = get_modulelocation(module_name, basename, relpaths)
      
      loaded_module = load_module(import_name, module_file_path)
   
      # imports and inserts into *sys.modules*
   
      loaded_module.function1()

See also `modules.loader <loader.html#>`_ and ":ref:`HOWTO_MODULES_LOAD_MULTIPLATFORM`".

yapyutils.modules
-----------------
Provides support for explicit import of modules as files.
This covers all supported platforms and implementations - *Python2.7*, (*Python3*), and *Python3.5+* /
*CPython*, *IPython*, *IronPython*, *Jython*, and *PyPy*.
See :ref:`Platform Support <PlatformSupport>`.

   .. parsed-literal::
   
      import_name, module_file_path = get_modulelocation(module_name)
      
      load_module(module_name, module_file_path)
   
      # imports and inserts into *sys.modules*
      
      loaded_module.function1()
   
A more advanced search:

   .. parsed-literal::
   
      basename = "/my/path/"
      relpaths = ["sub/path0", "sub/path1"]
      
      import_name, module_file_path = get_modulelocation(module_name, basename, relpaths)
      
      loaded_module = load_module(import_name, module_file_path)
   
      # imports and inserts into *sys.modules*
   
      loaded_module.function1()

See also `modules.loader <loader.html#>`_ and ":ref:`HOWTO_MODULES_LOAD_MULTIPLATFORM`".


yapyutils.releases
------------------

The subpackage *yapyutils.releases* supports the normalization of version
formats - on all supported platforms.
This e.g. naming conventions of setup files and platform dependent loadable 
packages in physical and virtual environments could be easily implemented.

