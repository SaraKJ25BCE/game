from things import *
from conf import *
import random

planets = []

def get_planets():
    global planets
    return planets

def is_seen(s):
    x, y = s.p
    lim = (WIDTH/2+s.size)*1.1
    t = (-lim <= x) and (x <= lim)
    return t

def make_planet(random_x=False):
    global planets
    s = Planet()
    s.color = (random.randint(0,55),random.randint(0,55),random.randint(0,55))
    s.ring = random.randint(0,1)
    s.size = (abs(random.random()-0.5)+0.5)*PLANET_MAX_SIZE
    x = WIDTH/2+s.size
    if random_x:
        x = (random.random()-0.5)*WIDTH
    y = (random.random()-0.5)*HEIGHT
    s.p = (x,y)
    assert is_seen(s)
    planets.append(s)

def renew():
    global planets
    num = PLANET_NUMBER - len(planets)
    # print("num: "+str(num))
    for i in range(num):
        make_planet()

def purge():
    global planets
    new_planets = []
    for s in planets:
        if is_seen(s):
            new_planets.append(s)
    # print("purged: "+str(len(new_planets)-len(planets)))
    planets = new_planets

def move(dt):
    global planets
    # print("move: "+str(len(planets)))
    for s in planets:
        x, y = s.p
        x-=VELOCITY_PLANET*s.size*dt
        s.p = (x,y)

def planetlogic(dt):
    renew()
    move(dt)
    purge()
    
def init_planetlogic():
    for i in range(PLANET_NUMBER):
        make_planet(random_x=True)
    
    