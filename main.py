# Demo audio player that plays random wav files from internal storage or
# SD card. Default pinout matches the Audio BFF for QT Py S2, S3 and RP2040

import board
import digitalio
from audio import *

button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)

audio.mount_sdcard()

while True:
    if not button.value:
        audio.play(["hello", "intro"], volume=5)
