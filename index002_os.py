"""
Lien : https://www.youtube.com/watch?v=Zx3J6lzfbOI
Tutoriel Python - opérations systèmes

Module os

Date : 26-01-2024
"""

import os

# try:
    # # Récupération du répertoire courant
    # print(os.getcwd())
    
    # # Changement du répertoire de travail
    # os.chdir("C:/Users/LRCOM")
    # print(os.getcwd())
    
    # # Liste d'un contenu d'un répertoire
    # print(os.listdir())
    
    # # Récupération de tout le contenu d'un répertoire
    # for (path, directories, files) in os.walk('.'):
    #     print(directories)
    
    # # Création d'un répertoire
    # os.mkdir('test')
    
    # # Création d'une hiérarchie de répertoires
    # os.makedirs('test/prog/projets/lua')
    
    # # Renommage d'un repertoire
    # os.mkdir('test')
    # os.rename('test', 'nouveau')
    
    # Suppression d'une arborescence complète :
    # os.makedirs('test/prog/projets/lua')
    # os.removedirs('test/prog/projets/lua')

# except OSError as e:
#     print(e)

# # Vérification si un fichier existe
# print(os.path.exists('test.txt'))
# print(os.path.exists('readme.md'))

# # Jointure d'un répertoire et d'un fichier mais qui n'est pas créé
# base = 'C:\\Users\\LRCOM\\pythonProjects\\jason_sys_os'
# filename = 'test.txt'
# complete_path = os.path.join(base, filename)
# print(complete_path)

# # Séparer un fichier dans un répertoire mais qui n'est pas réellement créé
# p = 'C:\\Users\\LRCOM\\pythonProjects\\jason_sys_os\\test.png'
# print(os.path.split(p))
# print(os.path.split(p)[1])

# # Comparaison entre deux chemins
# good_path = "C:\\Users\\LRCOM\\pythonProjects\\jason_sys_os\\"
# user_input_path = "C:\\Users\\LRCOM\\pythonProjects\\jason_sys_os\\"
# print(os.path.samefile(good_path, user_input_path))

# # Vérifier si le nom sélectionné est un répertoire
# os.mkdir('test') # création préalable du répertoire
# print(os.path.isdir('test'))

# # Vérifier si le nom sélectionné est un fichier
# print(os.path.isfile('test'))

# # Statistiques sur le fichier
# file_stats = os.stat('readme.md')
# print(file_stats) # obtention de toutes les données du fichier
# print(f"Taille du fichier : {file_stats.st_size}")
# print(f"Date de dernier accès : {file_stats.st_atime}")

# # Pour la version python 3.12 minimum
# print(f"Date de création du fichier : {file_stats.st_birthtime}")
