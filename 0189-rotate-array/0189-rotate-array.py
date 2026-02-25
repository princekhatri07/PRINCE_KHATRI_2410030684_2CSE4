class Solution(object):

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums, k):
       
        n = len(nums)
        k = k % n 
#first rotation-->complete array
        self.reverse(nums,0,n-1)
#second rotation --> first k elements
        self.reverse(nums,0,k-1)
#third rotation --> rest of the data rotate
        self.reverse(nums,k,n-1)