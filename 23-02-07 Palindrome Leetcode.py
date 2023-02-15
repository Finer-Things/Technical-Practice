def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numeric_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alpha_numeric_list = alpha_list + numeric_list + [letter.upper() for letter in alpha_list]
    print(alpha_numeric_list)
    significant_symbols_list = [letter for letter in s if letter in alpha_numeric_list]
    significant_symbols_list = [letter.lower() for letter in significant_symbols_list]
    print(significant_symbols_list)
    backwards_significant_list = significant_symbols_list[::-1]
    for i, character in enumerate(significant_symbols_list):
        if character != backwards_significant_list:
            return False
    return True

isPalindrome("A man, a plan, a canal: Panama")