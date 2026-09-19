import pygame
import random 

pygame.init()

CAR_COLOR_EVENT = pygame.USEREVENT +1
SIGNAL_COLOR_EVENT = pygame.USEREVENT +2

ROAD_COLOR = pygame.Color("grey")

CAR_BLUE = pygame.Color('blue')
CAR_LIGHTBLUE = pygame.Color('lightblue')
CAR_DARKBLUE = pygame.Color('darkblue')

TLIGHT_RED = pygame.Color("red")
TLIGHT_YELLOW = pygame.Color("yellow")
TLIGHT_GREEN = pygame.Color("green")

class Car(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 30))
        self.image.fill(CAR_DARKBLUE)
        self.velocity = 3
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.move_ip(self.velocity, 0)
        boundary_hit = False
        if self.rect.left <=0 or self.rect.right >= 600: 
            self.velocity = -self.velocity
            boundary_hit = True

        if boundary_hit: 
            pygame.event.post(pygame.event.Event(CAR_COLOR_EVENT))
            pygame.event.post(pygame.event.Event(SIGNAL_COLOR_EVENT))

    def change_color(self): 
        self.image.fill(random.choice([CAR_LIGHTBLUE, CAR_DARKBLUE, CAR_BLUE]))



screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Smart Traffic Simulator")

car1 = Car()
group = pygame.sprite.Group()
group.add(car1)
car1.rect.x = 50
car1.rect.y = 322

exit = False 
clock = pygame.time.Clock()

signal_color = TLIGHT_RED

def change_signal(): 
    global signal_color 
    current_color = signal_color
    while True: 
        signal_color = random.choice([TLIGHT_RED,TLIGHT_YELLOW,TLIGHT_GREEN])
        if signal_color == current_color: 
            continue
        break
        




while not exit: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit = True

        elif event.type == CAR_COLOR_EVENT:
            car1.change_color()

        elif event.type == SIGNAL_COLOR_EVENT: 
            change_signal()


    group.update()
    screen.fill(ROAD_COLOR)

    for x in range(0,600,80): 
        pygame.draw.rect(screen,pygame.Color("black"), (x, 354, 45, 5))

    pygame.draw.rect(screen,pygame.Color("black"), (275, 40, 50, 90))

    pygame.draw.circle(screen,signal_color, (300,85), 20)


    group.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()