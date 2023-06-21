import pygame, modules.path_file as path
pygame.mixer.init()
pygame.init()
music_num = 0
music = pygame.mixer.Sound(path.path_to_file("sounds\\place_ships_theme.mp3"))
music_place = True
def play_music(ships_placed):
    global music_place, music, music_num
    if ships_placed:
        if music_place or pygame.mixer.Sound.get_num_channels(music) < 1:
            pygame.mixer.Sound.fadeout(music, 100)
            music = pygame.mixer.Sound(path.path_to_file(f"sounds\\battle_theme_{music_num + 1}.mp3"))
            pygame.mixer.Sound.set_volume(music, 0.4)
            pygame.mixer.Sound.play(music)
            music_num += 1
            music_place = False
            if music_num > 2:
                music_num = 0