from conf import *

class Star:
    def __init__(self):
        self.p = (0,0)
        self.color = STAR_COLOR
        self.size = 0


class Planet:
    def __init__(self):
        self.p = (0,0)
        self.color = (0,0,0)
        self.size = 0
        self.ring = False
        self.ring_density = 0
        self.ring_tilt = 0


class Meteor:
    def __init__(self):
        self.p = (0,0)
        self.color = METEOR_COLOR
        self.size = 0
        self.vertices_num = 3
        self.vertices = []
        self.vertices_shade = []
        self.spin = ANGULAR_VELOCITY_METEOR


class Blaster:
    def __init__(self):
        self.p = (0,0)
        self.color = BLASTER_COLOR
        self.size = 0


class Spaceship:
    def __init__(self):
        self.p = (0,0)
        self.color = (0,0,0)
        self.size = 0


class Explosion:
    def __init__(self):
        self.p = (0,0)
        self.color = (0,0,0)
        self.size = 0
        self.conc = 0


class Enemy:
    def __init__(self):
        self.p = (0,0)
        self.color = (0,0,0)
        self.size = 0
