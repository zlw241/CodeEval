def decode(message, key_alphabet, alphabet):
    message_list = [list(i) for i in message.split()]

    mapped_alphabet = {}

    for i in range(len(key_alphabet)):
        mapped_alphabet[key_alphabet[i]] = alphabet[i]

    doubles = []
    for x in message_list:
        temp = []
        for i in range(0, len(x), 2):
            temp.append(x[i:i+2])
        doubles.append(temp)

    for i in range(len(doubles)):
        doubles[i] = [int(''.join(x)) for x in doubles[i]]

    decoded = []

    for i in doubles:
        for x in i:
            decoded.append(mapped_alphabet[alphabet[x]])
        decoded.append(' ')

    decoded = ''.join(decoded)
    return decoded


bit_message = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119"
bit_key_alphabet = "BHISOECRTMGWYVALUZDNFJKPQX"
bit_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(decode(bit_message,bit_key_alphabet, bit_alphabet))

