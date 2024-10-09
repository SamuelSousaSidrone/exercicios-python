import pygame

# Inicializa o Pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("lofi.mp3")

# Toca o áudio
pygame.mixer.music.play()

# Mantém o programa em execução enquanto o áudio toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)