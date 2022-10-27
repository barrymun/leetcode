def longest_palindrome(s: str) -> str:
    """
    :param s:
    :return:
    """
    max_len = 0
    res = ""
    if len(s) < 1 or len(s) > 1000:  # constraint
        return res
    for i in range(len(s), 0, -1):
        # print(f'i={i}')
        for j in range(0, i, 1):
            # print(f'j={j}')
            # print(f'res={s[j:i]}')
            if s[j:i] == s[j:i][::-1]:
                if len(s[j:i]) > max_len:
                    # print(f'res={s[j:i]}')
                    max_len = len(s[j:i])
                    res = s[j:i]
    return res


if __name__ == '__main__':
    print(longest_palindrome(s=""))
    print(longest_palindrome(s="babad"))
    print(longest_palindrome(s="cbbd"))
    print(longest_palindrome(s="cbbc"))
