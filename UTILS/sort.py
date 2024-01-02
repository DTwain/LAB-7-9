def default_cmp(x, y):
    if x < y: 
        return False
    return True

def default_key(x):
    return x

def shell_sort(iterable_obj, key = default_key, reverse = False, cmp = default_cmp):
    iterable_obj_as_list = list(iterable_obj)
    n = len(iterable_obj_as_list)
    gap = n // 2
    while gap > 0:
        j = gap 
        while j < n:
            i = j - gap
            while i >= 0:
                if cmp(key(iterable_obj_as_list[i]), key(iterable_obj_as_list[i + gap])) == False:
                    break
                else:
                    iterable_obj_as_list[i], iterable_obj_as_list[i + gap] = iterable_obj_as_list[i + gap], iterable_obj_as_list[i]
                i -= gap
            j += 1
        gap //= 2
    if reverse:
        iterable_obj_as_list.reverse()
    return iterable_obj_as_list
  
def bubble_sort(iterable_obj, key = default_key, reverse = False, cmp = default_cmp):
    iterable_obj_as_list = list(iterable_obj)
    for i in range(0, len(iterable_obj_as_list) - 1):
        for j in range(i+1, len(iterable_obj)):
            if cmp(key(iterable_obj_as_list[i]), key(iterable_obj_as_list[j])):
                iterable_obj_as_list[i], iterable_obj_as_list[j] = iterable_obj_as_list[j], iterable_obj_as_list[i]
    if reverse:
        iterable_obj_as_list.reverse()
    return iterable_obj_as_list

