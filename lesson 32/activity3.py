import pygame

def main(): 
    pygame.init()
    screen_width,screen_height = 500,500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("color changing sprite")

    colours = {
        "red" : pygame.Color('red'),
        "green" : pygame.Color('green'),
        "blue" : pygame.Color('blue'),
        "yellow" : pygame.Color('yellow'),
        "white" : pygame.Color('white'),      
    }



    def make_darker_color(current_color):
        darker_color = pygame.Color(
            max(0, current_color.r - 80),
            max(0, current_color.g - 80),
            max(0, current_color.b - 80)
        )

        return darker_color

    def make_lighter_color(current_color):
        lighter_color = pygame.Color(
            min(255, current_color.r + 80),
            min(255, current_color.g + 80),
            min(255, current_color.b + 80)
        )

        return lighter_color


    current_color = colours["white"]
    x,y = 30,30

    sprite_width,sprite_height = 60,60 
    clock = pygame.time.Clock()
    done = False

    while not done: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x-=3
        if pressed[pygame.K_RIGHT]: x+=3
        if pressed[pygame.K_UP]: y-=3
        if pressed[pygame.K_DOWN]: y+=3

        x = min(max(0,x), screen_width - sprite_width)
        y = min(max(0,y), screen_height - sprite_height)

        if x == 0: current_color = colours["blue"]
        elif x == screen_width - sprite_width: current_color = colours["yellow"]
        elif y == 0: current_color = colours["red"]
        elif y == screen_height - sprite_height: current_color = colours["green"]
        else : current_color = colours["white"]

        screen.fill((0,0,0))
        pygame.draw.rect(screen,current_color,(x,y, sprite_width, sprite_height))
        pygame.draw.circle(screen,make_lighter_color(current_color), (100,100), radius=sprite_width, width=0 )
        pygame.draw.circle(screen, make_darker_color(current_color), (400,400), radius=sprite_width, width=3 )
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__": 
    main()
        