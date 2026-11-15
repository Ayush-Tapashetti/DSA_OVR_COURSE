"""
Word Ladder (LeetCode 127)
Given two words (begin and end) and a dictionary words, return the number of words in the shortest transformation sequence from begin to end (or 0 if no such sequence exists). 
In each step, you can change only one letter at a time, and every intermediate word must exist in words. 
"""

from collections import deque

def ladder_length(begin, end, words):
    ws = set(words)
    if end not in ws: return 0
    q = deque([(begin, 1)]); seen = {begin}
    while q:
        w, d = q.popleft()
        if w == end: return d
        for i in range(len(w)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                n = w[:i]+ch+w[i+1:]
                if n in ws and n not in seen: seen.add(n); q.append((n, d+1))
    return 0