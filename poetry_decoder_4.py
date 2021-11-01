from poetry import poem4
from collections import OrderedDict

def decode_last_letter(poem):
    ordered = {}
    keys = []
    for subdivision in poem:
        subdivision_key = [subdivision[-1].lower()]
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

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Poema 4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
decode_last_letter(poem4)
print("")
