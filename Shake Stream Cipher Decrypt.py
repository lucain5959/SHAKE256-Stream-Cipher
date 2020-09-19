import secrets
from hashlib import shake_256
import base64

class ShakeStreamCipher:

    def __init__(self, key, nonce, hasher=shake_256):
        __call__ = hasher
        self._h = hasher(data)
        self._pos = 0
        
    def keystream(self, n):
        #Return bytes from the keystream
        newpos = self._pos + n
        length = self._pos+newpos
        stream = self._h.digest(length)
        self._pos = newpos
        return stream

    def encrypt(self, plaintextmessage):
        #Encrypt the bytes of the plaintext with the keystream
        stream = self.keystream(len(plaintextmessage))
        try:
            return bytes(x^y for x, y in zip(plaintextmessage, stream))
        except TypeError as e:
            self._pos -= len(plain)
            raise TypeError("argument must be a bytes object") from e
    decrypt = encrypt

#Nonce and key can be manually input. Since this is a stream cipher it needs a unique nonce


nonce = (base64.b64decode('xMMqSEXoAz6GHr0SRZfKrxQoZdNqPgeL6sk+M2F26Eo='))
key = (base64.b64decode('+4hGD9k6uPcQQlGgNL60Qh1G3Bm6/aKP8A+T0t/6jzQ='))

data = nonce+key

cipher = ShakeStreamCipher(key=key, nonce=nonce)
ciphertext = (base64.b64decode('H+FDr+C/9XPi'))
decryptedtext = cipher.decrypt(ciphertext)
print ("Cipher text is",decryptedtext)
