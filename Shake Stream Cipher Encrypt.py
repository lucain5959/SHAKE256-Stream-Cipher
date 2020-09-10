import secrets
import base64
from hashlib import shake_256

class ShakeStreamCipher:

    def __init__(self, key, nonce, hasher=shake_256):
        __call__ = hasher
        self._h = hasher(data)
        self._pos = 0

    def keystream(self, n):
        """Return a number of bytes from the keystream"""
        newpos = self._pos + n
        length = self._pos+newpos
        stream = self._h.digest(length)
        self._pos = newpos
        return stream

    def encrypt(self, plain):
        """Encrypt bytes object 'plain' with keystream"""
        stream = self.keystream(len(plain))
        try:
            return bytes(x^y for x, y in zip(plain, stream))
        except TypeError as e:
            self._pos -= len(plain)
            raise TypeError("argument must be a bytes object") from e

    decrypt = encrypt

#Nonce and key can be manually input. Since this is a stream cipher it needs a unique nonce

randomBitNumber = secrets.token_bytes(32)
print ("Nonce is:", base64.b64encode(randomBitNumber))

randomkeynumber = secrets.token_bytes(32)
print ("Key is:", base64.b64encode(randomkeynumber))

nonce = randomBitNumber
key = randomkeynumber

data = randomBitNumber+randomkeynumber

cipher = ShakeStreamCipher(key=key, nonce=nonce)
plaintext = b"plaintext"
ciphertext = cipher.encrypt(plaintext)
print ("Cipher text is",base64.b64encode(ciphertext))
