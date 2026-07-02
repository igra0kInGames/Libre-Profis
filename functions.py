import math
from pynput import keyboard
import sys
import pygame


def generate_polygon_points(n, radius=1.0, center_x=0, center_y=0, start_angle=0):
    points = []
    angle_step = 2 * math.pi / n

    for i in range(n):
        angle = start_angle + i * angle_step
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append([x, y])

    return points


def draw_all(l):
    for i in l:
        i.draw()


def point_in_triangle(point, triangle):
    x, y = point
    x1, y1 = triangle.point1.x, triangle.point1.y
    x2, y2 = triangle.point2.x, triangle.point2.y
    x3, y3 = triangle.point3.x, triangle.point3.y

    denominator = ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))

    if denominator == 0:
        return False

    alpha = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denominator
    beta = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denominator
    gamma = 1.0 - alpha - beta

    return alpha >= 0 and beta >= 0 and gamma >= 0


def make_window_transparent(color):
    """Делает указанный цвет прозрачным"""
    if sys.platform == "win32":
        import ctypes
        hwnd = pygame.display.get_wm_info()["window"]
        WS_EX_LAYERED = 0x00080000
        #WS_EX_TRANSPARENT = 0x00000020
        LWA_COLORKEY = 0x00000001
        GWL_EXSTYLE = -20

        ex_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        ctypes.windll.user32.SetWindowLongW(
            hwnd,
            GWL_EXSTYLE,
            ex_style | WS_EX_LAYERED
        )

        # Конвертируем RGB в формат COLORREF (0x00BBGGRR)
        color_ref = color[0] | (color[1] << 8) | (color[2] << 16)
        ctypes.windll.user32.SetLayeredWindowAttributes(
            hwnd,
            color_ref,
            0,
            LWA_COLORKEY
        )
        return True
    return False
