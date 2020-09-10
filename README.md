# SHAKE256-Stream-Cipher
In this example of turning a hash algorithm into a stream cipher, SHAKE256 is initialized with a key and nonce to encrypt text. No dependencies are needed.  

The key and nonce creates a keystream which is undergoes exclusive or with the plaintext. 
