import pyglet
from pyglet.window import mouse
from pyglet.image.codecs.png import PNGImageDecoder

class Renderer(pyglet.window.Window):
    def __init__(self):
        super().__init__()

        self.label = pyglet.text.Label('Hello, world!')
        self.board = pyglet.image.load("./resources/board.png", decoder=PNGImageDecoder())

    def on_draw(self):
        self.clear()
        self.label.draw()
        self.board.blit(0, 0)
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print('The left mouse button was pressed.')
    
    def run(self):
        pyglet.app.run()
