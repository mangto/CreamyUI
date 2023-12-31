import pygame, sys
from pygame import gfxdraw
from CreamyUI.function import *
from CreamyUI.loader import *
import win32gui
import win32con

def wndProc(oldWndProc, draw_callback, hWnd, message, wParam, lParam):
    if message == win32con.WM_SIZE:
        draw_callback()
        win32gui.RedrawWindow(hWnd, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)
    return win32gui.CallWindowProc(oldWndProc, hWnd, message, wParam, lParam)


pygame.init()
clock = pygame.time.Clock()

class system:
    TargetFps :int = 120
    fps = 120
    timer = 0
    reloaded = False

    def SetFPS(fps:int) -> None:
        system.TargetFps = fps

    def GetFPS() -> int:
        return system.fps if system.fps > 0 else system.TargetFps

    def update():
        system.fps = clock.get_fps()
        system.timer += 1/system.GetFPS()
        pygame.display.update()

    def DefualtEvent() -> list:
        events = pygame.event.get()

        for event in events:

            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

        return events
    
    def draw():
        window.fill(background)
        for object in objects:
            object.draw(
                window=window
            )
        
        system.update()
        clock.tick(system.TargetFps)
        

def InitWindow(size:tuple[int, int], title:str="Creamy Window", icon:pygame.Surface=None) -> pygame.Surface:
    window = pygame.display.set_mode(size, pygame.RESIZABLE| pygame.DOUBLEBUF)
    icon = icon if icon else LoadTexture(".\\CreamyUI\\tex\\CREAM.png")
    pygame.display.set_caption(title)
    pygame.display.set_icon(icon)

    return window

def unpack(settings):
    objects = settings.get("objects", [])
    background = settings.get("background", [0, 0, 0])
    reload = settings.get("reload", -1)
    caption = settings.get("caption", "Creamy Window")
    size = settings.get("size", [512, 512])
    connector = settings.get("connector", {})

    return objects, background, reload, caption, size, connector
    

def run(path:str=None):
    global window, objects, background, reload, caption, size, connector
    window = pygame.display.set_mode((1,1))

    settings = loader(path)
    objects, background, reload, caption, size, connector = unpack(settings)
    window = InitWindow(size, caption)

    oldWndProc = win32gui.SetWindowLong(win32gui.GetForegroundWindow(), win32con.GWL_WNDPROC, lambda *args: wndProc(oldWndProc, system.draw, *args))

    while True:
        events = system.DefualtEvent()
        system.draw()


        # reloader for designer

        if (path and reload > 0 and system.timer % reload < 1):
            if (system.reloaded == False):
                try:
                    settings = loader(path)
                    objects, background, reload, caption, size, connector = unpack(settings)
                    system.reloaded = True
                except:
                    pass

        else: system.reloaded = False