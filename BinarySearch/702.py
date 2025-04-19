# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#     def get(self, index: int) -> int:


class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        start, end = 0, 1
        while reader.get(end) < target:
            start = end
            end *= 2

        while start + 1 < end:
            mid = (start + end) // 2
            val = reader.get(mid)
            if val < target:
                start = mid
            elif val > target:
                end = mid
            else:
                return mid
            
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        
        return -1
    
if __name__ == "__main__":
   