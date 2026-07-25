class Solution:
    def eraseOverlapIntervals(self, a: List[List[int]]) -> int:
        a.sort()
        s1=a[0][0]
        e1=a[0][1]
        count=0

        for i in range(1,len(a)):
            s2=a[i][0]
            e2=a[i][1]

            if e1>s2:
                count+=1
                e1=min(e1,e2)
            else:
                e1=e2

        return count
        