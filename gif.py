import sys
import time
from PIL import Image
import numpy as np
import st7735

if len(sys.argv) > 1:
    image_file = sys.argv[1]
else:
    print(f"Usage: {sys.argv[0]} <filename.gif>")
    sys.exit(0)

# Function to convert RGB to BGR
def rgb_to_bgr(image):
    image_np = np.array(image)
    if image_np.shape[-1] == 3:
        bgr_array = image_np[..., ::-1]  # Swap R and B
        return Image.fromarray(bgr_array, 'RGB')
    return image

# Create TFT LCD display class.
disp = st7735.ST7735(
    port=0,
    cs=st7735.BG_SPI_CS_BACK,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT (CE0 or CE1 on board)
    dc="GPIO24",               # DC/A0 pin Connected to GPIO24
    backlight="GPIO22",
    rst = "GPIO25",            # RST pin Connected to GPIO25
    invert = False,
    rotation=90,
    spi_speed_hz=4000000
)

# Initialize display
disp.begin()

width = disp.width
height = disp.height

# Load the gif image
print(f"Loading gif: {image_file}...")
image = Image.open(image_file)

print("Drawing gif, press Ctrl+C to exit!")

frame = 0

while True:
    try:
        image.seek(frame)

        # Convert frame to RGB
        rgb_image = image.convert("RGB")

        # Resize and swap RGB -> BGR
        resized = rgb_image.resize((width, height))
        corrected = rgb_to_bgr(resized)

        # Display the corrected frame
        disp.display(corrected)

        frame += 1
        time.sleep(0.05)  # Adjust to match gif speed
    except EOFError:
        frame = 0
    except KeyboardInterrupt:
        print("Exiting.")
        break
