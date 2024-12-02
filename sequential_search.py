def is_in(e, collection):
    for c in collection:
        if c == e: return True
    return False

def sequential_search(e, collection):
    pos = 0
    while pos < len(collection):
        if collection[pos] == e:
            return pos
        if collection[pos] > e: return -1

        pos += 1

    return -1

def binary_search(element, collection):
    if not collection: return False
    

    def helper(element, collection, start, stop):
        halfway = (collection.index(stop) - collection.index(start)) // 2
        if element == collection[halfway]: 
            return True
        else:
            if element > collection[halfway]:
                start == halfway
                helper(element, collection, start, stop)
            elif element < collection[halfway]:
                stop == halfway
                helper(element)

    # if nothing in array, return false
    # check middle element
    # check higher or lower
    # if higher/lower return whether in left/right
    # recursive, use helper function
    
collection = [1, 4, 5, 7, 9, 14, 17]