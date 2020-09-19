# SHAKE256-Stream-Cipher
In this example of turning a hash algorithm into a stream cipher, SHAKE256 is initialized with a key and nonce to encrypt text. No dependencies are needed. My name for SHAKE as a stream cipher is Cookies and Code SHAKE. 

The key and nonce creates a keystream which is undergoes XOR with the plaintext. 

Note: Message lengths of less than 256 bits of length have less than 256 bits of security. Pad small messages for more security. 
