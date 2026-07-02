import pygame_gui

from classes import *

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
texts = []
input_path_manager = pygame_gui.UIManager(size)

stages = ["input_path_file", '']
stage_number = 0
stage = stages[stage_number]
input_path_text = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((330, 6), (350, 32)),
    manager=input_path_manager
)
input_path_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((690, 5), (48, 32)),
    text='Далее',
    manager=input_path_manager
)

running = True
while running:
    time_delta = clock.tick(60) / 1000.0
    print(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if stage == "input_path_file":
                if event.ui_element == input_path_button:
                    stage_number += 1
                    stage = stages[stage_number]
        input_path_manager.process_events(event)
    screen.fill((255, 255, 255))
    if stage == "input_path_file":
        Text(screen, "Введите путь к файлу excel:", 10, 10, fontSize=32).draw()
        input_path_manager.update(time_delta)
        input_path_manager.draw_ui(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
