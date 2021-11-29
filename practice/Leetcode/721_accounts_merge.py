# https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        hmap = {}
        for account in accounts:
            name, emails = account[0], set(account[1:])
            if name not in hmap:
                hmap[name] = [emails]
            else:
                parent = -1
                for i, emailSet in enumerate(hmap[name]):
                    if len(emails.intersection(emailSet)) > 0:
                        if parent > -1:
                            hmap[name][parent] = hmap[name][parent].union(emailSet)
                            hmap[name][i] = set()
                        else:
                            hmap[name][i] = emails.union(emailSet)
                            parent = i
                if parent == -1:
                    hmap[name].append(emails)
        ans = []
        for name, emailSets in hmap.items():
            for emailSet in emailSets:
                if len(emailSet) > 0:
                    ans.append([name] + sorted(list(emailSet)))
        
        return ans
