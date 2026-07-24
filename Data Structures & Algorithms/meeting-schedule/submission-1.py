"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, a: List[Interval]) -> bool:

        if len(a)==0:
            return True

        a.sort(key=lambda x: x.start)

        s1=a[0].start
        e1=a[0].end

        for i in range(1, len(a)):
            s2=a[i].start
            e2=a[i].end



            if e1>s2:
                return False
            else:
                e1=max(e1, e2)

        return True
        
