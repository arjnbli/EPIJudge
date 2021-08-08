from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    # TODO - you fill in here.
    if len(s) == 0:
        return True
    p1 = 0
    p2 = len(s) - 1
    while p1 <= p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
