class CorruptAudioFileError(Exception):
    pass

class BassBoost:
    def apply_effect(self, file_ok):
        if not file_ok:
            raise CorruptAudioFileError()

try:
    bb = BassBoost()
    bb.apply_effect(False)
except CorruptAudioFileError:
    print("Empty waveform")
