class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        target_start=newInterval[0]
        target_end=newInterval[1]

        inserted=False

        for i in range(len(intervals)):
            if intervals[i][0] > target_start:
                intervals.insert(i, [target_start, target_end])
                inserted = True
                break

        if not inserted:
            intervals.append([target_start,target_end])

        result=[]

        if len(intervals)==0:
            return [newInterval]

        start1=intervals[0][0]
        end1 =intervals[0][1]

        for i in range(1,len(intervals)):
            start2=intervals[i][0]
            end2=intervals[i][1]

            if end1>=start2:
                end1=max(end1, end2)
            else:
                result.append([start1, end1])
                start1=start2
                end1=end2

        result.append([start1,end1])

        return result

       

        
                
                


        
