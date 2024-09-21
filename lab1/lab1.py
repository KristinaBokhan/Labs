from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def connect(self):
        pass

class LocalDisk(Storage):
    def connect(self):
        print("Connected to Local Disk")

class AmazonS3(Storage):
    def connect(self):
        print("Connected to Amazon S3")

class StorageManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StorageManager, cls).__new__(cls)
            cls._instance.storage = None
        return cls._instance

    def set_storage(self, storage: Storage):
        self.storage = storage

    def connect_to_storage(self):
        if self.storage is not None:
            self.storage.connect()
        else:
            print("No storage selected!")

if __name__ == "__main__":
    manager = StorageManager()

    local_disk = LocalDisk()
    manager.set_storage(local_disk)
    manager.connect_to_storage()

    amazon_s3 = AmazonS3()
    manager.set_storage(amazon_s3)
    manager.connect_to_storage()

