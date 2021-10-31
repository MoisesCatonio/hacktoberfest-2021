from poetry import poem1
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
    

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~Poema 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
decode_numbers(poem1)
print("")