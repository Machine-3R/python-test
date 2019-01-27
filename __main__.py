#!/usr/bin/env python
import src as pyguioo
if __name__ == "__main__":
    controlGUI = pyguioo.Control()
    resultGUI = pyguioo.Result()
    pyguioo.Application(controlGUI, resultGUI)
