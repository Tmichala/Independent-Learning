import os


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


def calculate_hamming_distance(data1, data2):
    # assert len(data1) == len(data2)
    dist = 0
    print(tuple(zip(data1, data2)))
    for bit1, bit2 in zip(data1, data2):
        diff = bit1 ^ bit2
        dist += sum([1 for bit in bin(diff) if bit == '1'])
    return dist

os.chdir('cryptopals')

# Turns strings into bits of 1 and 0
test1 = "this is a test"
test2 = "wokka wokka!!!"

print(calculate_hamming_distance(bytes(test1, 'utf-8'), bytes(test2, 'utf-8')))

'''with open('Set 1/Challenge6.txt', 'r') as input_file:
    data = input_file.read()
    for key in range(2,41):
'''