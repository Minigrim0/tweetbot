import pygame
import pygame.camera
import sys
from settings import homedir, appdir, CAMERA_RES

pygame.camera.init()
cam = pygame.camera.Camera(sys.argv[1], CAMERA_RES)
cam.start()
img = cam.get_image()
pygame.image.save(img, "{}{}pic.jpg".format(homedir, appdir))
