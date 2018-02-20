class Solution(object):
    def accountsMerge(self, accounts):

        parent = {}

        def findParent(parent, x, idx):
            if x not in parent:
                parent[x] = [idx]
            else:
                parent[x] += [idx]

        for idx in range(len(accounts)):
            acc = accounts[idx]
            emails = acc[1:]
            for email in emails:  # Union
                findParent(parent, email, idx)

        res = []
        visited = [False for i in range(len(accounts))]
        summary = sorted(parent.items(),key = lambda x: -len(x[1]))
        for email, idxs in summary:
            if visited[idxs[0]]:
                continue
            ems = set()
            for idx in idxs:
                visited[idx] = True
                for em in accounts[idx][1:]:
                    ems.add(em)
            res += [accounts[idx][0],list(ems)]

        return res






