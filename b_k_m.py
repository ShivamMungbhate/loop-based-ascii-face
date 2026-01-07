from PIL import Image

# ASCII characters (dark → light)
ASCII_CHARS = ["@", "#", "S", "%", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=50):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""

    for pixel in pixels:               # 🔁 LOOP
        if pixel < 50:                  # 🔀 CONDITION
            ascii_str += "@"
        elif pixel < 100:
            ascii_str += "#"
        elif pixel < 150:
            ascii_str += "S"
        elif pixel < 200:
            ascii_str += ":"
        else:
            ascii_str += "."

    return ascii_str

def image_to_ascii(path):
    try:
        image = Image.open(path)
    except:
        print("Image not found")
        return

    image = resize_image(image)
    image = grayify(image)

    ascii_data = pixels_to_ascii(image)

    img_width = image.width
    ascii_image = ""

    for i in range(0, len(ascii_data), img_width):   # 🔁 LOOP
        ascii_image += ascii_data[i:i+img_width] + "\n"

    return ascii_image


# 🔹 MAIN
ascii_art = image_to_ascii(r"c:\Users\shiva\Downloads\ban-ki-moon.jpg.optimal.jpg")

print(ascii_art)

# Save to file
with open("ascii_output.txt", "w") as f:
    f.write(ascii_art)