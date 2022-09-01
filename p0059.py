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
valid_chars = list(range(32,60)) + list(range(65,91)) + list(range(97,123)) + [63,91,93]  # add characters as needed until stuff shows up

with open("p0059cipher.txt", 'r') as f:
    encoded = [int(ascii) for ascii in f.readline().strip().split(',')]

allowed_firsts = []
for a in range(97,123):
    candidate = True
    i = 0
    while i < len(encoded):
        char = a ^ encoded[i]
        if char not in valid_chars:
            candidate = False
            #print(char,chr(char))
            break
        i += 3
    if candidate:
        allowed_firsts.append(a)
#print(allowed_firsts)

allowed_seconds = []
for b in range(97,123):
    candidate = True
    i = 1
    while i < len(encoded):
        char = b ^ encoded[i]
        if char not in valid_chars:
            candidate = False
            #print(char,chr(char))
            break
        i += 3
    if candidate:
        allowed_seconds.append(b)
#print(allowed_seconds)

allowed_thirds = []
for c in range(97,123):
    candidate = True
    i = 2
    while i < len(encoded):
        char = c ^ encoded[i]
        if char not in valid_chars:
            candidate = False
            #print(char,chr(char))
            break
        i += 3
    if candidate:
        allowed_thirds.append(c)
#print(allowed_thirds)

for a in allowed_firsts:
    for b in allowed_seconds:
        for c in allowed_thirds:
            decoded_message = ""
            ascii_sum = 0
            for i in range(len(encoded)):
                if i % 3 == 0:
                    decoded_char = a ^ encoded[i]
                elif i % 3 == 1:
                    decoded_char = b ^ encoded[i]
                else:
                    decoded_char = c ^ encoded[i]
                decoded_message += chr(decoded_char)
                ascii_sum += decoded_char
            print(decoded_message)
            print(ascii_sum)
