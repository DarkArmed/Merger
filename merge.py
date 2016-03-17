N = 1 << 10

def to_string(code):
    ans = ''
    i = 0
    while code > 0:
        if code & 1:
            ans += str(i)
        code >>= 1
        i += 1
    return ans


def merge(nums):
    print
    print nums

    flag = [False] * N

    for num in nums:
        code = 0
        for char in num:
            code += 1 << ord(char) - ord('0')
        flag[code] = True

    for num in range(1, N):
        if not flag[num]:
            mask = 1
            while mask <= num:
                if (mask & num) and not flag[num - mask]:
                    break
                mask <<= 1
            else:
                flag[num] = True

    merged = []
    for num in range(1, N):
        if flag[num]:
            mask = 1
            while mask < num:
                if (num & mask):
                    flag[num - mask] = False
                mask <<= 1
    for num in range(1, N):
        if flag[num]:
            merged.append(to_string(num))
    return merged


print merge(['012', '013', '023', '123'])
print merge(['012', '013', '023', '124', '134', '234'])
print merge(['012', '013', '023', '123', '124', '134', '234'])
print merge(['012', '013', '014', '023', '024', '034', '123', '124', '134', '234'])
print merge(['012', '013', '023', '123', '124', '134', '234', '0124', '0134', '0234'])
print merge(['012', '013', '023', '123', '124', '134', '234', '1',  '4', '7', '36', '39', '69', '0123456789'])
print merge(['012', '023', '013', '123', '123', '234', '134', '124', '125', '127', '157', '257', '125', '127', '157'])
