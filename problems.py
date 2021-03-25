
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        
        
#         given 2 strings check if the strings have the same letters 
#         if they do return True else Return False
#         need to loop through all the letters in string 1 one and see if they match all the letter in string 2 


        
#         if count of letters in n == letter in t = count == True 
        
#         key = letter 
#         value = number of time that letter is in the string 
        
        number_dict = {}
        number_dict_2 = {}
        
        
        for n in s:
            if n in number_dict:
                number_dict[n] = number_dict[n] + 1 
            else:
                number_dict[n] = 1 
                
        for o in t:
            if o in number_dict_2:
                number_dict_2[o] = number_dict_2[o] + 1 
            else:
                number_dict_2[o] = 1 
        if number_dict == number_dict_2:
            return True  
        else:    
            return False
               