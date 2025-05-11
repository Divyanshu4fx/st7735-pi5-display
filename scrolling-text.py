import time
from PIL import Image, ImageDraw, ImageFont
import st7735

MESSAGE = "Hello World! How are you today?"

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

disp.begin()

WIDTH = disp.width
HEIGHT = disp.height


img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)

x1, y1, x2, y2 = font.getbbox(MESSAGE)
size_x = x2 - x1
size_y = y2 - y1

text_x = 160
text_y = (80 - size_y) // 2

t_start = time.time()

while True:
    x = (time.time() - t_start) * 100
    x %= (size_x + 160)
    draw.rectangle((0, 0, 160, 80), (0, 0, 0))
    draw.text((int(text_x - x), text_y), MESSAGE, font=font, fill=(255, 255, 255))
    disp.display(img)
