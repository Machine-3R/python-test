from src import pyguioo

if __name__ == "__main__":
    controlGUI = pyguioo.Control()
    resultGUI = pyguioo.Result()
    app = pyguioo.Application(controlGUI, resultGUI)
