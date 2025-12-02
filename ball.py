from pico2d import load_image, get_canvas_width, get_canvas_height, clamp
import common
import game_world


class Ball:
    def __init__(self, x, y):
        self.image = load_image('ball21x21.png')
        self.x = x
        self.y = y

    def draw(self):
        sx = self.x - common.court.window_left
        sy = self.y - common.court.window_bottom
        self.image.draw(sx, sy)

    def handle_collision(self, key, other):
        if key == 'boy:ball':
            common.balls.remove(self)
            game_world.remove_object(self)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10