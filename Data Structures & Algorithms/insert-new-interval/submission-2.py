class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        target_start=newInterval[0]
        target_end=newInterval[1]

        for i in range(len(intervals)):
            start=intervals[i][0]

            if start>target_start:
                intervals.insert(i,[target_start,target_end])
                break
            else:
                intervals.append([target_start,target_end])
            


        result=[]

        
        if len(intervals)>0:
            start1=intervals[0][0]
            end1=intervals[0][1]

            for i in range(len(intervals)):
                start2=intervals[i][0]
                end2=intervals[i][1]

                if end1>=start2:
                    end1=max(end1,end2)

                else:
                    result.append([start1,end1])
                    start1=start2
                    end1=end2
            result.append([start1,end1])

        else:
            result.append(newInterval)
        return result


       

        
                
                


        
