class MyErrors(Exception):
    def __init__(self, error: str):
        self.error = error

    def __repr__(self):
        return self.error
