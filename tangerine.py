#@author: @aurimukstis1 / github: https://github.com/Aurimukstis1
#> GNU General Public License v3.0

# Importing needed libraries
import pygame
import math
import sys
import threading

# Screen width in px
screen_width = 360

# Screen height in px
screen_height = 480

# The higher this number, the faster the cube will rotate
rotation_speed_coefficient = 0.2

# The higher this number, the bigger the cube will be
cube_size_coefficient = 1

# Set up the cube
cube_size = 100
cube_pos = [screen_width/2, screen_height/2]
cube_angles = [0, 0, 0] # X, Y, Z angles

loading = 0


class MainLoop:
    def __init__(self):
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run)
            self.thread.start()
    
    def run(self):
        # Initialize Pygame
        pygame.init()

        screen = pygame.display.set_mode([screen_width, screen_height], pygame.NOFRAME)
        pygame.display.set_caption('Loading...')

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

            # Update the cube angles
            cube_angles[0] += 1*rotation_speed_coefficient # Rotate the cube along the X axis
            cube_angles[1] += 1*rotation_speed_coefficient # ... Y axis
            cube_angles[2] += 2*rotation_speed_coefficient # ... Z axis

            screen.fill((20,20,20))

            # -- loading bar code
            # Add the `#` characters to the loading bar string
            loading_bar = ''
            for i in range(round(loading)):
                loading_bar += '#'

            # Add spaces to fill the rest of the loading bar
            for i in range(round(loading), 10):
                loading_bar += ' '

            # Draw text on the screen below the cube, centered
            font = pygame.font.SysFont('cambriamath', 20)
            text = font.render('Tangerine', True, (255,255,255))
            text_rect = text.get_rect()
            text_rect.center = (screen_width/2, screen_height - 100)

            # Draw the loading bar text on the screen below the cube, centered
            loading_text = font.render(loading_bar, True, (255,255,255))
            loading_text_rect = loading_text.get_rect()
            loading_text_rect.center = (screen_width/2, screen_height - 80)

            # Draw text on the screen below the cube, centered
            copyright_text = font.render('github.com/Aurimukstis1', True, (30,30,30))
            copyright_text_rect = copyright_text.get_rect()
            copyright_text_rect.center = (screen_width/2, screen_height - 40)

            if pygame.mouse.get_focused():
                screen.blit(text, text_rect)
                screen.blit(loading_text, loading_text_rect)
                screen.blit(copyright_text, copyright_text_rect)

            # Calculate the coordinates of each point on the cube
            point_list = []
            for x in (-1, 1):
                for y in (-1, 1):
                    for z in (-1, 1):
                        point_list.append((x*cube_size/2, y*cube_size/2, z*cube_size/2))

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
                pygame.draw.rect(screen, (255,255,255), (0, 0, screen_width, screen_height), 1)

            if pygame.mouse.get_focused():
                pygame.display.set_caption('Loading...')
            else:
                pygame.display.set_caption('Tangerine')

            # Update the display
            pygame.display.flip()
        
    def stop(self):
        if self.running:
            self.running = False
            self.thread.join()

tangerinemain = MainLoop()

