class DiskFullError(Exception):
    pass

class HTTPDownloader:
    def fetch_file(self, space, size):
        if space < size:
            raise DiskFullError()

try:
    d = HTTPDownloader()
    d.fetch_file(100, 200)
except DiskFullError:
    print("Download paused")
