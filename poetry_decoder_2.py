from poetry import poem2
from collections import OrderedDict
    
def decode_first_letter(poem):
    ordered = {}
    keys = []
    for subdivision in poem:
        subdivision_key = [subdivision[0].lower()]
        keys.extend(subdivision_key)

    index = 0
    for key in keys:
        ordered[key] = poem[index]
        index += 1 
    
    ordered = OrderedDict(sorted(ordered.items()))
    for key in ordered:
        print(ordered[key])

print("=============================== Poema 2 ===============================")
decode_first_letter(poem2)
print("")