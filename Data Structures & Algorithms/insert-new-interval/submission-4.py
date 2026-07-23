class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a=[]
        inserted=False

        for i in range(len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]
            if inserted==False and start>=newInterval[0]:
                a.append(newInterval)
                inserted=True
            
            a.append([start,end])

        if inserted==False:
            a.append(newInterval)

        start1=a[0][0]
        end1=a[0][1]

        result=[]

        for i in range(1,len(a)):
            start2=a[i][0]
            end2=a[i][1]

            if end1>=start2:
                end1=max(end1,end2)
            else:
                result.append([start1,end1])
                start1=start2
                end1=end2
        result.append([start1,end1])
        return result


       

        
                
                


        
