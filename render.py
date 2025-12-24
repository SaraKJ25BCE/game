from starlogic import *
from planetlogic import *
from meteorlogic import *
from blasterlogic import *
from shiplogic import *

def transform(p):
    x, y = p
    return (WIDTH/2+x, HEIGHT/2-y)

def random_centre(p,radius):
    x, y = p
    theta = random.random()*2*math.pi
    x+=math.cos(theta)*radius
    y+=math.sin(theta)*radius
    return (x,y)

def random_line_centre(p,length):
    x,y = p
    x-=(random.random())*length
    y+=(random.random()-0.5)*5
    return (x,y)

def render(surface):
    stars = get_stars()
    planets = get_planets()
    enemies = get_enemies()
    meteors = get_meteors()
    explosions = get_explosions()
    blasters = get_blasters()
    d_blasters = get_d_blasters()
    en_blasters = get_en_blasters()
    spaceship = get_ship()

    # print(len(stars))
    
    for s in stars:
        red_surface = pygame.Surface((2*s.size,2*s.size))
        green_surface = pygame.Surface((2*s.size,2*s.size))
        blue_surface = pygame.Surface((2*s.size,2*s.size))
        pygame.draw.circle(red_surface, (25,0,0), (s.size,s.size), s.size)
        pygame.draw.circle(green_surface, (0,25,0), (s.size,s.size), s.size)
        pygame.draw.circle(blue_surface, (0,0,25), (s.size,s.size), s.size)
        for i in range(10):
            x, y = transform(random_centre(s.p,FLICKER*random.random()))
            surface.blit(red_surface,(x-s.size,y-s.size),special_flags=pygame.BLEND_RGB_ADD)
            x, y = transform(random_centre(s.p,FLICKER*random.random()))
            surface.blit(green_surface,(x-s.size,y-s.size),special_flags=pygame.BLEND_RGB_ADD)
            x, y = transform(random_centre(s.p,FLICKER*random.random()))
            surface.blit(blue_surface,(x-s.size,y-s.size),special_flags=pygame.BLEND_RGB_ADD)
            #pygame.draw.circle(surface, s.color, transform(random_centre(s.p,s.size*random.random()*2)), s.size)



    for i in range(len(planets)):
        for j in range(i,len(planets)):
            if planets[i].size>planets[j].size:
                planets[i],planets[j] = planets[j],planets[i]
        
    for p in planets:
        p_surface = pygame.Surface((2.5*p.size,2.5*p.size),pygame.SRCALPHA)
        r,g,b = p.color
        for i in range(0,200,3):
            pygame.draw.circle(p_surface, (r+i,g+i,b+i), (p.size-i,p.size-i), p.size-(math.sqrt(2.5))*i)
        x, y = transform(p.p)
        if p.ring == True:
            for i in range(10):
                pygame.draw.arc(p_surface, p.color, (0,p.size+i,2*p.size,0.5*p.size+i), math.pi/1.015,math.pi/9,width = 1)
        surface.blit(p_surface,(x-p.size,y-p.size),special_flags=pygame.BLEND_ALPHA_SDL2)




    for m in meteors:
        m_surface = pygame.Surface((4*m.size,4*m.size),pygame.SRCALPHA)
        pygame.draw.polygon(m_surface, m.color, m.vertices)
        pygame.draw.lines(m_surface, (0,0,0), True, m.vertices)
        a = len(m.vertices)
        '''for i in range(a):
            for j in range(i):
                if abs(i-j)>1:
                    pygame.draw.line(m_surface, (0,0,0), m.vertices[i], m.vertices[j])'''
        x, y = transform(m.p)
        surface.blit(m_surface,(x-2*m.size,y-2*m.size),special_flags=pygame.BLEND_ALPHA_SDL2)

    for e in enemies:
        en_surface = pygame.Surface((e.size,e.size),pygame.SRCALPHA)
        t = e.size
        pygame.draw.polygon(en_surface, ENEMY_COLOR, ([0,0],[0,t],[t,0],[t,t]))
        pygame.draw.lines(en_surface, (0,0,0), True, ([0,0],[0,t],[t/2,t/2],[t,0],[t,t]))
        x, y = transform(e.p)
        surface.blit(en_surface,(x,y),special_flags=pygame.BLEND_ALPHA_SDL2)

    for e in explosions:
        e_surface = pygame.Surface((2*e.size,2*e.size))
        pygame.draw.circle(e_surface, EXPLOSION_COLOR, (e.size,e.size), e.size)
        for i in range(e.conc):
            x, y = transform(random_centre(e.p,FLICKER*5*random.random()))
            surface.blit(e_surface,(x-e.size,y-e.size),special_flags=pygame.BLEND_RGB_ADD)



    for b in blasters:
        bo_surface = pygame.Surface((10,10))
        bl_surface = pygame.Surface((b.size,10))
        pygame.draw.circle(bo_surface, BLASTER_COLOR, (5,5), 5)
        for i in range(1):
            pygame.draw.line(bl_surface, BLASTER_COLOR, (0,5),(b.size,5),width = 8)
        b_surface = pygame.Surface((b.size+15,20))
        b_surface.blit(bl_surface,(5,5),special_flags=pygame.BLEND_RGB_ADD)
        for i in range(150):
            x,y = (random_line_centre((b.size+5,5),b.size))
            b_surface.blit(bo_surface,(x,y),special_flags=pygame.BLEND_RGB_ADD)
        x,y = transform(b.p)
        surface.blit(b_surface, (x-b.size,y-5),special_flags=pygame.BLEND_RGBA_MAX)

    for b in d_blasters:
        dbo_surface = pygame.Surface((10,10))
        dbl_surface = pygame.Surface((b.size,10))
        pygame.draw.circle(dbo_surface, D_BLASTER_COLOR, (5,5), 5)
        pygame.draw.line(dbl_surface, D_BLASTER_COLOR, (0,5),(b.size,5),width = 8)
        db_surface = pygame.Surface((b.size+15,20))
        db_surface.blit(dbl_surface,(5,5),special_flags=pygame.BLEND_RGB_ADD)
        for i in range(150):
            x,y = (random_line_centre((b.size+5,5),b.size))
            db_surface.blit(dbo_surface,(x,y),special_flags=pygame.BLEND_RGB_ADD)
        x,y = transform(b.p)
        surface.blit(db_surface, (x-b.size,y-5),special_flags=pygame.BLEND_RGBA_MAX)

    for b in en_blasters:
        ebo_surface = pygame.Surface((10,10))
        ebl_surface = pygame.Surface((b.size,10))
        pygame.draw.circle(ebo_surface, EN_BLASTER_COLOR, (5,5), 5)
        pygame.draw.line(ebl_surface, EN_BLASTER_COLOR, (0,5),(b.size,5),width = 8)
        eb_surface = pygame.Surface((b.size+15,20))
        eb_surface.blit(ebl_surface,(5,5),special_flags=pygame.BLEND_RGB_ADD)
        for i in range(150):
            x,y = (random_line_centre((b.size+5,5),b.size))
            eb_surface.blit(ebo_surface,(x,y),special_flags=pygame.BLEND_RGB_ADD)
        x,y = transform(b.p)
        surface.blit(eb_surface, (x-b.size,y-5),special_flags=pygame.BLEND_RGBA_MAX)




    ss_surface = pygame.Surface((ship.size,ship.size),pygame.SRCALPHA)
    t = ship.size
    pygame.draw.polygon(ss_surface, SHIP_COLOUR, ([0,0],[t,t/2],[0,t],[t/4,t/2]))
    pygame.draw.lines(ss_surface, (0,0,0), True, ([0,0],[t,t/2],[0,t],[t/4,t/2]))
    x, y = transform(ship.p)
    surface.blit(ss_surface,(x,y),special_flags=pygame.BLEND_ALPHA_SDL2)

    sd_surface = pygame.Surface((drone.size,drone.size),pygame.SRCALPHA)
    t = drone.size
    pygame.draw.polygon(sd_surface, DRONE_COLOUR, ([0,0],[t,t/2],[0,t],[t/4,t/2]))
    pygame.draw.lines(sd_surface, (0,0,0), True, ([0,0],[t,t/2],[0,t],[t/4,t/2]))
    x, y = transform(drone.p)
    surface.blit(sd_surface,(x,y),special_flags=pygame.BLEND_ALPHA_SDL2)

    pygame.init()
    font = pygame.font.Font(None, 32)
    t1,t2 = get_score()
    t3,t4 = get_d_score()
    t5,t6 = get_hits()
    st1 = 'Meteors: '+str(t1)
    st2 = 'Enemies: '+str(t2)
    st3 = 'Meteors: '+str(t3)
    st4 = 'Enemies: '+str(t4)
    st5 = 'Hits: '+str(t5)
    st6 = 'Hits: '+str(t6)
    text1 = font.render(st1, True, (0,255,255))
    text2 = font.render(st2, True, (0,255,255))
    text3 = font.render(st3, True, (0,255,255))
    text4 = font.render(st4, True, (0,255,255))
    text5 = font.render(st5, True, (0,255,255))
    text6 = font.render(st6, True, (0,255,255))
    texts = font.render('p1', True, (0,255,255))
    textd = font.render('p2', True, (0,255,255))
    text1Rect = text1.get_rect()
    text2Rect = text2.get_rect()
    text3Rect = text3.get_rect()
    text4Rect = text4.get_rect()
    text5Rect = text5.get_rect()
    text6Rect = text6.get_rect()
    textsRect = texts.get_rect()
    textdRect = textd.get_rect()
    text1Rect.center = (WIDTH // 1.1, HEIGHT // 9)
    text2Rect.center = (WIDTH // 1.1, HEIGHT // 7)
    text3Rect.center = (WIDTH // 10.1, HEIGHT // 9)
    text4Rect.center = (WIDTH // 10.1, HEIGHT // 7)
    text5Rect.center = (WIDTH // 1.1, HEIGHT // 5)
    text6Rect.center = (WIDTH // 10.1, HEIGHT // 5)
    textsRect.center = (WIDTH // 1.1, HEIGHT // 20)
    textdRect.center = (WIDTH // 10.1, HEIGHT // 20)
    surface.blit(text1,text1Rect)
    surface.blit(text2,text2Rect)
    surface.blit(text3,text3Rect)
    surface.blit(text4,text4Rect)
    surface.blit(text5,text5Rect)
    surface.blit(text6,text6Rect)
    surface.blit(texts,textsRect)
    surface.blit(textd,textdRect)
