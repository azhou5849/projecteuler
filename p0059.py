"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes.
The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
Your task has been made easy, as the encryption key consists of three lower case characters.
Using p0059cipher.txt, a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.
"""
def ascii_bin_list(n):
    """
    Creates a list of 8 bits corresponding to the integer 0 <= n <= 255 (representing a character via ASCII)
    Least significant bit comes first
    """
    left = n
    output = []
    for _ in range(8):
        output.append(left % 2)
        left = left // 2
    return output

def bin_list_ascii(lst):
    """
    Inverts the previous function
    """
    return sum(lst[i] * (2**i) for i in range(8))

def xor_bin_list(b1, b2):
    """
    Performs bitwise XOR on two 8-bit strings
    """
    return [(t[0] + t[1]) % 2 for t in zip(b1,b2)]

with open("p0059cipher.txt", 'r') as f:
    encoded = [ascii_bin_list(int(ascii)) for ascii in f.readline().strip().split(',')]

# first character should come from a capital letter
key_possible_firsts = []
for capital in range(65, 91):
    first_character_candidate = bin_list_ascii(xor_bin_list(encoded[0], ascii_bin_list(capital)))
    if first_character_candidate >= 97 and first_character_candidate <= 122:
        key_possible_firsts.append(first_character_candidate)
key_possible_firsts.sort()


print(key_possible_firsts[:10])
