from pywinauto import Desktop


desktop = Desktop(backend="uia")
screen_width = desktop.screen.width()
screen_height = desktop.screen.height()
print(screen_width, screen_height)