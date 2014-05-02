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

from .cmd import *
from .utility import *


