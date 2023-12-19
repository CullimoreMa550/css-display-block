

import pygame
import sys 
pygame.init()
screen_width = 800 
screen_height = 400 
screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("Moving Train") 
black = (0, 0, 0) 
red = (255, 0, 0) 
blue = (0, 0, 255) 
white = (255, 255, 255) 
gray = (169, 169, 169) 
yellow = (255, 255, 0)
car_width = 150 
car_height = 80 
gap = 20 
num_cars = 4 
train_speed = 2 
clock = pygame.time.Clock() 
def draw_train(x, y): 
    for i in range(num_cars): 
        pygame.draw.rect(screen, gray, (x + (car_width + gap) * i, y, car_width, car_height)) 
        pygame.draw.rect(screen, yellow, (x + 20 + (car_width + gap) * i, y + 10, 40, 40)) 
        pygame.draw.rect(screen, yellow, (x + 90 + (car_width + gap) * i, y + 10, 40, 40)) 
        pygame.draw.circle(screen, blue, (x + 30 + (car_width + gap) * i, y + car_height - 10), 10) 
        pygame.draw.circle(screen, blue, (x + 120 + (car_width + gap) * i, y + car_height - 10), 10)
        if i < num_cars - 1: 
            pygame.draw.rect(screen, black, (x + car_width + (car_width + gap) * i, y + car_height // 4, gap, car_height // 2)) 
train_x = 0 
train_y = screen_height // 2 - car_height // 2 
running = True 
while running: 
    screen.fill(black)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    train_x += train_speed 
# Reset train position when it goes off the screen 
    if train_x > screen_width: 
        train_x = -car_width * num_cars - gap * (num_cars - 1) 
    draw_train(train_x, train_y) 
    pygame.display.flip() 
    clock.tick(60) 
pygame.quit() 
sys.exit()
