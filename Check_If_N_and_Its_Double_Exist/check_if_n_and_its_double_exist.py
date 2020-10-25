class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, n in enumerate(arr): 
            for m in arr[i+1:]:
                if m == n * 2 or m == n / 2: return True 
            
        return False

