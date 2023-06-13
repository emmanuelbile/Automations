from PIL import Image

"""def merge_images(image1, image2):
    image1 = Image.open(image1).convert('RGBA')
    image2 = Image.open(image2).convert('RGBA')
    image1.paste(image2, (0, 0), image2)
    res = image1.convert('RGB')
    return res"""



def merge_images(image1, image2):
    image1 = Image.open(image1).convert('RGBA')
    image2 = Image.open(image2).convert('RGBA')
    new_image = Image.new('RGBA', (image1.width + image2.width, max(image1.height, image2.height)))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (image1.width, 0))
    result = new_image.convert('RGB')
    return result




"""def merge_images(image1, image2):
    image1 = Image.open(image1).convert('RGBA')
    image2 = Image.open(image2).convert('RGBA')
    new_image = Image.new('RGBA', (max(image1.width, image2.width), image1.height + image2.height))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (0, image1.height))
    result = new_image.convert('RGB')
    return result"""

result = merge_images('20230425160317096_0001.jpg', '20230425160307596_0001.jpg')

result.save(r"CNI.jpg")