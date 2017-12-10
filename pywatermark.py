# -*- coding:utf-8 -*-
import math
from config.settings import Settings
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class Watermark(object):
    def __init__(self, font_size=80, radius=3, ):
        self.font_size = font_size
        self.radius = radius
        pass

    def watermark_with_text(self, filename, text, color):
        image = Image.open(filename).convert('RGBA')
        image_watermark = Image.new('RGBA', image.size, (255, 255, 255, 0))

        draw = ImageDraw.Draw(image_watermark)

        width, height = image.size
        margin = 10
        font = ImageFont.truetype(Settings.FONT_PATH, self.font_size)
        text_width, text_height = draw.textsize(text, font)
        # Middle of the picture
        x = (width / 2) - (text_width / 2)
        y = (height / 2) - (text_height / 2)

        draw.text((x, y), text, color, font)
        # Calculating inclination angle
        dip_angle = math.degrees(math.asin(float(height - margin) / text_width))
        image_watermark = image_watermark.filter(ImageFilter.GaussianBlur(radius=self.radius)).rotate(dip_angle)
        Image.alpha_composite(image, image_watermark).show()
        # Image.alpha_composite(image, image_watermark).save('1-mark.png')

    pass


if __name__ == '__main__':
    water_mark = Watermark(60, 2)
    water_mark.watermark_with_text('resource/test.png', 'www.zhangaoo.com', 'gray')
