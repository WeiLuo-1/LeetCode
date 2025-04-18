class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        width = len(matrix[0])
        length = len(matrix) * width
        start = 0
        end = length - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid//width][mid%width] < target:
                start = mid
            elif matrix[mid//width][mid%width] > target:
                end = mid
            else:
                return True
        
        if matrix[start//width][start%width] == target:
            return True
        if matrix[end//width][end%width] == target:
            return True

        return False
    
if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(Solution().searchMatrix(matrix, target))

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(Solution().searchMatrix(matrix, target))