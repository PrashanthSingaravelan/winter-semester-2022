def a2d(text):
    return [ord(i) for i in text]


def encrpyt(text, key):
    dtext = a2d(text)
    result = []
    for i in dtext:
        if (i >= 65 and i <= 90):
            result.append((((i - 65) + key) % 26) + 65)
        elif(i >= 97 and i <= 122):
            result.append((((i - 97) + key) % 26) + 97)
        else:
            result.append(i)
    final = list(map(chr, result))
    return ''.join(final)


def decrypt(text, key):
    dtext = a2d(text)
    result = []
    for i in dtext:
        if (i >= 65 and i <= 90):
            result.append((((i - 65) - key) % 26) + 65)
        elif(i >= 97 and i <= 122):
            result.append((((i - 97) - key) % 26) + 97)
        else:
            result.append(i)
    final = list(map(chr, result))
    return ''.join(final)


if __name__ == '__main__':
    text = input("Before encryption Plain text: ")
    key = int(input("Key: "))
    
    cipher = encrpyt(text, key)
    print("Cipher text : {}".format(cipher))
    
    plain = decrypt(cipher, key)
    print("After decryption Plain text : {}".format(plain))
