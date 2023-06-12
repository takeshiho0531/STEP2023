def binary_search(list_n: list[int], target: int):
    n=len(list_n)
    left=0
    right=n
    while left<=right:
        middle=(left+right)//2
        if target<list_n[middle]:
            right=middle-1
        if target==list_n[middle]:
            return middle
        if target>list_n[middle]:
            left=middle+1
    return -1  # targretが存在しない

