def binary_search(list_n: list[int], target: int) -> int:
    """targetがlist_n内に含まれるか、また含まれるならindexは何番目になるか

    Args:
        list_n (list[int]): 配列
        target (int): 探索対象

    Returns:
        int: index, 含まれなかった場合は-1
    """
    n = len(list_n)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if target < list_n[middle]:
            right = middle - 1
        if target == list_n[middle]:
            return middle
        if target > list_n[middle]:
            left = middle + 1
    return -1  # targretが存在しない


def binary_search_sub1(list_n: list[int], target: int) -> int:
    """ソートされた配列に挿入対象を挿入したときのindex

    Args:
        list_n (list[int]): 配列
        target (int): 挿入対象

    Returns:
        int: 挿入される場合のindex
    """
    # Input: nums = [1,3,5,6], target = 5
    # Output: 2
    # Input: nums = [1,3,5,6], target = 2
    # Output: 1
    # 二分探索はソートされてるものに対してするけど、探索されるものそのものが1,2,3と連続してたらいいけどそうとは限らない。
    # 二分探索では連続した整数値を対象にstartやendを取らないといけなくて、つまりindexなら取ることができる。
    # indexからstart/endを取った場合、ソートされてる配列そのものにはindexでアクセスすればいいだけ。

    n = len(list_n)
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end) // 2
        if target < list_n[middle]:
            end = middle - 1
            continue
        if target > list_n[middle]:
            start = middle + 1
            continue
        if target == list_n[middle]:
            return middle
    else:
        return end + 1  # 　ここは実験的にわかることかも
