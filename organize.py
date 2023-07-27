import os
import shutil

origem = "C:/Users/Usuario/Downloads"
destino = "C:/User/Usuario/OneDrive/Área de Trabalho/codigos/AULA-102"

lista = os.listdir(origem)
for fileName in lista:
    name, extencion = os.path.splitext(fileName)
    if extencion == "":
        continue
    if extencion in [".gif", ".png", ".jpg", "jpag", ".jfif"]:
        path1 = origem + "/" + fileName
        path2 = destino + "/" + "arquivos"
        path3 = destino + "/" + "arquivos" + "/" + fileName

        if os.path.exists(path2):
            print("Movendo " + fileName + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo " + fileName + "...")
            shutil.move(path1, path3)



