import os, pygame
def path_to_file(name_file):
    path_to_file = __file__
    path_to_file = path_to_file.split('\\')
    del path_to_file[-1]
    del path_to_file[-1]
    path_to_file_n = "\\".join(path_to_file)
    path_to_file_n = os.path.join(path_to_file_n, name_file)
    try:
        if str(name_file[-3]) == "p":
            a=pygame.image.load(name_file)
        else:
            a=pygame.font.Font(name_file, 10)
    except:
        path_to_file_n = "/".join(path_to_file)
        name_file = name_file.split("\\")
        name_file = "/".join(name_file)
        path_to_file_n = os.path.join(path_to_file_n, name_file)
    return path_to_file_n 
