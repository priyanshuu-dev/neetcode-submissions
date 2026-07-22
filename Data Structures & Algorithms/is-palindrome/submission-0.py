class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for i in range(len(s)):
            if s[i].isalnum():
                cleaned+=s[i]
        cleaned=cleaned.lower()
        low=0
        high=len(cleaned)-1

        while low<=high:
            if cleaned[low]==cleaned[high]:
                low+=1
                high-=1

            else:
                return False

        return True

            

       

           

        

        






        
                



        
        
        

        