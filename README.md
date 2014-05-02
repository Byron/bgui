This project contains all code which depends on qt in one way or another. Usually those are generalized widgets.

Those are meant to be used in specialized user interfaces.

Additionally it provides a simple abstraction layer to the python wrapper for QT. Even though [PySide](http://qt-project.org/wiki/PySide) is assumed to be the native one, [PyQT](http://www.riverbankcomputing.co.uk/software/pyqt/intro) should work just as good for the most part. `bqt` will figure out the details, allowing your code to `import bqt.get.QtGui`.

### Usage and Installation

As this is a library project, you won't use it standalone. Instead, consider having a look at the [bdevel assembly](https://github.com/Byron/bdevel-assembly), which has some tools that make use of it.

### Requirements

* [bcore](https://github.com/Byron/bcore)
* [PySide](https://github.com/Byron/bdep-pyside)
    - It possibly works with PyQT, but is currently not tested with it

### LICENSE

GNU LESSER GENERAL PUBLIC LICENSE, see LICENSE file for details.
