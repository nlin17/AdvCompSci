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
    if not collection or element not in collection: return False


    def helper(element, collection, start, stop):
        
        halfway = (collection.index(stop) - collection.index(start)) // 2
        if halfway == 0 and collection.index(stop) == len(collection) - 1:
            halfway = 1
        halfway = int(halfway) + collection.index(start)

        print(f"guess: {collection[halfway]}")

        if element == collection[halfway]: 
            print("you guessed it!")
            return True
        
        elif element > collection[halfway]:
            start = collection[halfway]

        else:
            stop = collection[halfway]

        helper(element, collection, start, stop)

    helper(element, collection, collection[0], collection[-1])

    # if nothing in array, return false
    # check middle element
    # check higher or lower
    # if higher/lower return whether in left/right
    # recursive, use helper function
    
collection = [1, 4, 5, 7, 9, 14, 18, 19, 25]
binary_search(1, collection)