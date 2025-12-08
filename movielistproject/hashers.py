from django.contrib.auth.hashers import BasePasswordHasher

class SimpleHasher(BasePasswordHasher):
    """
    Saves the password unhashed
    """

    algorithm = "simple"

    def encode(self, password, salt=None):
        return self.algorithm + "$" + password

    def decode(self, encoded):
        algorithm, password = encoded.split("$", 1)
        return {"algorithm": algorithm, "hash": password}

    def verify(self, password, encoded):
        return encoded == self.encode(password)
