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


def hex_to_b64(input_string):
    import base64
    return base64.b64encode(bytes.fromhex(input_string)).decode('utf-8')

