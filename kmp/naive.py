#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2019-01-15 18:59:37

def naive(s, t):
    for i in range(len(s)-len(t)+1):
        if s[i:(len(t)+i)] == t:
            return i
    return -1

def naive2(s, t):
    len_s = len(s)
    len_t = len(t)
    i = 0
    while i <= (len_s - len_t):
        for j in range(len_t):
            if s[i] == t[j]:
                i += 1
            else:
                i = i-j+1
                break
            if (j == (len_t -1)):
                return i - len_t
    return -1

def naive3(s, t):
    len_s = len(s)
    len_t = len(t)
    i = 0
    while i <= (len_s - len_t):
        j = 0
        while j < len_t:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i = i-j+1
                j = 0
                break
            if (j == len_t):
                return i - len_t
    return -1


if __name__ == "__main__":
    print(naive("abcdefsssdfsdfsdfsdf", "ef"))
    print(naive("abcdefsssdfsdfsdfsdf", "ff"))

    print(naive2("abcdefsssdfsdfsdfsdf", "ef"))
    print(naive2("abcdefsssdfsdfsdfsdf", "ff"))

    print(naive3("abcdefsssdfsdfsdfsdf", "ef"))
    print(naive3("abcdefsssdfsdfsdfsdf", "ff"))
