# https://leetcode.com/contest/weekly-contest-185/problems/display-table-of-food-orders-in-a-restaurant/

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        display = {}
        items = set()
        for order in orders:
            table = int(order[1])
            item = order[2]
            items.add(item)
            if table not in display:
                display[table] = {}
            if item not in display[table]:
                display[table][item] = 0
            display[table][item] += 1
        sorted_items = sorted(items)
        ans = [['Table']]
        for item in sorted_items:
            ans[0].append(item)
        for table in sorted(display.keys()):
            ans.append([str(table)])
            for item in sorted_items:
                ans[-1].append(str(display[table].get(item, 0)))
        return ans
