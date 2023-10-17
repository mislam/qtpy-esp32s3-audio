# Audio Player for Adafruit QT Py ESP32-S3

This repository demonstrates the implementation of a audio player on the Adafruit QT Py ESP32-S3 board using CircuitPython.

## Overview

- **Hardware:** [Adafruit QT Py ESP32-S3](https://learn.adafruit.com/adafruit-qt-py-esp32-s3) \w 4MB Flash and 2MB PSRAM and [Adafruit Audio BFF](https://learn.adafruit.com/adafruit-audio-bff).
- **Platform:** [CircuitPython 8.2.6](https://learn.adafruit.com/adafruit-qt-py-esp32-s3/circuitpython-2)
- **Library:** [Adafruit CircuitPython MiniMQTT v7.4.2](https://github.com/adafruit/Adafruit_CircuitPython_MiniMQTT)

## Getting Started

To run this project, follow these steps:

1. **Setup CircuitPython:** Ensure that CircuitPython is installed on your Adafruit QT Py ESP32-S3 board.

2. **SD Card:** Copy the two `.wav` files from your computer to a micro SD card. Then insert it to the Audio BFF's micro SD card slot.

3. **Connection:** Connect **QT Py** and **Audio BFF** boards. Add a 4Ω 3W speaker to the speaker connector.

4. **Upload Code:** Upload the project code to your board. You can use a tool like [CircuitPython Code Editor](https://code.circuitpython.org/) to transfer files to the board over WiFi.

5. **Execute:** Run the code on your board. When you press the **BOOT** button, it should play two machine-generated voice messages.

## Contributing

Contributions to this project are welcome. If you would like to enhance or extend the functionality, please submit issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
