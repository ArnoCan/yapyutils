# -*- coding: utf-8 -*-
"""Utility for pretty printout of paths.
"""
from __future__ import absolute_import
from __future__ import print_function

import sys
import os



__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


_debug = 0
_verbose = 0


def ppretty_environment():
    """Prints runtime environment parameters for the successive load of 
    helper and the remaining modules.  
    """
    
    sys.stderr.write('\n')

    sys.stderr.write("#*\n")
    sys.stderr.write("#* %-17s%s\n" %("sys.path", ":",))
    sys.stderr.write("#*\n")
    for p in sys.path:
        sys.stderr.write("%21s %s\n" %(":", str(p)))

    sys.stderr.write('\n')

    sys.stderr.write("#*\n")
    sys.stderr.write("#* %-17s%s\n" %("environ['PATH']", ":",))
    sys.stderr.write("#*\n")
    _path = os.environ['PATH'].split(os.pathsep)
    for p in _path:
        sys.stderr.write("%21s %s\n" %(":", str(p)))
    sys.stderr.write('\n')
    sys.stderr.flush()
        
    try:
        import pythonids.pythondist
        sys.stderr.write("\n#*\n#* RDBG:CLI:pythonids:\n#*\n")
        sys.stderr.write(str(pythonids.pythondist.PYDIST_DATA))
        sys.stderr.write('\n')
        sys.stderr.flush()
    except Exception:
        pass
        
    try:
        import platformids.platforms
        sys.stderr.write("\n#*\n#* RDBG:CLI:platformids:\n#*\n")
        _pparms = platformids.platforms.PlatformParameters()
        _pparms.scan()
        sys.stderr.write(str(_pparms))
        sys.stderr.write('\n')
        sys.stderr.flush()
    except Exception:
        pass

    sys.stderr.write('\n\n')
    sys.stderr.flush()

def main():
    ppretty_environment()
    
if __name__ in ("__main__", "yapyutils.prettyenv"):
    main()

sys.exit(0)
