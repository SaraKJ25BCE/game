from conf import *
from render import *
from starlogic import *
from planetlogic import *
from meteorlogic import *
from blasterlogic import *
from shiplogic import *


screen = pygame.display.set_mode((WIDTH, HEIGHT))
c = pygame.time.Clock()
pygame.display.set_caption("Demo")

def main():

    running = True
    init_starlogic()
    init_shiplogic()
    init_planetlogic()
    init_meteorlogic()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("time =",(pygame.time.get_ticks())/1000,"seconds")
                running = False

                
        dt = c.tick(MAX_FRAME_RATE)

        
        starlogic(dt)
        shiplogic(dt)
        planetlogic(dt)
        blasterlogic(dt)
        meteorlogic(dt)
        surface = pygame.Surface((WIDTH,HEIGHT))
        render(surface)
        screen.blit(surface,(0,0))

        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            moveleft(dt)
        if keys[pygame.K_RIGHT]:
            moveright(dt)
        if keys[pygame.K_UP]:
            moveup(dt)
        if keys[pygame.K_DOWN]:
            movedown(dt)
        if keys[pygame.K_x]:
            shoot()

        if keys[pygame.K_w]:
            moveup_d(dt)
        if keys[pygame.K_s]:
            movedown_d(dt)
        if keys[pygame.K_a]:
            moveleft_d(dt)
        if keys[pygame.K_d]:
            moveright_d(dt)
        if keys[pygame.K_m]:
            shoot_d()


        pygame.display.flip()       
        
        print(int(1000/dt))
        
        
main()