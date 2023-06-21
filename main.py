import pygame
import modules.data_base as data
import modules.playing_field as m_field
import modules.path_file as path
import modules.ship as ship
import modules.place_player_ships as place
import modules.shoot as sh
import modules.bot as bot
import modules.music as music
import modules.win as win
import modules.button as button

pygame.init()

bot.place_bot_ships()
print("end place")
screen = pygame.display.set_mode((1000, 700))
data.unplaced_ship = ship.Ship("four_decker", "player", [0,0,0], None, 0)

pygame.display.set_caption("Морський бій")
pygame.display.set_icon(pygame.image.load(path.path_to_file("images\\another\\icon.png")))

# button_reset = button.Button(x = 700, y = 20, text = "RESET")
# button_ok = button.Button(x = 700, y = 100, text = "OK")
# button_done = button.Button(x = 400, y = 317, tex = "DONE")

FPS = 60
step = "player"
clock = pygame.time.Clock()
# data.ship_list.append(ship.Ship("four_decker", "player", [0,0], "Calm", 0))
t=0
repeat = 0
main = True
mouse_press = False
mouse = False
winner = None
while main:
    if winner == None:
        music.play_music(place.ship_num < 10)
        m_field.all_fields(screen, t, repeat)
    mouse_press = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            main = False 
        if winner == None:
            if   pygame.key.get_pressed()[pygame.K_MINUS]==1 and t==0: t=1
            elif pygame.key.get_pressed()[pygame.K_MINUS]==1 and t==1: t=0
            if event.type == pygame.MOUSEBUTTONDOWN: 
                place.choose_ship()
                mouse_press = True
            elif event.type == pygame.MOUSEBUTTONUP: 
                if place.ship_num < 10: place.place_ship()
                mouse_press = "Up"
            # print(f"Mouse Button Down: {event.type==pygame.MOUSEBUTTONDOWN}; \nMouse Button Up: {event.type==pygame.MOUSEBUTTONUP}")
            place.rotate_ship()
            place.move_ship()
    if winner == None:
        if place.ship_num >= 10:
            win.scan_ship_cells()
        winner = win.scan_victory(repeat)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    if winner != None:
        win.win_screen(winner, screen)
    # sh.hover_and_shoot(mouse_press)
    clock.tick(FPS)
    if winner == None:
        if place.ship_num >= 10:
            if step == "player" and sh.hover_and_shoot(mouse_press):
                step = "enemy"
            elif step == "enemy" and bot.bot_shoot(repeat):
                step = "player"
    
        # ship.place_ship()
    
    pygame.display.flip()
    repeat += 1