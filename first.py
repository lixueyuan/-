import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter

#创建一个图像
img = Image.new("RGB",(150,50),(255,255,255))

#1创建画笔
draw = ImageDraw.Draw(img)

#2绘制线条和点
for i in range(random.randint(1,10)):
    draw.line(
        [
            (random.randint(1,150),random.randint(1,150)),
            (random.randint(1, 150), random.randint(1, 150))
        ],
        fill=(0,0,0)
    )

#3绘制点
for i in range(1000):
    draw.point(
        [
            random.randint(1,150),
            random.randint(1, 150)
        ],
        fill=(0,0,0)
    )

#4绘制文字
font_list = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
c_chars = "".join(random.sample(font_list,5))
font = ImageFont.truetype("simsun.ttc",28)
draw.text((5,5),c_chars,font=font,fill="red")

#5定义扭曲
#6使用滤镜
img.show()