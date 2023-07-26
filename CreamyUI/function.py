import pygame, os

def LoadTexture(path:str) -> pygame.Surface:
    img = pygame.image.load(path).convert_alpha()
    return img

fontmap = {
    c[:c.rfind(".")].lower():c for c in os.listdir("C:\\Windows\\Fonts")
}

def font(name:str, size:int) -> pygame.font.Font:

    name = name.lower()

    if name not in fontmap: return pygame.font.Font(f"C:\\Windows\\Fonts\\Arial.ttf", size)
    return pygame.font.Font(f"C:\\Windows\\Fonts\\{fontmap[name]}", size)

def DrawText(text, font, window, pos, cenleft="center", color=(0,0,0)):
    x, y = pos
    text_obj = font.render(text, True, color)
    text_rect=text_obj.get_rect()
    if(cenleft == "center"):
        text_rect.centerx = x
        text_rect.centery = y
    elif(cenleft == "left"):
        text_rect.left=x
        text_rect.top=y
    elif(cenleft == "right"):
        text_rect.right=x
        text_rect.top=y
    elif(cenleft == "cenleft"):
        text_rect.left=x
        text_rect.centery=y
    elif(cenleft == "cenright"):
        text_rect.right=x
        text_rect.centery=y
    window.blit(text_obj, text_rect)

def GetSize(text,font):
    return font.render(text,True,(0,0,0)).get_rect().size