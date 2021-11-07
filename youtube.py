def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def locate_card(cards, query):
    
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
                print(f'mid: {mid}')
            else:
                return 'found'
                print(f'mid: {mid}')
        elif cards[mid] > query:
            return 'left'
            print(f'mid: {mid}')
        else:
            return 'right'
            print(f'mid: {mid}')
    
    return binary_search(0, len(cards)-1, condition)

karty = [0,1,2,3,3,4,5,6,7,7]
karta = 2

print(locate_card(karty, karta))