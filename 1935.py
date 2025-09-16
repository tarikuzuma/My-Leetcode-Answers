class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        listofwords = text.split(" ")
        brokenletters = list(brokenLetters)
        for i in range (len(brokenletters)):
            for j in range(len(listofwords)-1, -1, -1):
                if brokenletters[i] in listofwords[j]:
                    listofwords.pop(j)
        return len(listofwords)
