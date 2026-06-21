# 2614. Prime in Diagonal

class Solution:
    def isPrime(self, num):
        if num <= 1:
            return False
        else:
            for i in range(2,int(num**0.5)+1):
                if num%i == 0:
                    return False
            else:
                return True
    def diagonalPrime(self, nums):
        mxpr = 0
        n = len(nums)
        for i in range(len(nums)):
            if self.isPrime(nums[i][i]):
                if nums[i][i] > mxpr:
                    mxpr = nums[i][i]
            if self.isPrime(nums[i][n-i-1]):
                if nums[i][n-i-1] > mxpr:
                    mxpr = nums[i][n-i-1]
        return mxpr
    
obj = Solution()
nums = [[1,2,3],[5,17,7],[9,11,10]]
res = obj.diagonalPrime(nums)
print("~"*15)
print("Output:",res)
print("~"*15)
