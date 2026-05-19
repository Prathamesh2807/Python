set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 8, 9}

if not set1.isdisjoint(set2):
    print("Common elements found!")
else:
    print("No common elements.")