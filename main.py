import pygame
import math

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

WIDTH = 1920
HEIGHT = 1080

x_init, y_init = 0, 0

x_separator = 10
y_separator = 20

rows = HEIGHT // y_separator
columns = WIDTH // x_separator

screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0

theta_spacing = 10
phi_spacing = 1

chars = '.,-~:;=!*#$@'

screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 18, bold = True)

def text_display(char, x_init, y_init):

    text = font.render(str(char), True, white)
    display_surface.blit(text, (x_init, y_init))

run = True
while run:

    screen.fill(black)

    z = [0] * screen_size
    b = [' '] * screen_size

    for j in range(0, 628, theta_spacing):
        for i in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_init == rows * y_separator - y_separator:
        y_init = 0

    for i in range(len(b)):
        A += 0.000002
        B += 0.000001
        if i == 0 or i % columns:
            text_display(b[i], x_init, y_init)
            x_init += x_separator
        else:
            y_init += y_separator
            x_init = 0
            text_display(b[i], x_init, y_init)
            x_init += x_separator

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False