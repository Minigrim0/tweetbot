import pygame
import pygame.camera
import sys
import os.path

homedir = os.path.expanduser("~")

pygame.camera.init()
cam = pygame.camera.Camera(sys.argv[1], (720, 720))
cam.start()
img = cam.get_image()
pygame.image.save(img, homedir + "/Documents/tweetbot/pic.jpg")
