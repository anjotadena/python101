from abc import ABC, abstractmethod

# Abstrac: is a contruct

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Cannot do this operation. Stream already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Cannot do this operation. Stream already closed.")
        self.opened = False
    
    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        if not self.opened:
            raise InvalidOperationError("Cannot do this operation. Stream is not yet open.")
        print("Read file Stream...")

class NetworkStream(Stream):
    def read(self):
        if not self.opened:
            raise InvalidOperationError("Cannot do this operation. Stream is not yet open.")
        print("Read network stream...")

stream = FileStream()

# stream.read()
stream.open()

stream.read()

