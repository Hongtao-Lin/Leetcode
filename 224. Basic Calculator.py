# priority def
p = {
    "*": 1, "/": 1,
    "+": 0, "-": 0
}

# Operator def
def operate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        return num1 // num2

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        def dfs(i):  # "1*2-3/4+5*6"
            res, num = [], 0
            # first flatten the calculation, eliminate '()'
            while i < len(s):
                if s[i] == " ":
                    i += 1
                    continue
                if s[i] == "(":
                    i += 1
                    tmp, i = dfs(i)
                    res.append(tmp)
                elif s[i] == ")":
                    i += 1
                    break
                elif s[i] in "+-*/":
                    res.append(s[i])
                    i += 1
                else:  # digits
                    while i < len(s) and s[i].isdigit():
                        num = 10 * num + int(s[i])
                        i += 1
                    res.append(num)
                    num = 0
            res.append("+")
            # print(res)

            # calculate final number by stack
            stack = [[0, "+"]]
            for j in range(0, len(res), 2):
                num, op = res[j], res[j + 1]
                while stack and p[stack[-1][1]] >= p[op]:
                    num0, op0 = stack.pop()
                    num = operate(num0, num, op0)
                stack.append([num, op])
                # # if p[stack[-1][1]] < 1: # in case: 1-0+2+3
                #     stack.append([num, op])
                # else:
                #     stack[-1] = [operate(stack[-1][0], num, stack[-1][1]), op]
            return stack[-1][0], i
            # res, op = stack[0]
            # for j in range(1, len(stack)):
            #     res = operate(res, stack[j][0], op)
            #     op = stack[j][1]

            # return res, i

        return dfs(0)[0]

s = Solution()
# print(s.calculate("282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024"))
print(s.calculate("1+2*(3)"))