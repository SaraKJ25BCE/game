from things import *
from blasterlogic import *
from conf import *
import random

meteors = []
enemies = []
explosions = []
hits1 = 0
hits2 = 0
hitse1 = 0
hitse2 = 0

def get_score():
    global hits1,hitse1
    return (hits1,hitse1)

def get_d_score():
    global hits2,hitse2
    return (hits2,hitse2)

def get_explosions():
    global explosions
    return explosions

def get_meteors():
    global meteors
    return meteors

def get_enemies():
    global enemies
    return enemies

def explode(s,p=(0,0)):  #if enemy, coordinates are given. else meteor.
    global hits1,hitse1
    blasters = get_blasters()
    for b in blasters:
        xb,yb = b.p
        xs,ys = s.p
        if xb<xs+s.size and xb>xs-s.size and yb<ys+s.size and yb>ys-s.size:
            if p == (0,0):
                p = s.p
                hits1+=1
            else:
                hitse1+=1
            #print("hits",hits1)
            e = Explosion()
            e.p = p
            e.size = s.size
            e.conc = EX_CONC
            explosions.append(e)
            s.p = (4000,2000)
            b.p = (4000,2000)
            


    global hits2,hitse2
    d_blasters = get_d_blasters()
    for b in d_blasters:
        xb,yb = b.p
        xs,ys = s.p
        if xb<xs+s.size and xb>xs-s.size and yb<ys+s.size and yb>ys-s.size:
            if p == (0,0):
                p = s.p
                hits2+=1
            else:
                hitse2+=1
            #print("hits",hits2)
            e = Explosion()
            e.p = p
            e.size = s.size
            e.conc = EX_CONC
            explosions.append(e)
            s.p = (4000,2000)
            b.p = (4000,2000)

    en_blasters = get_en_blasters()
    for b in en_blasters:
        xb,yb = b.p
        xs,ys = s.p
        if xb-b.size<xs+s.size and xb-b.size>xs-s.size and yb<ys+s.size and yb>ys-s.size:
            if p == (0,0):
                p = s.p
            else:
                continue
            #print("hits",hits1)
            e = Explosion()
            e.p = p
            e.size = s.size
            e.conc = EX_CONC
            explosions.append(e)
            s.p = (4000,2000)
            b.p = (4000,2000)

def is_seen(s):
    x, y = s.p
    lim = (WIDTH/2+s.size)*1.1
    t = (-lim <= x) and (x <= lim)
    return t

def make_meteor(random_x=False):
    global meteors
    s = Meteor()
    tc=random.randint(45,100)
    s.color = (tc,tc,tc)
    s.size = (abs(random.random()-0.5)+0.5)*METEOR_MAX_SIZE

    n = 5+int(random.random()*METEOR_MAX_VERTICES)
    s.vertices_num = n
    theta = math.pi*2/n
    low = math.sqrt((s.size*s.size)+(s.size*s.size))
    for i in range (n):
        rx = (abs(random.random()-0.5)+0.5)*s.size
        ry = (abs(random.random()-0.5)+0.5)*s.size
        x,y = rx*math.cos(i*theta),ry*math.sin(i*theta)
        if math.sqrt((rx*rx)+(ry*ry))<low/1.19:
            #low = math.sqrt((rx*rx)+(ry*ry))
            s.vertices_shade.append((x+2*s.size,y+2*s.size))
        s.vertices.append((x+2*s.size,y+2*s.size))
    

    s.spin = ANGULAR_VELOCITY_METEOR/s.vertices_num
    
    x = WIDTH/2+s.size
    if random_x:
        x = abs(random.random()-0.5)*WIDTH
    y = (random.random()-0.5)*HEIGHT
    s.p = (x,y)
    meteors.append(s)


def make_enemy():
    e = Enemy()
    x = WIDTH/2
    y = (random.random()-0.5)*HEIGHT
    e.p = (x,y)
    e.size = ENEMY_SIZE
    enemies.append(e)


def renew():
    global meteors
    num = METEOR_NUMBER - len(meteors)
    # print("num: "+str(num))
    for i in range(num):
        make_meteor()

    global enemies
    num = ENEMY_NUMBER - len(enemies)
    # print("num: "+str(num))
    for i in range(num):
        make_enemy()

def purge():
    global meteors
    new_meteors = []
    for s in meteors:
        explode(s)
        if is_seen(s):
            new_meteors.append(s)
    # print("purged: "+str(len(new_meteors)-len(meteors)))
    meteors = new_meteors

    global enemies
    new_enemies = []
    for e in enemies:
        x,y = e.p
        x+=e.size/2
        y-=e.size/2
        explode(e,(x,y))
        if is_seen(e):
            new_enemies.append(e)
    # print("purged: "+str(len(new_meteors)-len(meteors)))
    enemies = new_enemies

def exploding(dt):
    global explosions
    new_explosions = []
    for e in explosions:
        e.conc-=DIFFUSION
        if e.conc>0:
            new_explosions.append(e)
    explosions = new_explosions


def move(dt):
    global meteors
    # print("move: "+str(len(meteors)))
    for s in meteors:
        x, y = s.p
        x-=VELOCITY_METEOR*dt/s.vertices_num
        s.p = (x,y)

def move_en(dt):
    global enemies
    # print("move: "+str(len(meteors)))
    for s in enemies:
        x, y = s.p
        x-=VELOCITY_ENEMY*dt
        s.p = (x,y)

def transform(x,y,w,dt):
    theta = math.atan2(y,x)
    theta+=w*dt
    r = math.sqrt((x*x)+(y*y))
    return (r*math.cos(theta),r*math.sin(theta))

def spin(dt):
    global meteors
    for s in meteors:
        for v in s.vertices_shade:
            x,y = v
            t = (s.vertices_shade).index(v)
            a,b = transform(x-2*s.size,y-2*s.size,s.spin,dt)
            s.vertices_shade[t] = (a+2*s.size,b+2*s.size)
        for v in s.vertices:
            x,y = v
            t = (s.vertices).index(v)
            a,b = transform(x-2*s.size,y-2*s.size,s.spin,dt)
            s.vertices[t] = (a+2*s.size,b+2*s.size)


def meteorlogic(dt):
    renew()
    move(dt)
    move_en(dt)
    spin(dt)
    purge()
    exploding(dt)

def init_meteorlogic():
    for i in range(METEOR_NUMBER):
        make_meteor(random_x=True)
    for i in range(ENEMY_NUMBER):
        make_enemy()
    
    
    
    