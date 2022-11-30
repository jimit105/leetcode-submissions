# https://leetcode.com/problems/erect-the-fence/discuss/2831393/Python-full-explanation-!

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def compare_slopes(point1, point2, point3):
            x_point1, y_point1 = point1
            x_point2, y_point2 = point2
            x_point3, y_point3 = point3
            
            return ((y_point3 - y_point2) * (x_point2 - x_point1)) - ((y_point2 - y_point1) * (x_point3 - x_point2))
            
            
        trees.sort()
        upper, lower = [], []

        for point in trees:
            while len(upper) > 1 and compare_slopes(upper[-2], upper[-1], point) > 0:
                upper.pop()
            while len(lower) > 1 and compare_slopes(lower[-2], lower[-1], point) < 0:
                lower.pop()

            upper.append(tuple(point))
            lower.append(tuple(point))
            
        return list(set(upper + lower))            
    
