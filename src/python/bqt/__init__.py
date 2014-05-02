#-*-coding:utf-8-*-
"""
@package bqt
@brief Root package for general use gui components.

Use these components to build modular user interfaces

@copyright 2012 Sebastian Thiel
"""
# Allow better imports !
from __future__ import absolute_import

from butility import Version
__version__ = Version("0.1.0")

# quick and dirty
class ModuleProxy(object):
    """A standin which tries to import it's attribute from a list of modules, in order.

    It will delay actual imports to the last moment
    """
    __slots__ = '_module_names'

    def __init__(self, module_names):
        super(ModuleProxy, self).__init__()
        self._module_names = tuple(module_names)
        
    def __getattr__(self, name):
        """try to import name form a given module"""
        for mod_name in self._module_names:
            try:
                return __import__('%s.%s' % (mod_name, name), globals(), locals(), [name])
            except ImportError:
                pass
            # end try import
        # end for each name to try
        msg = "Couldn't import module '%s' from any module: %s" % (name, ', '.join(self._module_names))
        raise ImportError(msg)

        


mod = ModuleProxy(('PySide', 'PyQT'))

from .cmd import *
from .utility import *
