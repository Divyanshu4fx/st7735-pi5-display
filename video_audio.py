import sys
import cv2
from PIL import Image
import st7735
import time
import subprocess
import threading


if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <video_file>")
    sys.exit(1)

video_file = sys.argv[1]

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

def play_audio(file_path):
    subprocess.call(['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', file_path])

# Start audio playback in a separate thread
audio_thread = threading.Thread(target=play_audio, args=(video_file,))
audio_thread.start()

cap = cv2.VideoCapture(video_file)

if not cap.isOpened():
    print("Error: Cannot open video file.")
    sys.exit(1)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (WIDTH, HEIGHT))
        image = Image.fromarray(frame)
        disp.display(image)

        # Adjust frame rate
        time.sleep(1 / 44)

except KeyboardInterrupt:
    print("Video playback interrupted.")

finally:
    cap.release()
    audio_thread.join()
