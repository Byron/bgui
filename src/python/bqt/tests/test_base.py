#-*-coding:utf-8-*-
"""
@package bqt.tests.test_base
@brief tests for bqt

@author Sebastian Thiel
@copyright [GNU Lesser General Public License](https://www.gnu.org/licenses/lgpl.html)
"""
__all__ = []

from butility.tests import TestCaseBase

# Test from * import 
from bqt import *
from bqt.widgets import *


class TestCase(TestCaseBase):
    """Minimal tests for bqt - it's quite difficult to test GUIs properly"""

