from things import *
from conf import *
import random

stars = []

def get_stars():
    global stars
    return stars

def is_seen(s):
    x, y = s.p
    lim = (WIDTH/2+s.size)*1.1
    t = (-lim <= x) and (x <= lim)
    return t

def make_star(random_x=False):
    global stars
    s = Star()
    s.size = random.random()*STAR_MAX_SIZE
    x = WIDTH/2+s.size
    if random_x:
        x = (random.random()-0.5)*WIDTH
    y = (random.random()-0.5)*HEIGHT
    s.p = (x,y)
    #s.size = (math.exp(-((1/random.random())-1)))*STAR_MAX_SIZE
    assert is_seen(s)
    stars.append(s)

def renew():
    global stars
    num = STAR_NUMBER - len(stars)
    # print("num: "+str(num))
    for i in range(num):
        make_star()

def purge():
    global stars
    new_stars = []
    for s in stars:
        if is_seen(s):
            new_stars.append(s)
    # print("purged: "+str(len(new_stars)-len(stars)))
    stars = new_stars

def move(dt):
    global stars
    # print("move: "+str(len(stars)))
    for s in stars:
        x, y = s.p
        x-=VELOCITY_STAR*s.size*dt
        s.p = (x,y)

def starlogic(dt):
    move(dt)
    renew()
    purge()
    
def init_starlogic():
    for i in range(STAR_NUMBER):
        make_star(random_x=True)
    
    