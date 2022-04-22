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
    for bit1, bit2 in zip(data1, data2):
        diff = bit1 ^ bit2
        dist += sum([1 for bit in bin(diff) if bit == '1'])
    return dist

os.chdir('cryptopals')

keysize_difference = {}
with open('Set 1/Challenge6.txt', 'r') as input_file:
    data = input_file.read()
    for keysize in range(2,41):
        segment1 = data[:keysize]
        segment2 = data[keysize:keysize*2]
        segment3 = data[keysize*2:keysize*3]
        segment4 = data[keysize*3:keysize*4]
        distancea = calculate_hamming_distance(bytes(segment1, 'utf-8'), bytes(segment2, 'utf-8'))/ keysize
        distanceb = calculate_hamming_distance(bytes(segment1, 'utf-8'), bytes(segment3, 'utf-8'))/ keysize
        distancec = calculate_hamming_distance(bytes(segment1, 'utf-8'), bytes(segment4, 'utf-8'))/ keysize
        distanced = calculate_hamming_distance(bytes(segment2, 'utf-8'), bytes(segment3, 'utf-8'))/ keysize
        distancee = calculate_hamming_distance(bytes(segment2, 'utf-8'), bytes(segment4, 'utf-8'))/ keysize
        distancef = calculate_hamming_distance(bytes(segment3, 'utf-8'), bytes(segment4, 'utf-8'))/ keysize
        keysize_difference[keysize] = (distancea + distanceb + distancec + distanced + distancee + distancef)/6

# print keysizes with the lowest hamming distance
print(sorted(keysize_difference.items(), key=lambda x: x[1])[:4])

# print keysizes with the highest hamming distance
print(sorted(keysize_difference.items(), key=lambda x: x[1], reverse=True)[:4])

# pick shortest hamming distance for the keysize
final_key_length = sorted(keysize_difference.items(), key=lambda x: x[1])[0][0]