from abc import ABC, abstractclassmethod

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

