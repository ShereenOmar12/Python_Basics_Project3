
from PIL import Image

image = Image.open(r"C:\Users\user\Desktop\image\صور-برمجة1.jpg")
print(f"Original size : {image.size}") 

image_resized = image.resize((400, 400))
image_resized.save(r"C:\Users\user\Desktop\image\new_size.jpg")
