def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid, lo)
        if result == 'found':
            return mid
        if result == 'start':
            return lo
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
        #print(mid)
    return 0


def count_rotations(entry_list):
    
    def condition(mid, lo):
        if mid > 0 and entry_list[mid] < entry_list[mid-1]:
                return 'found'
        elif entry_list[mid] < entry_list[len(entry_list)-1]:
            return 'left'
        elif entry_list[mid] > entry_list[len(entry_list)-1]:
            return 'right'
    
    return binary_search(0, len(entry_list)-1, condition)


def count_rotations_find_target(entry_list, target):
    
    def condition(mid, lo):
        rotated_index = count_rotations(entry_list)
        if mid > 0 and entry_list[mid] == target:
            return 'found'
        elif entry_list[lo] == target:
            return 'start'
        elif mid < rotated_index:
            if entry_list[lo] > target and entry_list[mid] > target:
                return 'right'
            #elif entry_list[0] > target and entry_list[mid] < target:
                #return 'right'
            elif entry_list[lo] < target and entry_list[mid] > target:
                return 'left'
            elif entry_list[lo] < target and entry_list[mid] < target:
                return 'right'
        elif mid >= rotated_index:
            if entry_list[lo] > target and entry_list[mid] > target:
                return 'left'
            elif entry_list[lo] > target and entry_list[mid] < target:
                return 'right'
           # elif entry_list[0] < target and entry_list[mid] > target:
            #    return 'right'
            #elif entry_list[0] < target and entry_list[mid] < target:
             #   return 'right'

    
    return binary_search(0, len(entry_list)-1, condition)

#def count_rotations(entry_list):
 #   i = 0
  #  while i<len(entry_list)-1 and entry_list[i+1]>entry_list[i] :
  #      i += 1
  #  if i != len(entry_list)-1 and len(entry_list) != 0:
   #     return i+1
  #  else: return 0

test1 = {
    'input' : {
        'nums' : [4, 5, 6, 7, 8, 1, 2, 3]
    },
    'output' : 2
}

test2 = {
    'input' : {
        'nums' : [1, 2, 3, 4, 0]
    },
    'output' : 2
}

test3 = {
    'input' : {
        'nums' : [0]
    },
    'output' : 0
}

test4 = {
    'input' : {
        'nums' : []
    },
    'output' : 0
}

tests = [test1]

for item in tests:
    print(count_rotations_find_target(item['input']['nums'], item['output']))
