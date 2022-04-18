from basic_functions import fixed_xor

a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

c = b"0000000011111111"
d = b"1111111100000000"

print(fixed_xor(bytes.fromhex(a), bytes.fromhex(b)).hex())
# print(fixed_xor(c, d))