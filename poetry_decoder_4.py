from poetry import poem1, poem2
from collections import OrderedDict

def decode_numbers(poem):
    ordered = {}
    keys = []
    for subdivision in poem:
        subdivision_key = [int(k) for k in list(subdivision) if k.isdigit()]
        keys.extend(subdivision_key)

    count = 0
    for key in keys:
        ordered[key] = poem[count]
        count += 1 
    
    ordered = OrderedDict(sorted(ordered.items()))
    for key in ordered:
        print(ordered[key])
    
def decode_first_letter(poem):
    ordered = {}
    keys = []
    for subdivision in poem:
        subdivision_key = [subdivision[0].lower()]
        keys.extend(subdivision_key)

    count = 0
    for key in keys:
        ordered[key] = poem[count]
        count += 1 
    
    ordered = OrderedDict(sorted(ordered.items()))
    for key in ordered:
        print(ordered[key])

def decode_cesar(poem):
    pass

def decode_last_letter(poem):
    pass

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Poema 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
decode_numbers(poem1)
print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Poema 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
decode_first_letter(poem2)
print("")