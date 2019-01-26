import random
import string

def gen_next(t):
    ret = []
    j = 0
    for i in range(len(t)):
        if i == 0:
            ret.append(0)
        if t[i] == t[j]:
            j += 1
            ret.append(j)
        else:
            j = 0
            ret.append(0)
    return ret

def kmp(s, t):
    len_s = len(s)
    len_t = len(t)
    i = 0
    t_next = gen_next(t)
    while i <= (len_s - len_t):
        j = 0
        while j < len_t:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                # 由于找到不匹配的位置了，这里ｉ要保持为已经匹配过的位置
                # 这里 i = i - j + 1 不代表是后退了，是因为i需要满足i>j
                i = i-j+1

                # 这里如果不匹配了，那么ｊ就需要回退，回退值为 已匹配的字符数 - 对应的部分匹配值
                j = j - (i - t_next[j])
                break
            if (j == len_t):
                return i - len_t
    return -1

def random_str(num):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return ran_str
if __name__ == "__main__":
    for i in range(100):
        s = random_str(20)
        n = random.randint(0, 15)
        t = s[n:n+3]
        index = kmp(s, t)
        assert index != -1
        assert s[index:index+3] == t

