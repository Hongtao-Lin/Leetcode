class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        n = len(expression)

        def get_num(arg, d):
            if isinstance(arg, int) or arg[0].isdigit():
                return int(arg)
            while not isinstance(arg, int):
                arg = d[arg]
            return arg

        def get_arg(i, d):
            while expression[i] == " ":
                i += 1
            if expression[i] == "(":
                return dfs(i + 1, d)
            a = ""
            while i < n and expression[i] not in " )":
                a += expression[i]
                i += 1
            if not a[0].isalpha():
                return int(a), i + bool(expression[i] == " ")
            return a, i + bool(expression[i] == " ")

        def dfs(i, od):
            d = od.copy()
            res = 0
            while True:
                if not expression[i]:
                    i += 1
                elif expression[i:].startswith("add"):
                    i += 4
                    a, i = get_arg(i, d)
                    b, i = get_arg(i, d)
                    res = get_num(a, d) + get_num(b, d)
                elif expression[i:].startswith("mult"):
                    i += 5
                    a, i = get_arg(i, d)
                    b, i = get_arg(i, d)
                    res = get_num(a, d) * get_num(b, d)
                elif expression[i:].startswith("let"):
                    i += 4
                    # print(expression[i])
                    while True:
                        a, i = get_arg(i, d)
                        if expression[i] == ")":
                            break
                        b, i = get_arg(i, d)
                        d[a] = b
                    # final expr
                    # print(d)
                    # a, i = get_arg(i, d)
                    res = get_num(a, d)
                elif expression[i] == ")":
                    return res, i + 1
        return dfs(1, {})[0]


s = Solution()
expr = "(let x 2 (add (let x 3 (let x 4 x)) x))"
res = s.evaluate(expr)
print(res)