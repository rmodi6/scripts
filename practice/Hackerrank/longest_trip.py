# We would like to encourage passengers to experience the joy of travel using our transit system, therefore we would like to determine the longest path available to advertise to the public. Specifically we would like to determine the longest possible trip on the transit system that will involve two tickets. The destinations must be connected, and all destinations must be unique.
# 
# You will be provided input in the format of CHI:NYC: 719 where CHI Is one location, NYC Is a connected location, and 719 is the distance between the locations.
# 
# One line of output should be provided per line of Input In the format of 3167:CHI:NYC: LA where 3167 is the distance of the trip. CHI is the starting location NYC is the intermediary location, and LA Is the final location.

import fileinput
class PathCalculator:
    
    # You may enter code here.

    def __init__(self):
        self.matrix = None
        self.cityToId = {}
        self.idToCity = []
    
    def process(self, line: str) -> str:
        
        # You must enter code here.
        src, dest, dist = line.split(':')
        dist = int(dist)
        if len(self.cityToId) == 0:
            self.cityToId[src] = 0
            self.cityToId[dest] = 1
            self.idToCity.append(src)
            self.idToCity.append(dest)
            self.matrix = [[0, dist], [dist, 0]]
            return 'NONE'
        else:
            if src not in self.cityToId:
                self.cityToId[src] = len(self.idToCity)
                self.idToCity.append(src)
                rows, cols = len(self.matrix), len(self.matrix[0])
                self.matrix.append([0] * cols)
                for row in self.matrix:
                    row.append(0)
            if dest not in self.cityToId:
                self.cityToId[dest] = len(self.idToCity)
                self.idToCity.append(dest)
                rows, cols = len(self.matrix), len(self.matrix[0])
                self.matrix.append([0] * cols)
                for row in self.matrix:
                    row.append(0)
            srcId, destId = self.cityToId[src], self.cityToId[dest]
            self.matrix[srcId][destId] = dist
            self.matrix[destId][srcId] = dist
            ans = ''
            max_dist = -1
            for i in range(len(self.matrix)):
                for j in range(i, len(self.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        if i != j and j != k and k != i:
                            distance = self.matrix[i][k] + self.matrix[k][j]
                            if distance > max_dist:
                                max_dist = distance
                                temp = sorted([self.idToCity[i], self.idToCity[j]])
                                ans = ':'.join([str(distance), temp[0], self.idToCity[k], temp[1]])
                            elif distance == max_dist:
                                temp = sorted([self.idToCity[i], self.idToCity[j]])
                                if temp[0] < ans.split(':')[1]:
                                    ans = ':'.join([str(distance), temp[0], self.idToCity[k], temp[1]])
            return ans
            

if __name__ == "__main__":
    path_calc = PathCalculator()
    for line in fileinput.input():
        cleaned_line = line.replace("\n", "")
        print(path_calc.process(cleaned_line))