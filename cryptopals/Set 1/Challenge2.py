def fixed_xor(key, data):
    """xors two equal length strings together
    Arguments:
        key {bytes} -- bytes to xor with
        data {bytes} -- bytes to xor
    Returns:
        """
    print(key)
    key_int = int.from_bytes(key, 'big')
    print(key_int)
    data_int = int.from_bytes(data, 'big')
    return (key_int ^ data_int).to_bytes(len(data), 'big')

a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

c = b"0000000011111111"
d = b"1111111100000000"

print(fixed_xor(bytes.fromhex(a), bytes.fromhex(b)).hex())
# print(fixed_xor(c, d))