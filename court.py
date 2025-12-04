from pico2d import load_image, get_canvas_width, get_canvas_height, clamp
import common

class Court:
    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        # fiil here
        self.w = self.image.w
        self.h = self.image.h

    def update(self):
        # fill here
        self.window_left = clamp(0, int(common.boy.x) - self.cw // 2, self.w - self.cw -1)
        self.window_bottom = clamp(0, int(common.boy.y) - self.ch // 2, self.h - self.ch -1)
        pass

    def draw(self):
        # self.image.draw(self.cw // 2, self.ch // 2)
        self.image.clip_draw_to_origin(
            self.window_left,
            self.window_bottom,
            self.cw, self.ch,
            0, 0
        )



class TileCourt:
    def __init__(self):
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()

        # fill here
        self.w = 800 * 6
        self.h = 600 * 6

        self.tiles = [ [load_image(('cube%d%d.png' % (x, y))) for x in range(3)] for y in range(3) ]


    def update(self):
        pass

    def draw(self):
        self.window_left = clamp(0, int(common.boy.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(common.boy.y) - self.ch // 2, self.h - self.ch - 1)

        # fill here
        tile_left = self.window_left // 800
        tile_right = (self.window_left + self.cw) // 800
        left_offset = self.window_left % 800

        tile_bottom = self.window_bottom // 600
        tile_top = (self.window_bottom + self.ch) // 600
        bottom_offset = self.window_bottom % 600

        for ty in range(tile_bottom, tile_top + 1):
            for tx in range(tile_left, tile_right + 1):
                self.tiles[ty % 3][tx % 3].draw_to_origin(
                    -left_offset + (tx - tile_left) * 800,
                    -bottom_offset + (ty - tile_bottom) * 600
                )




class InfiniteCourt:

    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)                        # quadrant 3
        self.image.clip_draw_to_origin(self.q4l, self.q4b, self.q4w, self.q4h, self.q3w, 0)                        # quadrant 3
        self.image.clip_draw_to_origin(self.q2l, self.q2b, self.q2w, self.q2h, 0, self.q3h)                        # quadrant 3
        self.image.clip_draw_to_origin(self.q1l, self.q1b, self.q1w, self.q1h, self.q3w, self.q3h)                        # quadrant 3
        # fill here

    def update(self):
        # quadrant 3
        self.q3l = (int(common.boy.x) - self.cw // 2) % self.w
        self.q3b = (int(common.boy.y) - self.ch // 2) % self.h
        self.q3w = clamp(0, self.w - self.q3l, self.cw)
        self.q3h = clamp(0, self.h - self.q3b, self.ch)
        # quadrant 2
        self.q2l = self.q3l
        self.q2b = 0
        self.q2w = self.q3w
        self.q2h = self.ch - self.q3h
        # quadrand 4
        self.q4l = 0
        self.q4b = self.q3b
        self.q4w = self.cw - self.q3w
        self.q4h = self.q3h
        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = self.q4w
        self.q1h = self.q2h


    def handle_event(self, event):
        pass

