# -*- coding: UTF-8 -*-
import math
import re

# help functions
def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)

def to_string(code):
    """
    transfer binary code to string
    """
    string = ''
    i = 0
    while code > 0:
        if code & 1:
            string += str(i)
        code >>= 1
        i += 1
    return string

def to_code(string):
    """
    transfer string to binary code
    """
    code = 0
    for char in string:
        code += 1 << ord(char) - ord('0')
    # if string == u'986': print string, code
    return code

def bit_count(code):
    """
    count number of 1 in code
    """
    code = (code & 0x5555) + ((code >> 1) & 0x5555)
    code = (code & 0x3333) + ((code >> 2) & 0x3333)
    code = (code & 0x0f0f) + ((code >> 4) & 0x0f0f)
    code = (code & 0x00ff) + ((code >> 8) & 0x00ff)
    return code

def decode(text):
    nums = {}
    value = 0
    for line in re.split(u'[元y]', text)[:-1]:
        # print line.encode('utf-8')
        tmp = re.split(u"[ .=\xa0各g]", line.strip())
        # print tmp
        bases, multi = tmp[:-1], int(tmp[-1])
        for base in bases:
            # if base == '' or len(base) > 3:
            if base == '':
                # print 'skip~', base, multi
                # print tmp
                continue
            value += multi
            nums[base] = nums.get(base, 0) +  multi
    print 'Value:', value
    return nums

def encode(code2num):
    # print code2num
    text = ''
    value_sum = 0
    for code, num in code2num.items():
        # text += code + '=' + str(num) + '元 '
        value_sum += num
    text += '数量' + str(len(code2num))
    text += ' 总值' + str(value_sum) + '元\n'
    
    for k in range(3, 11):
        num2codes = {}
        for code in code2num.keys():
            if len(code) == k:
                if code2num[code] in num2codes:
                    num2codes[code2num[code]].append(code)
                else:
                    num2codes[code2num[code]] = [code]
                del code2num[code]
        # print 'code2num:', code2num
        # print 'num2codes:', num2codes

        # print num2codes.keys()
        code_text = ''
        for num in sorted(num2codes.keys(), reverse = True):
            num2codes[num].sort()
            # print num, num2codes[num]
            for code in num2codes[num]:
                code_text += ' ' + code
            if len(num2codes[num]) == 1:
                code_text += '=' + str(num) + '元'
            else:
                code_text += '各' + str(num) + '元'
        if code_text != '':
            text += code_text.strip() + '\n'

    return text
