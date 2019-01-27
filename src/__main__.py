#!/usr/bin/env python
if __name__ == "__main__":
	from application import Application
	from gui import Control, Result
	controlGUI = Control()
	resultGUI = Result()
	Application(controlGUI, resultGUI)

