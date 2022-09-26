dict1 = {0: "abc", 1: "def"}

dict2 = dict1

print(dict2)

dict1[2] = "ghi"

print(dict2)

dict3 = dict1.copy()

print(f'[x] dict3: {dict3}')

dict1[4] = "jkl"

print(f'[x] dict2: {dict2}')
print(f'[x] dict3: {dict3}')