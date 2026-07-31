class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[0] * len(nums)

        for i in range(len(nums)):

            while stack and nums[i] > nums[stack[-1]]:
                a=stack.pop()

                res[a]=i-a

            stack.append(i)

        return res
        