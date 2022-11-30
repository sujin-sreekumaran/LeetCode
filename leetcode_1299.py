class Solution(object):
    def replaceElements(self, arr):
        #initial-max = -1
        #And the last element arr[] will be the value of arr[n-1] position
        #iterate the arr through reverse order
        #everytime new max val will be the oldmax and previous arr[i]
        
        right = -1
        for i in range(len(arr) - 1,-1,-1):
            newMaxValue = max(right,arr[i])
            arr[i] = right
            right = newMaxValue
        return arr
