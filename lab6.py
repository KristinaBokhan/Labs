from abc import ABC, abstractmethod

class Downloader(ABC):
    @abstractmethod
    def download(self, file_name: str) -> str:
        pass

class SimpleDownloader(Downloader):
    def download(self, file_name: str) -> str:
        return f"Downloading file: {file_name}"

class ProxyDownloader(Downloader):
    def __init__(self):
        self.downloader = SimpleDownloader()
        self.cache = {}

    def download(self, file_name: str) -> str:
        if file_name in self.cache:
            return f"Returning cached file: {file_name}"
        else:

            result = self.downloader.download(file_name)
            self.cache[file_name] = result
            return result

def client_code(downloader: Downloader, file_name: str):
    print(downloader.download(file_name))


if __name__ == "__main__":
    print("Using SimpleDownloader:")
    simple_downloader = SimpleDownloader()
    client_code(simple_downloader, "file1.txt")
    client_code(simple_downloader, "file2.txt")

    print("\nUsing ProxyDownloader with caching:")
    proxy_downloader = ProxyDownloader()
    client_code(proxy_downloader, "file1.txt")
    client_code(proxy_downloader, "file1.txt")
    client_code(proxy_downloader, "file2.txt")
