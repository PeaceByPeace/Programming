def recursive_binary_search(lst, target):

    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst)//2

    if lst[midpoint] == target:
        return True
    elif lst[midpoint] < target:
        return recursive_binary_search(lst[midpoint+1:], target)
    else:
        return recursive_binary_search(lst[:midpoint], target)


def verify(result):
    print("Target found: ", result)


nums = [1,2,3,4,5,6,7,8]

result = recursive_binary_search(nums, 5)
verify(result)