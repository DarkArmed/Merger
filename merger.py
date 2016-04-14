from helper import *

N = 1 << 10

class Merger:
    """Code Merger Class"""
    def __init__(self, bases):
        self._codes = {}
        for idx in range(3, 11):
            self._codes[idx] = []
        for code in range(1, N):
            if bit_count(code) >= 3:
                self._codes[bit_count(code)].append(code)
        self._merged = {}
        self._bases = bases
        self.build_pool()

    def get_codes(self, k):
        return self._codes[k]

    def build_pool(self):
        """
        build base code pool
        """
        self._pool = [0] * N
        if isinstance(self._bases, dict):
            for base, num in self._bases.items():
                self._pool[to_code(base)] += num
        elif isinstance(self._bases, list):
            for base in self._bases:
                self._pool[to_code(base)] += 1

    def merge(self, k):
        """
        Find all possible combination of length k
        """
        merged = {}
        if k <= 3:
            for base in range(N):
                if bit_count(base) >= 3 and self._pool[base] > 0:
                    merged[to_string(base)] = self._pool[base]
                    self._pool[base] = 0
            # print 'merged k=', k, merged
            return merged
        full_num = nCr(k, 3)
        for mask in self._codes[k]:
            match = [base for base in self._codes[3] if base & mask == base and self._pool[base] > 0]
            if len(match) == full_num:
                merge_num = min([self._pool[base] for base in match])
                if merge_num > 0:
                    merged[to_string(mask)] = merge_num * full_num
                    for base in match:
                        self._pool[base] -= merge_num
        # print 'merged k:', k, merged
        for code, num in self.merge(k - 1).items():
            if code in merged.keys():
                merged[code] += num
            else:
                merged[code] = num
        return merged

    def merge_result(self, k):
        """
        Solve with max length k
        """
        self.build_pool()
        return self.merge(k)
        if not k in self._merged:
            self.build_pool()
            self._merged[k] = self.merge(k)
        return self._merged[k]
