# PRACTICE PROBLEM Q04 — Palindrome Check Using a Deque
def palindrome_deque():

    from collections import deque as _deque

    def is_palindrome(s):
        dq = _deque(s)
        while len(dq) > 1:
            if dq.popleft() != dq.pop():   # compare FRONT and REAR
                return False
        return True

    for test in ["racecar", "hello", "", "a", "abba", "abcd"]:
        print(f"is_palindrome({test!r}) -> {is_palindrome(test)}")

palindrome_deque()