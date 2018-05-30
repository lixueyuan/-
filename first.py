import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageGrab
import urllib

# Creat image
img = Image.new("RGB",(150,50),(255,255,255))

#1 Creact brush
draw = ImageDraw.Draw(img)

#2 Draw lines
for i in range(random.randint(1,10)):
    draw.line(
        [
            (random.randint(1,150),random.randint(1,150)),
            (random.randint(1, 150), random.randint(1, 150))
        ],
        fill=(0,0,0)
    )

#3 Draw points
for i in range(1000):
    draw.point(
        [
            random.randint(1,150),
            random.randint(1, 150)
        ],
        fill=(0,0,0)
    )

#4 Draw text
font_list = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
c_chars = "".join(random.sample(font_list,5))
font = ImageFont.truetype("simsun.ttc",38)
draw.text((5,5),c_chars,font=font,fill="black")
'''
First param:Represents the position of the text
Second param:Represents contents of the text
Third param: Is font
Forth param:Font color
'''

#5 Custom param of the warp
params = [
    1 - float(random.randint(1,2))/100,
    0,
    0,
    0,
    1 - float(random.randint(1,2))/100,
    float(random.randint(1,2))/500,
    0.001,
    float(random.randint(1,1))/500
]
img = img.transform((150,50),Image.PERSPECTIVE,params)
'''
first: arround of the warp
second: style of the warp
third: params of the  warp
'''
#6 Filter
ima = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

img.show()
img.save('123.jpg')