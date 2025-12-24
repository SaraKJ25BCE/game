from things import *
from conf import *
import random

blasters = []
d_blasters = []
en_blasters = []

def get_blasters():
    global blasters
    return blasters

def get_d_blasters():
    global d_blasters
    return d_blasters

def get_en_blasters():
    global en_blasters
    return en_blasters

def is_seen(s):
    x, y = s.p
    lim = (WIDTH/2+s.size)*1.1
    t = -lim<=x and x<=lim
    return t


def shoot_en_blaster(x,y):
    global en_blasters
    s = Blaster()
    s.size = BLASTER_SIZE
    s.color = EN_BLASTER_COLOR
    s.p = (x,y)
    #s.size = (math.exp(-((1/random.random())-1)))*BLASTER_MAX_SIZE
    en_blasters.append(s)

def shoot_d_blaster(x,y):
    global d_blasters
    s = Blaster()
    s.size = BLASTER_SIZE
    s.p = (x,y)
    #s.size = (math.exp(-((1/random.random())-1)))*BLASTER_MAX_SIZE
    d_blasters.append(s)

def shoot_blaster(x,y):
    global blasters
    s = Blaster()
    s.size = BLASTER_SIZE
    s.p = (x,y)
    #s.size = (math.exp(-((1/random.random())-1)))*BLASTER_MAX_SIZE
    blasters.append(s)


def purge():
    global blasters,en_blasters,d_blasters
    new_blasters = []
    for s in blasters:
        if is_seen(s):
            new_blasters.append(s)
    blasters = new_blasters
    new_d_blasters = []
    for s in d_blasters:
        if is_seen(s):
            new_d_blasters.append(s)
    d_blasters = new_d_blasters
    new_en_blasters = []
    for s in en_blasters:
        if is_seen(s):
            new_en_blasters.append(s)
    en_blasters = new_en_blasters

def move(dt):
    global blasters,en_blasters,d_blasters
    # print("move: "+str(len(blasters)))
    for s in blasters:
        x, y = s.p
        x+=VELOCITY_BLASTER*dt
        s.p = (x,y)
    
    for s in d_blasters:
        x, y = s.p
        x+=VELOCITY_BLASTER*dt
        s.p = (x,y)

    for s in en_blasters:
        x, y = s.p
        x-=VELOCITY_BLASTER*dt
        s.p = (x,y)


def blasterlogic(dt):
    move(dt)
    purge()
    