import collections

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        if not formula:
            return ""

        def count(formula, i):
            counter = collections.Counter()
            n = len(formula)
            while i < n:
                if formula[i] == "(":
                    tmp_counter, i = count(formula, i + 1)
                    cnt = 0 # brackets are possibly followed by cnt
                    while i < n and formula[i].isdigit():
                        cnt = 10 * cnt + int(formula[i])
                        i += 1
                    cnt = max(cnt, 1)
                    counter += collections.Counter({k: cnt * v for k, v in tmp_counter.items()})
                    continue
                if formula[i] == ")":
                    return counter, i + 1
                # if not (), get the element and cnt
                ele, cnt = "", 0
                ele += formula[i]
                i += 1
                while i < n and formula[i].isalpha() and formula[i].islower():
                    ele += formula[i]
                    i += 1
                while i < n and formula[i].isdigit():
                    cnt = 10 * cnt + int(formula[i])
                    i += 1
                counter[ele] += max(cnt, 1)
            return counter, i + 1

        res = ""
        for k, v in sorted(count(formula, 0)[0].items()):
            res += k
            if v != 1:
                res += str(v)
        return res


s = Solution()
formula = "K4(ON(SO3)2SMg)2"
s.countOfAtoms(formula)
