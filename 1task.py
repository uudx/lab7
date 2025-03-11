import pygame
import time
import math
import pyautogui

pygame.init()

clock_bg = pygame.image.load(".\mickeyclock.jpeg") 
right_hand = pygame.image.load(".\r.jpeg") 
left_hand = pygame.image.load(".\l.jpeg")

w, h = clock_bg.get_size()
screen = pygame.display.set_mode((w, h))

center = (w // 2, h // 2)

def rotate_and_blit(image, angle, position):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=position)
    screen.blit(rotated_image, new_rect.topleft)

running = True
while running:
    print(pyautogui.position())
    screen.fill((255, 255, 255))
    screen.blit(clock_bg, (0, 0))
    
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    
    second_angle = -seconds * 6
    minute_angle = -minutes * 6
    
    rotate_and_blit(left_hand, second_angle, center)
    rotate_and_blit(right_hand, minute_angle, center)
    
    pygame.display.flip()
    pygame.time.delay(1000)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
