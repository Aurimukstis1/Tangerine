#/////////////////////////////////////////////////////////////////////////////////////
#@author: @aurimukstis1 / github: https://github.com/Aurimukstis1
#> GNU General Public License v3.0
#/////////////////////////////////////////////////////////////////////////////////////
import pygame
import math
import os
import webbrowser

# Initialize Pygame
pygame.init()

loading = 0

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.NOFRAME)
pygame.display.set_caption('Tangerine loader')

icon = pygame.image.load(os.path.join(os.path.dirname(__file__), 'icon.png'))
pygame.display.set_icon(icon)

rotation_speed_coefficient = 0.2; # The higher this number, the faster the cube will rotate
cube_size_coefficient = 1; # The higher this number, the bigger the cube will be

#>>># Colors list
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_RED = (255, 0, 0)
C_GREEN = (0, 255, 0)
C_BLUE = (0, 0, 255)
C_MATTE = (20, 20, 20)
C_LIGHT_MATTE = (30, 30, 30)
#>>>#

# Set up the game loop
running = True

# Set up the cube
CUBE_SIZE = 100
cube_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
cube_angles = [0, 0, 0] # X, Y, Z angles

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()

    # Update the cube angles
    cube_angles[0] += 1*rotation_speed_coefficient # Rotate the cube along the X axis
    cube_angles[1] += 1*rotation_speed_coefficient # Rotate the cube along the Y axis
    cube_angles[2] += 2*rotation_speed_coefficient # Rotate the cube along the Z axis

    # Fill the screen with a color
    try:
        screen.fill(C_MATTE)
    except:
        pass # If the screen is not initialized, ignore the error

    # Draw a grid on the background
    try:
        if pygame.mouse.get_focused():
            for i in range(0, SCREEN_WIDTH, round(SCREEN_WIDTH/3)):
                pygame.draw.line(screen, C_LIGHT_MATTE, (i, 0), (i, SCREEN_HEIGHT))
            for i in range(0, SCREEN_HEIGHT, round(SCREEN_WIDTH/3)):
                pygame.draw.line(screen, C_LIGHT_MATTE, (0, i), (SCREEN_WIDTH, i))
    except:
        pass # If the screen is not initialized, ignore the error

    "This is the loading bar code" ##############################
    # Add the `#` characters to the loading bar string
    loading_bar = ''
    for i in range(round(loading)):
        loading_bar += '#'

    # Add spaces to fill the rest of the loading bar
    for i in range(round(loading), 10):
        loading_bar += ' '

    # Draw text on the screen below the cube, centered
    font = pygame.font.SysFont('cambriamath', 20)
    text = font.render('Tangerine', True, C_WHITE)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 100)

    # Draw the loading bar text on the screen below the cube, centered
    loading_text = font.render(loading_bar, True, C_WHITE)
    loading_text_rect = loading_text.get_rect()
    loading_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 80)

    # Draw text on the screen below the cube, centered
    copyright_text = font.render('github.com/Aurimukstis1', True, C_LIGHT_MATTE)
    copyright_text_rect = copyright_text.get_rect()
    copyright_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 40)

    # If mouse if over the copyright text, change the color
    if copyright_text_rect.collidepoint(pygame.mouse.get_pos()):
        copyright_text = font.render('github.com/Aurimukstis1', True, C_WHITE)
    # if mouse is over the copyright text, go to the github page
    if copyright_text_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            webbrowser.open('https://github.com/Aurimukstis1')

    if pygame.mouse.get_focused():
        screen.blit(text, text_rect)
        screen.blit(loading_text, loading_text_rect)
        screen.blit(copyright_text, copyright_text_rect)
    ##############################################################

    # Calculate the coordinates of each point on the cube
    point_list = []
    for x in (-1, 1):
        for y in (-1, 1):
            for z in (-1, 1):
                point_list.append((x*CUBE_SIZE/2, y*CUBE_SIZE/2, z*CUBE_SIZE/2))

    # Rotate the cube along the X axis
    for i in range(len(point_list)):
        point = point_list[i]
        x = point[0]
        y = point[1]*math.cos(math.radians(cube_angles[0])) - point[2]*math.sin(math.radians(cube_angles[0]))
        z = point[1]*math.sin(math.radians(cube_angles[0])) + point[2]*math.cos(math.radians(cube_angles[0]))
        point_list[i] = (x, y, z)

    # Rotate the cube along the Y axis
    for i in range(len(point_list)):
        point = point_list[i]
        x = point[0]*math.cos(math.radians(cube_angles[1])) + point[2]*math.sin(math.radians(cube_angles[1]))
        y = point[1]
        z = -point[0]*math.sin(math.radians(cube_angles[1])) + point[2]*math.cos(math.radians(cube_angles[1]))
        point_list[i] = (x, y, z)
    
    # Rotate the cube along the Z axis
    for i in range(len(point_list)):
        point = point_list[i]
        x = point[0]*math.cos(math.radians(cube_angles[2])) - point[1]*math.sin(math.radians(cube_angles[2]))
        y = point[0]*math.sin(math.radians(cube_angles[2])) + point[1]*math.cos(math.radians(cube_angles[2]))
        z = point[2]
        point_list[i] = (x, y, z)

    # Resize the cube
    for i in range(len(point_list)):
        point = point_list[i]
        x = point[0]*cube_size_coefficient
        y = point[1]*cube_size_coefficient
        z = point[2]*cube_size_coefficient
        point_list[i] = (x, y, z)
    
    # Draw the cube
    for i in range(len(point_list)):
        point = point_list[i]
        x = point[0] + cube_pos[0]
        y = point[1] + cube_pos[1]
        point_list[i] = (x, y)

    # Draw the cube
    pygame.draw.polygon(screen, (255, 0, 0), (point_list[0], point_list[1], point_list[3], point_list[2]))
    pygame.draw.polygon(screen, (0, 255, 0), (point_list[4], point_list[5], point_list[7], point_list[6]))
    pygame.draw.polygon(screen, (0, 0, 255), (point_list[0], point_list[1], point_list[5], point_list[4]))

    pygame.draw.polygon(screen, (255, 255, 0), (point_list[2], point_list[3], point_list[7], point_list[6]))
    pygame.draw.polygon(screen, (255, 0, 255), (point_list[1], point_list[3], point_list[7], point_list[5]))
    pygame.draw.polygon(screen, (0, 255, 255), (point_list[0], point_list[2], point_list[6], point_list[4]))

    # Draw an outline around the screen if it's focused 
    if pygame.mouse.get_focused():
        pygame.draw.rect(screen, C_WHITE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 1)

    if pygame.mouse.get_focused():
        pygame.display.set_caption('Loading...')
    else:
        pygame.display.set_caption('Tangerine')

    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()