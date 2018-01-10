import bisect

# Wrong Answer, but don't know where I did wrong

class RangeModule(object):
    def __init__(self):
        self.lefts, self.rights = [], []

    def addRange(self, left, right):
        l, r = bisect.bisect_left(self.rights, left), bisect.bisect(self.lefts, right)
        if l == len(self.lefts) or r == 0:
            p = r if not r else l
            self.lefts.insert(p, left)
            self.rights.insert(p, right)
            return
        self.lefts = self.lefts[:l] + [min(left, self.lefts[l])] + self.lefts[r:]
        self.rights = self.rights[:l] + [max(right, self.rights[r - 1])] + self.rights[r:]

    def queryRange(self, left, right):
        if not self.lefts:
            return False
        l, r = bisect.bisect(self.lefts, left) - 1, bisect.bisect_left(self.rights, right)
        print(l, r)
        return 0 <= l == r < len(self.lefts) and self.lefts[l] <= left and self.rights[r] >= right

    def removeRange(self, left, right):
        if not self.lefts:
            return
        left, right = max(left, self.lefts[0]), min(right, self.rights[-1])
        if left >= right:
            return False
        l, r = bisect.bisect(self.lefts, left) - 1, bisect.bisect_left(self.rights, right)
        lefts, rights = [], []
        if self.lefts[l] != left:
            lefts.append(self.lefts[l])
            rights.append(left)
        if self.rights[r] != right:
            lefts.append(right)
            rights.append(self.rights[r])
        self.lefts[l:r + 1], self.rights[l:r + 1] = lefts, rights

    def print(self):
        print(list(zip(self.lefts, self.rights)))

mod = RangeModule()
mod.addRange(10, 200)
mod.addRange(250, 500)
# mod.removeRange(14, 16)
mod.print()
print(mod.queryRange(50, 100))
# mod.removeRange(1, 10)
# mod.removeRange(16, 17)