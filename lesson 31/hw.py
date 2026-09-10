import pygame
exit = False

pygame.init()

screen_height = 500
screen_width = 500
screen = pygame.display.set_mode((screen_width, screen_height))

background_image = pygame.transform.scale(
    pygame.image.load("/Users/pirteeklakhani/Desktop/Yuvraj/Python/Python Codingal/lesson 31/jungle.png").convert(),
    (screen_width,screen_height)
)

wildlife_image = pygame.transform.scale(
    pygame.image.load("/Users/pirteeklakhani/Desktop/Yuvraj/Python/Python Codingal/lesson 31/tiger.png").convert_alpha(),
    (220,220)
)

wildlife_rect = wildlife_image.get_rect(
    center=(screen_width//2, screen_height//2+50)
)

clock = pygame.time.Clock()
done = False

while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    screen.blit(background_image, (0,0))
    screen.blit(wildlife_image, wildlife_rect)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()