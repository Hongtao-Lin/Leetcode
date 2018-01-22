'''Ideas:
Construct a dict of dict, recording the cnt of tickets from i to j
Order the places by its string order and perform dfs with this order

Better idea: can be greedy:
maintain a heap for each destination, and deterministically go from a to b
via the smallest arrival port available

'''
import collections

class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(path):
            if len(path) == n + 1:
                return True
            i = path[-1]
            for j in sorted(matrix[i]):
                if matrix[i][j]:
                    matrix[i][j] -= 1
                    path.append(j)
                    if dfs(path):
                        return True
                    path.pop()
                    matrix[i][j] += 1
            return False

        id2place = list(set(sum(tickets, [])))
        id2place.sort()
        place2id = {p: i for i, p in enumerate(id2place)}
        n = len(tickets)
        matrix = collections.defaultdict(dict)
        for a, b in tickets:
            i, j = place2id[a], place2id[b]
            if j not in matrix[i]:
                matrix[i][j] = 0
            matrix[i][j] += 1

        path = [place2id['JFK']]
        dfs(path)

        return [id2place[p] for p in path]


s = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
s.findItinerary(tickets)
