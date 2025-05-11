# st7735-pi5-display
This project provides Python scripts and utilities to render static images and play videos on a 1.8" ST7735 display connected to a Raspberry Pi 5 via SPI. It includes frame conversion, resizing, and efficient drawing functions optimized for small TFT displays.

![Image](https://github.com/Divyanshu4fx/st7735-pi5-display/blob/main/content/image.jpg)

## Pin Connections
| Display Pin | Board Pin |
|:------------|:----------|
| VCC | 3.3V |
| GND | GND  |
| SDA/MOSI | GPIO 10 |
| SCL | GPIO 11 |
| CS  | GPIO 8  |
| RST | GPIO 25 |
| DC  | GPIO 24 |
| BL  | 3.3V    |

## Setup
1. Enable SPI interface on Pi 5
   - Run `sudo raspi-config`
   - Go to Interface Options
   - Select SPI
   - Enable SPI
2. Install Requirements
   ```bash
   pip install -r requirements.txt
   ```
3. Change Display Height and Width in st7735 libray location to get full display.
   - go to `~/lib/python3.11/site-packages/st7735/__init__.py` Or your python installation location
   - change these variables according to your display size
   ```python
   ST7735_TFTWIDTH = 128
   ST7735_TFTHEIGHT = 160
   ```
4. Install ffmpeg
   ```bash
   sudo apt install ffmpeg
   ```
5. Run the code
   ```bash
   python image.py ./content/cat.jpg
   ```
