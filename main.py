import pygame

# Initialize Pygame
pygame.init()

# Window settings
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Little 2D Game")

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
brown = (139, 69, 19)
dark_green = (0, 100, 0)

# Clock for FPS management
clock = pygame.time.Clock()

# Character settings
initial_character_x = 50
character_x = initial_character_x
camera_offset = 0
character_y = 400
character_width = 40
character_height = 60

# The speed is a float that represents the number of pixel by frame.
# It can be negative if we want to move in the left.
character_speed = 0

max_character_speed = 6
jump_power = 15
gravity = 1.2
vertical_speed = 0
character_color = (255, 0, 0)
sword_length = 30
attacking = False
attack_duration = 5
attack_timer = 0
moving_left = False
moving_right = False
is_jumping = False
lastPressed = None

# Camera settings
camera_x = 0
camera_speed = 100
camera_smoothing = 0.08

# Eyes settings
eye_radius = 9
pupil_radius = 6

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                vertical_speed = -jump_power
                is_jumping = True

    # Key pressing management
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] and lastPressed == pygame.K_d:
        character_speed = 0
    if keys[pygame.K_d] and lastPressed == pygame.K_q:
        character_speed = 0
    if keys[pygame.K_q] and character_speed > -max_character_speed:
        character_speed -= 0.7
        lastPressed = pygame.K_q
        moving_left = True
        moving_right = False
    if keys[pygame.K_d] and character_speed < max_character_speed:
        character_speed += 0.7
        lastPressed = pygame.K_d
        moving_right = True
        moving_left = False
    
    # If no keys are pressed reset the speed to 0
    if not keys[pygame.K_q] and not keys[pygame.K_d]:
        character_speed = 0
    
    if keys[pygame.K_e]:
        attacking = True
        attack_timer = attack_duration

    # Apply the character speed
    character_x += character_speed
    character_y += vertical_speed

    # Apply gravity
    vertical_speed += gravity
    if character_y >= 400:
        character_y = 400
        is_jumping = False
        vertical_speed = 0

    # Collisions with borders
    # if character_x < 0:
    #     character_x = 0
    # if character_x > window_width - character_width:
    #     character_x = window_width - character_width
    # Camera Logic
    target_camera_x = character_x - window_width // 2 + character_width // 2
    if moving_right:
        target_camera_x += window_width // 4
    elif moving_left:
        target_camera_x -= window_width // 4
    
    camera_x += (target_camera_x - camera_x) * camera_smoothing

    if attacking:
        attack_timer -= 1
        if attack_timer <= 0:
            attacking = False

    # Background
    screen.fill(dark_green)

    for i in range(100):
        pygame.draw.rect(screen, green, (i * 80 - camera_x, 200, 40, 100))

    pygame.draw.rect(screen, brown, (- camera_x, 460, window_width * 2, 140))


    # Draw character
    pygame.draw.rect(screen, character_color, (character_x - camera_x, character_y, character_width, character_height))

    # Draw eyes
    eye_x_offset = character_width // 4
    eye_y_offset = -15
    pupil_x_offset = 0
    if moving_left:
        pupil_x_offset = -3
    elif moving_right:
        pupil_x_offset = 3

    # Left eye
    left_eye_x = character_x + eye_x_offset - camera_x
    left_eye_y = character_y + eye_y_offset
    pygame.draw.circle(screen, white, (left_eye_x, left_eye_y), eye_radius)
    pygame.draw.circle(screen, (0,0,0), (left_eye_x + pupil_x_offset, left_eye_y), pupil_radius)
    # Right eye
    right_eye_x = character_x + character_width - eye_x_offset - camera_x
    right_eye_y = character_y + eye_y_offset
    pygame.draw.circle(screen, white, (right_eye_x, right_eye_y), eye_radius)
    pygame.draw.circle(screen, (0,0,0), (right_eye_x + pupil_x_offset, right_eye_y), pupil_radius)

    # Draw sword
    if attacking:
        if moving_left:
            sword_x = character_x
        else:
            sword_x = character_x + character_width
        sword_y = character_y + character_height // 2
        pygame.draw.line(screen, white, (sword_x - camera_x, sword_y), (sword_x - camera_x + (sword_length if not moving_left else -sword_length), sword_y), 5)

    # Refresh the display and set the fps to 60
    clock.tick(60)
    pygame.display.update()

pygame.quit()
