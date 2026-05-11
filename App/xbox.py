import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("Controle conectado:", joystick.get_name())
else:
    print("Nenhum controle encontrado")
