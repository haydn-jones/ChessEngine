import pyglet
from pyglet.window import mouse
from resources.resources import ResourceFactory

class Renderer(pyglet.window.Window):
    def __init__(self):
        super().__init__(width=900, height=900)
        self.exited = False

        self.resources = ResourceFactory()
        self.resources.set_scale(self.width, self.height)

        self.sprites = []
        self.load_sprites()

    def load_sprites(self):
        self.board = self.resources.get_sprite('board')

    def on_draw(self):
        self.clear()
        self.board.draw()
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print('The left mouse button was pressed.')
    
    def on_close(self):
        self.exited = True
        self.close()

    def run_loop(self):
        pyglet.clock.tick()

        self.switch_to()
        self.dispatch_events()
        self.dispatch_event('on_draw')
        self.flip()