class File:
    def __init__(self, path: str):
        self.path = path
        self.content = []

    def add_content(self, *content):
        for file in content:
            self.content.append(file)

    @property
    def size(self) -> int:
        return sum([len(i) for i in self.content])
    
    def info(self):
        return f"{self.path} [{self.size}B]"
    
class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int):
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

class VideoFile(MediaFile):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int, dimensions: tuple):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

mp4 = VideoFile("/home/python/vanrossum.mp4", "h264", (23.5454, 31.4343), 487, (1920, 1080))
mp4.add_content("audio/ogg", "video/webm")


print(
    mp4.info()
)