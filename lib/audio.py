import board
import audiocore
import audiobusio
import audiomixer
import storage
import digitalio
import adafruit_sdcard


class _Audio:
    def __init__(self) -> None:
        self._i2s = audiobusio.I2SOut(board.A3, board.A2, board.A1)
        self._mixer = audiomixer.Mixer(
            voice_count=1,
            sample_rate=22050,
            channel_count=1,
            bits_per_sample=16,
            samples_signed=True,
        )

    def mount_sdcard(self):
        try:
            card_cs = digitalio.DigitalInOut(board.A0)
            sdcard = adafruit_sdcard.SDCard(board.SPI(), card_cs)
            vfs = storage.VfsFat(sdcard)
            storage.mount(vfs, "/sd")
            print("Mounted SD card")
        except OSError:
            pass

    def play(self, sounds, *, volume):
        print("Playing:", end=" ")
        for sound in sounds:
            file = open("/sd/" + sound + ".wav", "rb")
            wave = audiocore.WaveFile(file)
            self._mixer.voice[0].level = volume / 100
            self._i2s.play(self._mixer)
            self._mixer.voice[0].play(wave)
            print(sound, end=" ")
            while self._mixer.playing:  # wait until finish playing
                pass
            file.close()
        print()


# Instantiate the singleton
audio = _Audio()
