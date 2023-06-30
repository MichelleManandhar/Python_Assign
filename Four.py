# Concatenate any 2 strings to give 
# smallest string from given array of srings
# Example:
# Input: S=[“aab”,”bcddbc”,”aa”,”aazef”]
# Output: “aabaa”


s = ["aab","bcddbc","aa","aazef"]


s2=s[:]

s.sort()


if s[0]==s2[0]:
    print(s[0]+s[1])

else:
    print(s[1]+s[0])

    

