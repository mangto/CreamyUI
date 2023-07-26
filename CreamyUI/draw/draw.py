from math import atan2, cos, degrees, radians, sin
import pygame

def Move(rotation, steps, position):
    """Return coordinate position of an amount of steps in a direction."""
    xPosition = cos(radians(rotation)) * steps + position[0]
    yPosition = sin(radians(rotation)) * steps + position[1]
    return (xPosition, yPosition)

def aaline(surface, color, point1, point2, thickness):
    angle = degrees(atan2(point1[1] - point2[1], point1[0] - point2[0]))

    vertices = list()
    vertices.append(Move(angle-90, thickness, point1))
    vertices.append(Move(angle+90, thickness, point1))
    vertices.append(Move(angle+90, thickness, point2))
    vertices.append(Move(angle-90, thickness, point2))

    pygame.gfxdraw.aapolygon(surface, vertices, color)
    pygame.gfxdraw.filled_polygon(surface, vertices, color)