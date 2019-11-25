import pyglet
from pyglet.window import mouse
from resources.resources import load_images

class Renderer(pyglet.window.Window):
    def __init__(self):
        super().__init__(width=800, height=800, vsync=False, resizable=True)
        self.exited = False

        self.images = {}
        self.load_resources()

        self.sprite_scale = 1
        self.sprites = []
        self.load_sprites()

    def load_resources(self):
        self.images = load_images()

    def load_sprites(self):
        self.board = pyglet.sprite.Sprite(self.images['board'])

    def on_resize(self, width, height):
        super().on_resize(width, height)

        factor_x = self.width  / self.board_img.width
        factor_y = self.height / self.board_img.height

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