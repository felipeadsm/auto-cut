import cv2


class CutImage:
    def __init__(self):
        self.frame = None
        self.out_frame = None

    def open_images(self, folder, group_number, img_number):
        teste = f'{folder}/G{group_number}/Img{img_number}.jpg'
        self.frame = cv2.imread(f'{folder}/G{group_number}/Img{img_number}.jpg')

    def image_cut(self):
        self.out_frame = self.frame[37:691, 317:1338]

    def save_image(self, folder, group_number, img_number):
        teste = f'{folder}/G{group_number}/imagem_editada{img_number}.jpg'
        cv2.imwrite(f'{folder}/G{group_number}/imagem_editada_{img_number}.jpg', self.out_frame)


def main():
    cut_object = CutImage()

    count_images_exp = [4, 6, 5, 5, 5, 5, 9, 6]
    count_images_bolsa = [3, 3, 4, 2]

    pasta_experimento = 'Fotos_96_hs'
    pasta_bolsa = 'Bolsa_Neta_96_hs'

    # Experimento
    for i in range(8):
        for j in range(count_images_exp[i]):
            cut_object.open_images(pasta_experimento, i + 1, j + 1)
            cut_object.image_cut()
            cut_object.save_image(pasta_experimento, i + 1, j + 1)

    # Bolsa
    for i in range(4):
        for j in range(count_images_bolsa[i]):
            cut_object.open_images(pasta_bolsa, i + 3, j + 1)
            cut_object.image_cut()
            cut_object.save_image(pasta_bolsa, i + 3, j + 1)


if __name__ == "__main__":
    main()
