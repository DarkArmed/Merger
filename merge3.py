from random import choice as rand_choice
from timeit import timeit
from nCr import nCr

N = 1 << 10

# help functions
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

class Pool:

    def __init__(self, nums):
        self._codes = {}
        for idx in range(3, 11):
            self._codes[idx] = []
        for code in range(1, N):
            if bit_count(code) >= 3:
                self._codes[bit_count(code)].append(code)
        self._merged = {}
        self._nums = nums
        self.build_pool()

    def get_codes(self, k):
        return self._codes[k]

    def build_pool(self):
        self._pool = [0] * N
        for num in self._nums:
            self._pool[to_code(num)] += 1

    def merge(self, k):
        merged = []
        if k <= 3:
            for base in range(N):
                for dummy_i in range(self._pool[base]):
                    merged.append(to_string(base))
                self._pool[base] = 0
            # print 'merged k=', k, merged
            return merged
                    
        full_num = nCr(k, 3)
        for mask in self._codes[k]:
            match = [base for base in self._codes[3] if base & mask == base and self._pool[base] > 0]
            if len(match) == full_num:
                merge_num = min([self._pool[base] for base in match])
                if merge_num > 0:
                    for dummy_i in range(merge_num):
                        merged.append(to_string(mask))
                    for base in match:
                        self._pool[base] -= merge_num
        # print 'merged k=', k, merged
        return merged + self.merge(k - 1)

    def merge_result(self, k):
        self.build_pool()
        if not self._merged.has_key(k):
            self._merged[k] = self.merge(k)
        return self._merged[k]


def test(test_case):
    pool = Pool(test_case)
    codes = pool.get_codes(3)

    for k in range(10, 9, -1):
        value_sum = 0
        for code in pool.merge_result(10):
            value_sum += nCr(len(code), 3)
        print 'k =', k, ', merged:', len(pool.merge_result(k)), ', value sum:', value_sum
        print pool.merge_result(k)

    
TEST_CASES = [
                ['012', '013', '023', '123'],
                ['012', '013', '023', '124', '134', '234'],
                ['012', '013', '023', '123', '124', '134', '234'],
                ['012', '013', '023', '123', '123', '124', '134', '234'],
                ['012', '013', '014', '023', '024', '034', '123', '124', '134', '234'],
                ['012', '023', '013', '123', '123', '234', '134', '124', '125', '127', '157', '257', '125', '127', '157'],
                ['012', '023', '013', '123', '123', '234', '134', '124', '125', '125', '127', '157', '257', '125', '127', '157'],
             ]

codes = Pool([]).get_codes(3)
print len(codes)
case = TEST_CASES[0]
case = [to_string(rand_choice(codes)) for dummy_i in range(10000)]
# case = TEST_CASES[3] * 10
# case = TEST_CASES[0] + TEST_CASES[4]
# case = TEST_CASES[6]

print str(timeit('test(case)', 'from __main__ import test, case', number=1)) + 's used.'

