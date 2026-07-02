import pygame
import logging
import os

from functions import *


class Point:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), 3)
        logging.debug("point draw!")


class Polygon:
    def __init__(self, screen, x, y, scale, angle):
        self.screen = screen
        self.x = x
        self.y = y
        self.scale = scale
        self.angle = angle
        self.points = []
        self.triangles = []
        self.center_point = Point(self.screen, self.x, self.y)
        points_pos = generate_polygon_points(self.angle, self.scale, self.x, self.y)
        for i in points_pos:
            self.points.append(Point(self.screen, i[0], i[1]))
        for i in range(len(points_pos)):
            self.triangles.append(Triangle(screen, self.points[i-1], self.points[i], self.center_point))

    def draw(self):
        draw_all(self.triangles)

    def collide(self, x, y):
        for i in self.triangles:
            if point_in_triangle((x, y), i):
                i.color_background = [128, 128, 128]
            else:
                i.color_background = [255, 255, 255]

    def click(self, x, y, pressed_key, old_pressed_key):
        for i in self.triangles:
            if point_in_triangle((x, y), i) and \
                    ("Key.ctrl_l" in old_pressed_key and "Key.shift" in old_pressed_key and
                     "Key.alt_l" in old_pressed_key and len(old_pressed_key) == 3) and \
                    pressed_key == []:
                print(f"{i.file_name}.py запущен")
                os.system(f"python scripts/{i.file_name}.py")


class Triangle:
    def __init__(self, screen, point1, point2, point3):
        self.color_background = [255, 255, 255]
        self.text = None
        self.file_name = None
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.screen = screen
        self.lines = [Line(self.screen, point1.x, point2.x, point1.y, point2.y),
                      Line(self.screen, point2.x, point3.x, point2.y, point3.y),
                      Line(self.screen, point1.x, point3.x, point1.y, point3.y)]

    def draw(self):
        font = pygame.font.Font(None, 20)
        text_width, text_height = font.size(self.file_name)
        self.text = Text(self.screen, self.file_name, (self.point1.x + self.point2.x + self.point3.x)/3-text_width/2,
                         (self.point1.y + self.point2.y + self.point3.y) / 3)
        pygame.draw.polygon(self.screen, self.color_background, ([self.point1.x, self.point1.y],
                                                     [self.point2.x, self.point2.y],
                                                     [self.point3.x, self.point3.y]), 0)
        draw_all(self.lines)
        self.text.draw()


class Line:
    def __init__(self, screen, x1, x2, y1, y2):
        self.screen = screen
        self.pos1 = [x1, y1]
        self.pos2 = [x2, y2]

    def draw(self):
        pygame.draw.line(self.screen, [0, 0, 0], self.pos1, self.pos2, 5)


class Text:
    def __init__(self, screen, text, x, y, font_size=32, color=(0, 0, 0)):
        self.screen = screen
        self.text = text
        self.font_size = font_size
        self.color = color
        self.x = x
        self.y = y
        self.font_name = None
        self.font = pygame.font.Font(None, self.font_size)
        self.rendered_text = []
        self.texts = self.text.split("/")
        for i in self.texts:
            self.rendered_text.append(self.font.render(i, True, self.color))

    def draw(self):
        current_y = self.y
        for i in self.rendered_text:
            self.screen.blit(i, (self.x, current_y))
            current_y += self.font_size/1.5

    def set_text(self, text):
        self.text = text
        self.rendered_text = []
        self.texts = self.text.split("/")
        for i in self.texts:
            self.rendered_text.append(self.font.render(i, True, self.color))


class Button:
    def __init__(self, screen, rect, color):
        self.x = rect[0]
        self.y = rect[1]
        self.scaleX = rect[2]
        self.scaleY = rect[3]
        self.screen = screen
        self.color = color
        self.rect = rect

    def is_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousepos = pygame.mouse.get_pos()
                if self.x < mousepos[0] < self.scaleX+self.x:
                    if self.y < mousepos[1] < self.scaleY+self.y:
                        return True
        return False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

