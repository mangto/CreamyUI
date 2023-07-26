import pygame, sys
from pygame import gfxdraw
from CreamyUI.function import *

pygame.init()
clock = pygame.time.Clock()

class system:
    TargetFps :int = 120
    fps = 0.1**30

    def SetFPS(fps:int) -> None:
        system.TargetFps = fps

    def GetFPS() -> int:
        return max(system.fps, 0.1**30)

    def update():
        pygame.display.update()

    def DefualtEvent() -> list:
        events = pygame.event.get()

        for event in events:

            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

        return events
        

def InitWindow(size:tuple[int, int], title:str="Creamy Window", icon:pygame.Surface=None) -> pygame.Surface:
    window = pygame.display.set_mode(size)
    icon = icon if icon else LoadTexture(".\\CreamyUI\\tex\\CREAM.png")
    pygame.display.set_caption(title)
    pygame.display.set_icon(icon)

    return window