
python_project(
		NAME
			bqt
		VERSION
			0.1.0-devel
		AUTHORS
			"Sebastian Thiel <byronimo@gmail.com>"
		ROOT_PACKAGE
			bqt
		SPHINX_CONFIG_IN
			DEFAULT
		PYSIDE_UI_FILES
			bqt/widgets/ui/selector.ui
			bqt/hub/ui/window.ui
		SDKS
			pyside 1.2.1			
		DOXYFILE_IN
			DEFAULT
		)
