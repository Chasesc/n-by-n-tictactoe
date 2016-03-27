#! python2.7

import pygame
pygame.init()

import pygame._view # This is needed for py2exe to work with pygame.

from game import Game

def main():    
    Game(True).run()

if __name__ == "__main__":
    main()