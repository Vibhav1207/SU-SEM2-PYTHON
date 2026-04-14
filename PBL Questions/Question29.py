class CodecNotSupportedError(Exception):
    pass

class MobilePlayer:
    def play_video(self, format):
        if format == "mkv":
            raise CodecNotSupportedError()
        print("Playing")

try:
    mp = MobilePlayer()
    mp.play_video("mkv")
except CodecNotSupportedError:
    print("Not supported")
