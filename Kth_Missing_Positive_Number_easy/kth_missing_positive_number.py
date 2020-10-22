class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        if not arr:
            return 0

        #Find the missing numbers from the left most element which is 1
        def findMissing(index):
            return arr[index]-1-index
        
        low=0
        high=len(arr)-1
        
        mcnt=findMissing(high)
        
        if mcnt < k:
            return arr[-1]+k-mcnt
        
        while low < high:
            mid = (low + high) // 2
            
            missing = findMissing(mid)
            
            if missing < k:
                low = mid + 1
            else:
                high = mid 
        
        #Once the binary search terminates the low will point to right
        # so find the element from array low -1
        return arr[low-1]+k-findMissing(low-1) 

    
# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         array = []
#         prev = arr[0]
#         if arr[0] != 1:
#             array += range(1, arr[0])
#         for i in range(1,len(arr)):
#             if arr[i] != arr[i-1] + 1:
#                 array += range(prev+1, arr[i])
#             prev = arr[i]
                
#         if array == []:
#             array += range(arr[-1] + 1 , arr[-1] + k + 1)
#         if len(array) < k:
#             if array[-1] + 1 == arr[-1]:
#                 array += range(array[-1] + 2 , array[-1] + k + 1)
#             else:
#                 array += range(array[-1] + 1 , array[-1] + k + 1)
            
        
#         print(array)
#         return array[k-1]
