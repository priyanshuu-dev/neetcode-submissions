class Solution(object):
    def groupAnagrams(self, s):
        freq={}
        for i in range(len(s)):
            sortedd="".join(sorted(s[i]))
            if sortedd not in freq:
                freq[sortedd]=[]
                freq[sortedd].append(s[i])

            else:
                freq[sortedd].append(s[i])

        return list(freq.values())
            
                


            

            
  







       
            



      
            


        