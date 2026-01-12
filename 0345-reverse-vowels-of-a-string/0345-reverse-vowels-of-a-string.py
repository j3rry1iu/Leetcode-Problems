class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        vowels = ["a", "e", "i", "o", 'u', 'A', "E", 'I', 'O', 'U']
        extract = []
        for i in range(len(string)): 
            if string[i] in vowels: 
                extract.append(string[i])
                string[i] = ""
        extract.reverse()
        j = 0
        for i in range(len(string)):
            if string[i] == "":
                string[i] = extract[j]
                j+=1 
        return "".join(string)
        
        


        