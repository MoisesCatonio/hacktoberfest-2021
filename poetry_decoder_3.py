from poetry import poem3
from collections import OrderedDict

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def decode_caesar(poem):
    for i in range(len(poem)):
        poem[i] = poem[i].lower()

    result = []
    for subtext in poem:
        decoded_string = ""
        for char in list(subtext):
            if char != ' ':
                decoded_string = decoded_string + alphabet[alphabet.index(char) - 13]
            else:
                decoded_string = decoded_string + " "
        result.append(decoded_string)
    
    for verse in result:
        print(verse)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Poema 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
decode_caesar(poem3)
print("")

# print(chr(ord('a') + 1))