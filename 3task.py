import pygame

pygame.init()

w, h = 500, 500
r = 25
step_point = 20

screen = pygame.display.set_mode((w, h))

ball_x, ball_y = w // 2, h // 2

running = True
while running:
    screen.fill(255, 255, 255)
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), r)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - r - step_point >= 0:
                ball_y -= step_point
            elif event.key == pygame.K_DOWN and ball_y + r + step_point <= h:
                ball_y += step_point
            elif event.key == pygame.K_LEFT and ball_x - r - step_point >= 0:
                ball_x -= step_point
            elif event.key == pygame.K_RIGHT and ball_x + r + step_point <= w:
                ball_x += step_point
pygame.quit()
