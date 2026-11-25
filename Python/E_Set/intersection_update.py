set1 = {10, 20, 30, 40, 50}
set2 = {15,20,30,40,60}
print("Set 1: ", set1)
print("------------------->>>")
print("Set 2: ", set2)
print("------------------->>>")
set1.intersection_update(set2)
print("after intersection_update:", set1)