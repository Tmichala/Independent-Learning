def hex_to_b64(input_string):
    import base64
    return base64.b64encode(bytes.fromhex(input_string)).decode('utf-8')