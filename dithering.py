from PIL import Image

img = Image.open('butterfly.png')
pixel = img.load()
width = img.size[0]
height = img.size[1]


def code(old_pixel):
    color = old_pixel[:-1]
    for y in range(0,height-1):
        for x in range(0,width-1):
            old_pixel = pixel[x, y]
            closest_color = round(old_pixel / 256)
            new_pixel = closest_color
            pixel[x, y] = new_pixel
            quant_error = old_pixel - new_pixel
            pixel[x + 1][y] = pixel[x + 1][y] + quant_error * 7 / 16
            pixel[x - 1][y + 1] = pixel[x - 1][y + 1] + quant_error * 3 / 16
            pixel[x][y + 1] = pixel[x][y + 1] + quant_error * 5 / 16
            pixel[x + 1][y + 1] = pixel[x + 1][y + 1] + quant_error * 1 / 16
            return new_pixel
    def closest_color(old_pixel):
        color = old_pixel[:-1]
        pixel[x, y] = new_pixel
        old_blue = pixel[y, x, 0]
        old_green = pixel[y, x, 1]
        old_red = pixel[y, x, 2]

        c = 1

        new_blue = round(c * old_blue / 255.0) * (255 / c)
        new_green = round(c * old_green / 255.0) * (255 / c)
        new_red = round(c * old_red / 255.0) * (255 / c)

        pixel[y, x, 0] = new_blue
        pixel[y, x, 1] = new_green
        pixel[y, x, 2] = new_red

        old_blue = new_blue
        old_green = new_green
        old_red = new_red

        return img

img.show()
img.save('butterfly2.png')