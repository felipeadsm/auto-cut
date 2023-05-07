import cv2


class CutImage:
    def __init__(self):
        self.frame = None
        self.out_frame = None

    def open_images(self, group_number, img_number):
        self.frame = cv2.imread(f'G{group_number}/Imagem{img_number}.jpg')

    def image_cut(self):
        self.out_frame = self.frame[37:691, 317:1338]

    def save_image(self, group_number, img_number):
        cv2.imwrite(f'G{group_number}/imagem_cortada{img_number}.jpg', self.out_frame)


def main():
    cut_object = CutImage()

    list_count_images = []

    cut_object.open_images(1, 1)
    cut_object.image_cut()
    cut_object.save_image(1, 1)


if __name__ == "__main__":
    main()
