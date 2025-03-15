class Solution:
    def getSecondLargest(self, arr):
        arr.remove(max(arr))
        large=arr[0]
        for num in arr:
            if num >large:
                large=num
                return num
            return -1
s1=Solution
arr=[12,35,1,10,34,1]
print(s1.getSecondLargest(arr))