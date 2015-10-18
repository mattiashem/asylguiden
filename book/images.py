#!/usr/bin/env python
try:
	    from PIL import Image, ImageOps
except ImportError:
	    import Image
	    import ImageOps


image = Image.open('snake.jpg')

# ImageOps compatible mode
if image.mode not in ("L", "RGB"):
    image = image.convert("RGB")


imageresize = image.resize((200,200), Image.ANTIALIAS)
imageresize.save('resize_200_200_aa.jpg', 'JPEG', quality=75)

image.thumbnail((200,200), Image.ANTIALIAS)
image.save('thumbnail_200_200_aa.jpg', 'JPEG', quality=75)

imagefit = ImageOps.fit(image, (200, 200), Image.ANTIALIAS)
imagefit.save('fit_200_200_aa.jpg', 'JPEG', quality=75)