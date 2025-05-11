import numpy as np
from PIL import Image
import st7735
import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <image_file>")
    sys.exit(1)

image_file = sys.argv[1]

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

WIDTH = disp.width
HEIGHT = disp.height

disp.begin()

# Load image and convert to RGB
image = Image.open(image_file).convert("RGB")
image = image.resize((WIDTH, HEIGHT))

# Convert to NumPy array and BGR format
rgb_array = np.array(image)
bgr_array = rgb_array[..., ::-1]  # Swap R and B

# Convert back to Image
bgr_image = Image.fromarray(bgr_array, 'RGB')

disp.display(bgr_image)
