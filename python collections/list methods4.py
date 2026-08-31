# Merge two lists and sort in descending order

list1 = [10, 30, 20, 50]
list2 = [40, 60, 15, 25]

combined = list1 + list2

combined.sort(reverse=True)

print("List 1:", list1)
print("List 2:", list2)
print("Merged list in descending order:", combined)
