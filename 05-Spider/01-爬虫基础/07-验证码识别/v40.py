import pytesseract as pt
from PIL import Images

# 生成图片实例
image = Image.open("1.jpg")

# 代用pytesseract,把图片转换成文字
# 返回结果是转换后的结果

text = pt.image_to_string(image, lang="chi_sim")
print(text)

print(image)
print(type(image))
