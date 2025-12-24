from things import *
from blasterlogic import *
from meteorlogic import *
from conf import *
import random

c,cd,ce = COOLDOWN,COOLDOWN,EN_COOLDOWN
ci1,ci2,ci3,ci4 = 1,1,1,1
cdi1,cdi2,cdi3,cdi4 = 1,1,1,1
ship_hit = 0
drone_hit = 0
ship_hitm = 0
drone_hitm = 0


ship = Spaceship()
drone = Spaceship()

def get_ship():
    global ship
    return ship

def get_drone():
    global drone
    return drone

def make_ship():
    global ship
    ship.size = SHIP_SIZE
    x = -WIDTH/2
    y = 0
    ship.p = (x,y)
    #s.size = (math.exp(-((1/random.random())-1)))*STAR_MAX_SIZE

def make_drone():
    global drone
    drone.size = DRONE_SIZE
    x = -WIDTH/2
    y = 0
    drone.p = (x,y)



def get_hits():
    global ship_hit,drone_hit
    return ship_hit,drone_hit

def cooldown(dt):
    global c,cd,ce
    global ci1,ci2,ci3,ci4
    global cdi1,cdi2,cdi3,cdi4

    if ci1<=1000:
        ci1+=INERTIA
    if ci2<=1000:
        ci2+=INERTIA
    if ci3<=1000:
        ci3+=INERTIA
    if ci4<=1000:
        ci4+=INERTIA
    if c<=COOLDOWN:
        c+=dt
    if cdi1<=1000:
        cdi1+=INERTIA
    if cdi2<=1000:
        cdi2+=INERTIA
    if cdi3<=1000:
        cdi3+=INERTIA
    if cdi4<=1000:
        cdi4+=INERTIA
    if cd<=COOLDOWN:
        cd+=dt
    if ce<=EN_COOLDOWN:
        ce+=dt
    
def shoot():
    global c
    if c>COOLDOWN:
        x,y = ship.p
        x+=BLASTER_SIZE-5
        shoot_blaster(x,y)
        x,y = ship.p
        x+=BLASTER_SIZE-5
        y-=ship.size-10
        shoot_blaster(x,y)
        c=0

def shoot_d():
    global cd
    if cd>COOLDOWN:
        x,y = drone.p
        x+=BLASTER_SIZE-5
        shoot_d_blaster(x,y)
        x,y = drone.p
        x+=BLASTER_SIZE-5
        y-=drone.size-10
        shoot_d_blaster(x,y)
        cd=0

def hit():
    global ship_hit,drone_hit
    explosions = get_explosions()
    en_blasters = get_en_blasters()
    m = get_meteors()
    for b in en_blasters:
        xb,yb = b.p
        xs,ys = ship.p
        if xb-b.size>xs and xb-b.size<xs+ship.size and yb<ys and yb>ys-ship.size:
            ship_hit+=1
            e = Explosion()
            e.p = (xb-b.size,yb)
            e.size = ship.size
            e.conc = EX_CONC
            explosions.append(e)
            b.p = (4000,2000)

    for b in en_blasters:
        xb,yb = b.p
        xs,ys = drone.p
        if xb-b.size>xs and xb-b.size<xs+drone.size and yb<ys and yb>ys-drone.size:
            drone_hit+=1
            e = Explosion()
            e.p = (xb-b.size,yb)
            e.size = drone.size
            e.conc = EX_CONC
            explosions.append(e)
            b.p = (4000,2000)

def enemy_fire():
    global ce
    enemies = get_enemies()
    if ce>EN_COOLDOWN:
        for e in enemies:
            if enemies.index(e)==random.randint(0,ENEMY_NUMBER):
                x,y = e.p
                x+=e.size
                y-=0*e.size
                shoot_en_blaster(x,y)
                x,y = e.p
                x+=e.size
                y-=e.size-10
                shoot_en_blaster(x,y)
        ce=0

def inertia(dt):
    global ship
    global ci1,ci2,ci3,ci4
    x,y = ship.p
    
    x-=VELOCITY_SHIP*dt/ci1
    x+=VELOCITY_SHIP*dt/ci2
    y+=VELOCITY_SHIP*dt/ci3
    y-=VELOCITY_SHIP*dt/ci4
    ship.p = (x,y)


def moveleft(dt):
    global ship
    global ci1
    x, y = ship.p
    x-=VELOCITY_SHIP*dt
    ship.p = (x,y)
    ci1 = 1

def moveright(dt):
    global ship
    global ci2
    x, y = ship.p
    x+=VELOCITY_SHIP*dt 
    ship.p = (x,y)
    ci2 = 1

def moveup(dt):
    global ship
    global ci3
    x, y = ship.p
    y+=VELOCITY_SHIP*dt
    ship.p = (x,y)
    ci3 = 1

def movedown(dt):
    global ship
    global ci4
    x, y = ship.p
    y-=VELOCITY_SHIP*dt
    ship.p = (x,y)
    ci4 = 1

def inertia_d(dt):
    global drone
    global cdi1,cdi2,cdi3,cdi4
    x,y = drone.p
    
    x-=VELOCITY_SHIP*dt/cdi1
    x+=VELOCITY_SHIP*dt/cdi2
    y+=VELOCITY_SHIP*dt/cdi3
    y-=VELOCITY_SHIP*dt/cdi4
    drone.p = (x,y)


def moveleft_d(dt):
    global drone
    global cdi1
    x, y = drone.p
    x-=VELOCITY_SHIP*dt
    drone.p = (x,y)
    cdi1 = 1

def moveright_d(dt):
    global drone
    global cdi2
    x, y = drone.p
    x+=VELOCITY_SHIP*dt
    drone.p = (x,y)
    cdi2 = 1

def moveup_d(dt):
    global drone
    global cdi3
    x, y = drone.p
    y+=VELOCITY_SHIP*dt
    drone.p = (x,y)
    cdi3 = 1

def movedown_d(dt):
    global drone
    global cdi4
    x, y = drone.p
    y-=VELOCITY_SHIP*dt
    drone.p = (x,y)
    cdi4 = 1



def is_seen():
    global ship
    x, y = ship.p
    if x>WIDTH/2:
        x=-WIDTH/2-ship.size
    if x<-WIDTH/2-ship.size:
        x=WIDTH/2
    if y<-HEIGHT/2:
        y=HEIGHT/2+ship.size
    if y>HEIGHT/2+ship.size:
        y=-HEIGHT/2
    ship.p = (x,y)

    global drone
    x, y = drone.p
    if x>WIDTH/2:
        x=-WIDTH/2-drone.size
    if x<-WIDTH/2-drone.size:
        x=WIDTH/2
    if y<-HEIGHT/2:
        y=HEIGHT/2+drone.size
    if y>HEIGHT/2+drone.size:
        y=-HEIGHT/2
    drone.p = (x,y)



def shiplogic(dt):
    cooldown(dt)
    inertia(dt)
    inertia_d(dt)
    is_seen()
    hit()
    enemy_fire()


def init_shiplogic():
    make_ship()
    make_drone()