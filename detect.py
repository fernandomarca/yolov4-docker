import json
import os
import sys
import time
import cv2
import matplotlib.pyplot as plt


def show(caminho):
    imagem = cv2.imread(caminho)
    fig = plt.gcf()
    fig.set_size_inches(18, 10)
    plt.axis('off')
    plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
    plt.show()


def detect(obj_file, cfg_file, weights_file, image_name, thresh=0.9):
    if not (obj_file and obj_file.strip()):
        os.system(
            "cd darknet && ./darknet detect {} {} {} -thresh {} -ext_output -out result.json".format(cfg_file, weights_file, image_name, thresh))
        # show('predictions.jpg')
    else:
        os.system(
            "cd darknet && ./darknet detector test {} {} {} {} -thresh {} -ext_output -ext_output -out result.json".format(obj_file, cfg_file, weights_file, image_name, thresh))
        # show('predictions.jpg')


if __name__ == "__main__":
    with open('config.json') as f:
        data = json.load(f)
    weights_file = data['weights_file']
    cfg_file = data['cfg_file']
    obj_file = data['obj_file']
    data_directory = data['data_directory']

    image_name = sys.argv[1]
    image_path = "{}/{}".format(data_directory, image_name)
    detect(obj_file, cfg_file, weights_file, image_path)
    os.system(
        "cp darknet/predictions.jpg results/{}-{}".format(time.time(), image_name))
    image_name_split = image_name.split(".")
    os.system(
        "cp darknet/result.json results/{}-{}.json".format(
            time.time(), image_name_split[0])
    )


# diretorio_fotos = 'fotos_teste'
# caminhos = [os.path.join(diretorio_fotos, f) for f in os.listdir(diretorio_fotos)]
# print(caminhos)
# for caminho_imagem in caminhos:
#   try:
#     imagem = cv2.imread(caminho_imagem)
#     (H, W) = imagem.shape[:2]
#   except:
#     print('Erro ao carregar a imagem -> ' + caminho_imagem)
#     continue
