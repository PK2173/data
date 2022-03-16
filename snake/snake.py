# from curses import KEY_DOWN
# import pygame
# from pygame.locals import *

# def draw_block():
#     surface.fill((52, 235, 152))#difind colo rgb color picker
#     surface.blit(block,(block_x,block_y))#adderass of block
#     pygame.display.flip()
# if __name__=="__main__":
#     pygame.init()
#     surface=pygame.display.set_mode((1000,500))#difaind a srceen size
#     surface.fill((52, 235, 152))#difind colo rgb color picker
#     block=pygame.image.load('/home/praveen/Desktop/New/block.jpg').convert()#adderass of block link
#     block_x=100
#     block_y=100
#     surface.blit(block,(block_x,block_y))#adderass of block
#     pygame.display.flip()
#     runing=True
#     while runing:
#         for event in  pygame.event.get():
#             if event.type==KEYDOWN:

#                 if event.type==K_ESCAPE:
#                     runing==False

#                 if event.key==K_UP:
#                     block_y=block_y-10
#                     draw_block()

#                 if event.key==K_DOWN:
#                     block_y=block_y+10
#                     draw_block()

#                 if event.key==K_LEFT:
#                     block_x=block_x-10
#                     draw_block()

#                 if event.key==K_RIGHT:
#                     block_x=block_x+10
#                     draw_block()

#             elif event.type==QUIT:
#                 runing=False

