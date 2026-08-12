import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        heap=[]
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1

        for num,count in freq.items():
            heapq.heappush(heap,(-count,num))

        ans=[]
        while k:
            a,b=heapq.heappop(heap)
            ans.append(b)
            k-=1
        return ans

        

        