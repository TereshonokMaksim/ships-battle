import pygame, modules.data_base as data, modules.path_file as path, modules.effects as effect

def hover_and_shoot(click):
    return_data = False
    # Блок главного условия и создания главных переменных
    cursor = pygame.SYSTEM_CURSOR_ARROW
    if (0 < pygame.mouse.get_pos()[0] - 650 < 320 and
        0 < pygame.mouse.get_pos()[1] - 300 < 320):
        cell = [(pygame.mouse.get_pos()[1] - 300) // 32, (pygame.mouse.get_pos()[0] - 650) // 32]
        # print(cell)
        enemy_cell = data.enemy_map[cell[0]][cell[1]]
        # print(enemy_cell)
        # Блок сканирования наведения/клика/отжимания
        if click == False:
            # print("hovering")
            if enemy_cell == 1:                       data.enemy_map[cell[0]][cell[1]] = 6;  cursor = pygame.SYSTEM_CURSOR_HAND
            elif enemy_cell == 0 or enemy_cell == 2:  data.enemy_map[cell[0]][cell[1]] = 5;  cursor = pygame.SYSTEM_CURSOR_HAND
            elif enemy_cell == 5 or enemy_cell == 6:                cursor = pygame.SYSTEM_CURSOR_HAND
            elif enemy_cell == 3 or enemy_cell == 4:                cursor = pygame.SYSTEM_CURSOR_NO
        elif click == True:
            print("click")
            # print("cell",enemy_cell)
            if enemy_cell == 5:    data.enemy_map[cell[0]][cell[1]] = 7;  cursor = pygame.SYSTEM_CURSOR_HAND; print(2)
            elif enemy_cell == 6:  data.enemy_map[cell[0]][cell[1]] = 8;  cursor = pygame.SYSTEM_CURSOR_HAND; print(1)
            elif enemy_cell == 7 or enemy_cell == 8: cursor = pygame.SYSTEM_CURSOR_HAND; print(3)
            else:                      cursor = pygame.SYSTEM_CURSOR_NO; print("that's else?")
            print("cell",enemy_cell)
        elif click == "Up":
            print("up")
            if enemy_cell == 8:   data.enemy_map[cell[0]][cell[1]] = 3;   print(f"cell chaged to expl, {cell}"); data.effect_list.append(effect.Effect("explosion", (cell[1] * 32 + 650, cell[0] * 32 + 300)))
            elif enemy_cell == 7:   data.enemy_map[cell[0]][cell[1]] = 4; print(f"cell chaged to miss, {cell}"); data.effect_list.append(effect.Effect("miss", (cell[1] * 32 + 650, cell[0] * 32 + 300))); return_data = True
            else: print("error 1"); cursor = pygame.SYSTEM_CURSOR_NO
        # Блок управления курсором мыши
        # print(cursor)
    pygame.mouse.set_cursor(cursor)
    return return_data