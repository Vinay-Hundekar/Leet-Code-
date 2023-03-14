class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # Spliting the given string into list of words
        w=s.split()
        # If no of words in string is not equal to no of letters in pattern
        # Than return False
        if len(w) != len(pattern):
            return False
        # Creating a pdict(pattern dictionary)
        # Where key are letters and values are words
        pdict={}
        # Extracting each word and letters
        for word,letter in zip(w,pattern):
            # If word is already present in pdict but it is mapped to another letter
            # Than return False
            if word in pdict.values() and letter not in pdict:
                return False
            # If letter is not there in pdict than map it with coresponding word
            pdict.setdefault(letter,word)
            # If word not in pdict[letter], than return False
            # Means if letter is already mapping to other word
            if word not in pdict[letter]:
                return False
        return True