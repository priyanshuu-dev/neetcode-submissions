class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:
        heap=[]

        for i in range(len(nums)):
            heapq.heappush(heap,-nums[i])

        while len(heap)>1:
            a=-heapq.heappop(heap)
            b=-heapq.heappop(heap)

            if a!=b:
                res=a-b

                heapq.heappush(heap,-res)

        if heap:
            return -heapq.heappop(heap)
        else:
            return 0

        


        