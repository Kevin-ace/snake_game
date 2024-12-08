import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake initial position and direction
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 15
snake_dir = "RIGHT"

# Food position
food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game Over
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_dir != "RIGHT":
        snake_dir = "LEFT"
    if keys[pygame.K_RIGHT] and snake_dir != "LEFT":
        snake_dir = "RIGHT"
    if keys[pygame.K_UP] and snake_dir != "DOWN":
        snake_dir = "UP"
    if keys[pygame.K_DOWN] and snake_dir != "UP":
        snake_dir = "DOWN"

    # Move the snake
    if snake_dir == "LEFT":
        snake_pos[0] -= 10
    if snake_dir == "RIGHT":
        snake_pos[0] += 10
    if snake_dir == "UP":
        snake_pos[1] -= 10
    if snake_dir == "DOWN":
        snake_pos[1] += 10

    # Update snake body position
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food if eaten
    if not food_spawn:
        food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    food_spawn = True

    # Check for collision with boundaries
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        game_over = True
        break

    # Check for collision with itself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True
            break

    # Update screen
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    text = font.render("Score: " + str(score), True, white)
    screen.blit(text, [0, 0])
    pygame.display.update()

    # Control game speed
    pygame.time.Clock().tick(snake_speed)

# Quit Pygame
pygame.quit()
quit()