import copy
name = [34, 6, 8, 'ram', ['sam', 'hk', [0, 8], 7]]
#ram = copy.copy(name)
ram = copy.deepcopy(name) 
name.append(6)
name[3] = "tom"
name[4][0] = "ramesh"
name[4][2][1] = "new"
print(name)
print(ram)
