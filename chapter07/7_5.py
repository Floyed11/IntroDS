import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image

# 加载彩色图像
image = Image.open('/Users/linto/Documents/IntroDaSE/Homework/IntroDS/chapter07/color_image.jpg')

# 转换为灰度图像
transform = transforms.Grayscale()
grayscale = transform(image)
grayscale.save('gray_scale.jpg')

# 转换为任意大小的图像
transform = transforms.Compose([
    transforms.Resize((1000, 1000)),
    transforms.ToTensor()
])
resized_image = transform(image)
# 将张量转换回PIL图像
to_pil = transforms.ToPILImage()
pil_image = to_pil(resized_image)

# 保存图像
pil_image.save('resized_image.jpg')