import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from PIL import Image


class ImageViewer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.images = [
            file for file in os.listdir(folder_path) if file.endswith(".ppm")
        ]
        self.index = 0

        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)
        self.img_display = plt.imshow(self.load_image())

        self.btn_next = Button(plt.axes([0.7, 0.05, 0.2, 0.075]), "Next image")
        self.btn_next.on_clicked(self.next_image)

        self.btn_prev = Button(
            plt.axes([0.1, 0.05, 0.2, 0.075]), "Previous image"
        )
        self.btn_prev.on_clicked(self.prev_image)

    def load_image(self):
        image_path = os.path.join(self.folder_path, self.images[self.index])
        return Image.open(image_path)

    def next_image(self, event):
        self.index = (self.index + 1) % len(self.images)
        self.img_display.set_data(self.load_image())
        plt.draw()

    def prev_image(self, event):
        self.index = (self.index - 1) % len(self.images)
        self.img_display.set_data(self.load_image())
        plt.draw()


folder_path = r"\Users\jonax\DocumentsPC\Code\Projets\Australie\Intelligence artificielle\projets_ia\cs50\course5\traffic\gtsrb\2"
viewer = ImageViewer(folder_path)
plt.show()
