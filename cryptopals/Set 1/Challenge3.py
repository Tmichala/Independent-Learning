# The hex-encoded string has been XOR'd against a single character. Find the key, decrypt the message.
import base64
from basic_functions import *
import string


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


input_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

frequency_dict = {
    'E': 56.88,
    'A': 43.31,
    'R': 38.64,
    'I': 38.45,
    'O': 36.51,
    'T': 35.43,
    'N': 33.92,
    'S': 29.23,
    'L': 27.98,
    'C': 23.13,
    'U': 18.51,
    'D': 17.25,
    'P': 16.14,
    'M': 15.36,
    'H': 15.31,
    'G': 12.59,
    'B': 10.56,
    'F': 9.24,
    'Y': 9.06,
    'W': 6.57,
    'K': 5.61,
    'V': 5.13,
    'X': 1.48,
    'Z': 1.39,
    'J': 1.00,
    'Q': 0.98,
}

# hex to utf-8
text = bytes.fromhex(input_hex).decode('utf-8')

# input hex to bytes
input_bytes = bytes.fromhex(input_hex)

# create list of letters and numbers
# get all ascii characters and punctuation
possible_keys = list(string.printable)

answer_dict = {}

for char in possible_keys:
    # key to bytes
    key = generate_xor_key(char, len(input_bytes))
    key_bytes = bytes(key, 'utf-8')
    answer = xor_byte(key_bytes, input_bytes)
    
    # convert answer to string
    answer_string = answer.decode('utf-8')

    # calculate score
    score = 0
    for character in answer_string.upper():
        if character in frequency_dict:
            char_u = character.upper()
            score += frequency_dict[char_u]
    answer_dict[f"{char} - {answer_string}"] = score
    print(f"{char}: {answer_string} : {score}")

# print top 5 scores and keys
print("Top 5 scores:")
for key, score in sorted(answer_dict.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{key}: {score} ")
