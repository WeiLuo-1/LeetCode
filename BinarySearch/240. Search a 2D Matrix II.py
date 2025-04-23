# Time Complexity: O(m log n)
# Space Complexity: O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in range(len(matrix)):
            if matrix[row][-1] < target:
                continue
            else:
                l = 0
                r = len(matrix[row])-1
                while r >= l:
                    mid = (l+r) // 2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
        return False

if __name__ == "__main__":
    solution = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    print(solution.searchMatrix(matrix, target))  # Output: True

    target = 20
    print(solution.searchMatrix(matrix, target))  # Output: False