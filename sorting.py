# HW: write a bubble sort and a selection sort algorithm

def bubble_sort(list):
    x = False
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            x = True
            print(list)

    if not x: 
        return list

    else:
        return bubble_sort(list)

list = [2, 1, 5, 8, 2, 4]
# print(bubble_sort(list))

def selection_sort(list):
    # x = False
    for i in range(len(list)-1):
        subset = list[i:]
        if list[i] < min(subset):
            list[i], list[list.index(min(subset))] = list[list.index(min(subset))], list[i]
            # x = True
            print(list)
            
    # if not x:
    #     return list

    # else:
    #     return selection_sort(list)
    

print(selection_sort(list))