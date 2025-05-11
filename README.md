# st7735-pi5-display
This project provides Python scripts and utilities to render static images and play videos on a 1.8" ST7735 display connected to a Raspberry Pi 5 via SPI. It includes frame conversion, resizing, and efficient drawing functions optimized for small TFT displays.

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
1. Install requirements
2. ` pip install -r requirements.txt`
