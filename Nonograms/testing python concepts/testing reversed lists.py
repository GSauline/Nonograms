l1 = ['bob', '1', 2, True, 'frodrich']
l2 = [l1[val] for val in range(len(l1)-1,-1,-1)]
print("original list", l1)
print("reversed list", l2)