def count_rotations(entry_list):
    i = 0
    while i<len(entry_list)-1 and entry_list[i+1]>entry_list[i] :
        i += 1
    if i != len(entry_list)-1 and len(entry_list) != 0:
        return i+1
    else: return -1

print(count_rotations([]))
