from pico2d import load_image, get_canvas_width, get_canvas_height, clamp
import common

class Ball:
    def __init__(self, x, y):
        self.image = load_image('ball21x21.png')
        self.x = x
        self.y = y

    def draw(self):
        sx = self.x - common.court.window_left
        sy = self.y - common.court.window_bottom
        self.image.draw(sx, sy)

    def handle_collision(self, group, other):
        pass

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10