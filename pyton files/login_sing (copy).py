array = [1,[2],[3,[7,8,6],[4,5,[6,[7,8,9,[10]]],9]],0,9]
array2 = []
ind = 0
changes = 0
while True:
    if type(array[ind]) == list:
        array2.extend(array.pop(ind))
        changes += 1
    if len(array)!=0 and type(array[ind]) != list:
        array2.append(array.pop(ind))
    if len(array)==0:
        if changes == 0:
            print(array2)
            break
        else:
            array = array2.copy()
            array2.clear();  
        changes = 0