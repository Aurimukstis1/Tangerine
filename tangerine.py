#@author: @aurimukstis1 / github: https://github.com/Aurimukstis1
#> GNU General Public License v3.0

# Importing needed libraries
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import math
import threading


class MainLoop:
    def __init__(self):
        # Init without running
        self.running: bool = False
        # Start with no threads
        self.thread = None
        # Init loading starting point
        self.loading: float = 0.0

    def start(self,custom_screen_width,custom_screen_height,rot_speed_coef,custom_cube_size,custom_cube_size_coef):
        if not self.running:
            self.running = True

            self.screen_width = custom_screen_width
            self.screen_height = custom_screen_height
            self.rotation_speed_coefficient = rot_speed_coef
            self.cube_size = custom_cube_size
            self.cube_size_coefficient = custom_cube_size_coef

            self.cube_pos = [self.screen_width/2, self.screen_height/2]
            self.cube_angles = [0, 0, 0] # X, Y, Z angles

            self.thread = threading.Thread(target=self.run)
            self.thread.start()
        else:
            print("Loading applet already running...")
    
    def run(self):
        # Initialize Pygame
        pygame.init()

        screen = pygame.display.set_mode([self.screen_width, self.screen_height], pygame.NOFRAME)
        pygame.display.set_caption('Loading...')

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

            # Update the cube angles
            self.cube_angles[0] += 1*self.rotation_speed_coefficient # Rotate the cube along the X axis
            self.cube_angles[1] += 1*self.rotation_speed_coefficient # ... Y axis
            self.cube_angles[2] += 2*self.rotation_speed_coefficient # ... Z axis

            screen.fill((20,20,20)) # the matte color

            # -- loading bar code
            # Add the `#` characters to the loading bar string
            loading_bar = ''
            for i in range(round(self.loading)):
                loading_bar += '#'

            # Add spaces to fill the rest of the loading bar
            for i in range(round(self.loading), 10):
                loading_bar += ' '

            # Draw text on the screen below the cube, centered
            font = pygame.font.SysFont('cambriamath', 20)
            text = font.render('Tangerine', True, (200,200,200))
            text_rect = text.get_rect()
            text_rect.center = (self.screen_width/2, self.screen_height - 100)

            # Draw the loading bar text on the screen below the cube, centered
            loading_text = font.render(loading_bar, True, (255,255,255))
            loading_text_rect = loading_text.get_rect()
            loading_text_rect.center = (self.screen_width/2, self.screen_height - 80)

            if pygame.mouse.get_focused():
                screen.blit(text, text_rect)
                screen.blit(loading_text, loading_text_rect)

            # Calculate the coordinates of each point on the cube
            point_list = []
            for x in (-1, 1):
                for y in (-1, 1):
                    for z in (-1, 1):
                        point_list.append((x*self.cube_size/2, y*self.cube_size/2, z*self.cube_size/2))

            # Rotate the cube along the X axis
            for i in range(len(point_list)):
                point = point_list[i]
                x = point[0]
                y = point[1]*math.cos(math.radians(self.cube_angles[0])) - point[2]*math.sin(math.radians(self.cube_angles[0]))
                z = point[1]*math.sin(math.radians(self.cube_angles[0])) + point[2]*math.cos(math.radians(self.cube_angles[0]))
                point_list[i] = (x, y, z)

            # Rotate the cube along the Y axis
            for i in range(len(point_list)):
                point = point_list[i]
                x = point[0]*math.cos(math.radians(self.cube_angles[1])) + point[2]*math.sin(math.radians(self.cube_angles[1]))
                y = point[1]
                z = -point[0]*math.sin(math.radians(self.cube_angles[1])) + point[2]*math.cos(math.radians(self.cube_angles[1]))
                point_list[i] = (x, y, z)
            
            # Rotate the cube along the Z axis
            for i in range(len(point_list)):
                point = point_list[i]
                x = point[0]*math.cos(math.radians(self.cube_angles[2])) - point[1]*math.sin(math.radians(self.cube_angles[2]))
                y = point[0]*math.sin(math.radians(self.cube_angles[2])) + point[1]*math.cos(math.radians(self.cube_angles[2]))
                z = point[2]
                point_list[i] = (x, y, z)

            # Resize the cube
            for i in range(len(point_list)):
                point = point_list[i]
                x = point[0]*self.cube_size_coefficient
                y = point[1]*self.cube_size_coefficient
                z = point[2]*self.cube_size_coefficient
                point_list[i] = (x, y, z)
            
            # Draw the cube
            for i in range(len(point_list)):
                point = point_list[i]
                x = point[0] + self.cube_pos[0]
                y = point[1] + self.cube_pos[1]
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
                pygame.draw.rect(screen, (255,255,255), (0, 0,self.screen_width, self.screen_height), 1)

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

