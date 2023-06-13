def calculate_hash(string: str, l: int, r: int, mod: int, B: int) -> int:
    """文字列strのindexl~rの部分の文字列のhash値を計算する関数

    Args:
        string (str): 文字列全体
        l (int): 取り出す文字列の最初のindex
        r (int): 取り出す文字列の最後のindex
        mod (int): ハッシュ計算時のmod
        B (int): B進法を使ってる

    Returns:
        int: 取り出す文字列のhash値。これが同じになれば、その部分文字列同士が等しいと考えられる
    """
    str_list = list(map(lambda c: ord(c) - ord("a") + 1, string))
    N = len(str_list)

    # 各文字の持つhash計算用の値を出す
    hash = [None] * (N + 1)
    hash[0] = 0
    for i in range(N):
        hash[i + 1] = (
            B * hash[i] + str_list[i]
        ) % mod  # hashとstr_listのindexの対応がずれてることに注意

    # 先にBのn乗を計算
    powerB = [None] * (N + 1)
    powerB[0] = 1
    for i in range(N):
        powerB[i + 1] = powerB[i] * B % mod

    return hash[r] - hash[l - 1] * powerB[r - l + 1] % mod
