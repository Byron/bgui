#-*-coding:utf-8-*-
"""
@package bqt.hub.controller
@brief Main hub controller widget

@copyright 2013 Sebastian Thiel
"""
__all__ = ['HubController']

from bqt.mod import QtGui
from .res import Ui_HubWindow
from .interfaces import IHubPanel


class HubController(QtGui.QMainWindow):
    """A main window with dock-widget support"""
    
    def __init__(self, *args):
        super(HubController, self).__init__(*args)
        self.ui = Ui_HubWindow()
        self.ui.setupUi(self)
        
    # -------------------------
    ## @name Interface
    # @{
    
    def init(self):
        """Initialize this instance
        @return self
        @todo"""
        # DEBUG: For now get a a wiget and try to put it as central widget
        # This is not the way it should be ! We just ease debugging
        
        for cls in self.application().context().types(IHubPanel):
            self.setCentralWidget(cls(self).init())
            break
        # end set central widget
        
        return self
        
    ## -- End Interface -- @}

# end class HubController




