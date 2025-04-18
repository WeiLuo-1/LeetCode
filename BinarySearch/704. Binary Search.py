class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1

        while start + 1 < end:
            mid = (end + start) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                return mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
    
if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print(Solution().search(nums, target))

    nums = [-1,0,3,5,9,12]
    target = 2
    print(Solution().search(nums, target))