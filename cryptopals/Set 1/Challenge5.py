def generate_xor_key(key, length):
    """repeats a key to the desired length
    Arguments:
        key {bytes} -- bytes to repeat
        length {int} -- length of the repeated key
    Returns:
        keykeykey to length specified"""
    return (key * (length // len(key) + 1))[:length]


def xor_byte(key, data):
    """xors two equal length strings together
    Arguments:
        key {bytes} -- bytes to xor with
        data {bytes} -- bytes to xor
    Returns:
        """
    # using zip
    return bytes(a ^ b for a, b in zip(key, data))


key = "ICE"

plaintext = ("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")

ciphertext = xor_byte(generate_xor_key(bytes(key, 'utf-8'), len(plaintext)), bytes(plaintext, 'utf-8'))

# ciphertext binary to hex
print(ciphertext.hex())