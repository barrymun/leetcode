def helper(s: str, l_index: int, r_index: int):
    """
    get the longest palindrome
    :param s:
    :param l_index:
    :param r_index:
    :return:
    """
    while 0 <= l_index and r_index < len(s) and s[l_index] == s[r_index]:
        l_index -= 1
        r_index += 1
    return s[l_index + 1:r_index]


def longest_palindrome(s: str) -> str:
    """
    :param s:
    :return:
    """
    res = ""
    for i in range(len(s)):
        odd_case = helper(s, i, i)
        even_case = helper(s, i, i + 1)
        res = max(odd_case, even_case, res, key=len)
    return res


if __name__ == '__main__':
    print(longest_palindrome(s=""))
    print(longest_palindrome(s="babad"))
    print(longest_palindrome(s="cbbd"))
    print(longest_palindrome(s="cbbc"))
    print(longest_palindrome(s="ac"))
    print(longest_palindrome(
        s="qkajbumzdzkiplmbcpnhbzweoevrvbptpozhtrfntszvnwbdahvkykmezrwruhvvslngruvwqebudtfxgpbmwefczwrecpqjegxkqknpobzkemmtruidulnxgntjxcmxtwmlxhzmbqfqylwvzjyojhfawwuupiipvxjiyxkqvsxbhgzzegfkdihizvjoxzrmeorikzsdyphbujaqmykrfblneqmwwxsoonzsgvligqxrrumspylfvquklbanjhkudlprwoycpxdsueokruoofyubirbhbyfuvgllijywuqmkcsfjttbnmelrylivkefllepgxnoeummujbaoyvryukyoumvuxezegpwgmwsupjuaarvbtbfmisrifjadqjypmzipvjysgakvjhfeaqwpsqijvqibshctuabwqqsjwotjopahoaptmxkwerkjkmwiodgblhtnhykzjuaoluoyokroxuvqtkpggfanzabgjejdfsgybhxbscubdpufywbxgutheskuhixasnksoayjngvhfoxxclykfobrwxjwgefarzczvptlfrgrtrjcemaeihpukhbeoezgvrwxgyhpkkfvmfvquwtswkdwqqgrgasopladdnteulqofmjhewpghkibbrewnhdllfppctgkfkoedoiwqocnpvfviochrokrgrzthrvyhqfsrzyyvqwkhuzsrkfaympcdodkwaojnghzytkhf"))
