class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i in range(len(arr)):
            if arr[i] == 0:
                arr.insert(i+1, 0)
                i += 2
                arr.pop()
            else:
                i += 1
                           
        return None
