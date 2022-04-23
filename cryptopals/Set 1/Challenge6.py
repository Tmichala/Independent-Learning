import os
from itertools import combinations
import base64

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

keysize_differences = {}
with open('Set 1/Challenge6.txt', 'r') as input_file:
    # decode the base64 file
    data = base64.b64decode(input_file.read())
    for keysize in range(2,40):
        # get sample_max identically sized samples of the data as a list of bytes
        sample_max = 20
        samples = []
        for segment in range(0, sample_max):
            sample = data[(segment*keysize):((segment+1)*keysize)]
            samples.append(sample)
        # calculate the hamming distance between each pair of samples
        keysize_difference = sum([calculate_hamming_distance(sample1, sample2) for sample1, sample2 in combinations(samples, 2)])
        # normalize keysize difference by dividing by the number of sample combinations and keysize 
        keysize_difference = keysize_difference / (((sample_max-1)*(sample_max/2)) * keysize)
        # add the keysize and its difference to the dictionary
        keysize_differences[keysize] = keysize_difference

print("(Keysize, Difference)")
# print all keysizes and their differences, sorted by difference
for keysize in sorted(keysize_differences.items(), key=lambda x: x[1]):
    print(f'{keysize}')

# print keysizes with the lowest hamming distance
print(f"Best candidates: {sorted(keysize_differences.items(), key=lambda x: x[1])[:10]}")

# print keysizes with the highest hamming distance
print(f"Worst candidates: {sorted(keysize_differences.items(), key=lambda x: x[1], reverse=True)[:10]}")

# pick shortest hamming distance for the keysize
final_key_length = sorted(keysize_differences.items(), key=lambda x: x[1])[0][0]
print(f"Final key length: {final_key_length}")