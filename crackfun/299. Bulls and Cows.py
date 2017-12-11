class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        countA = 0
        countB = 0
        i = 0
        while i < len(secret):
            if secret[i] == guess[i]:
                countA += 1
                secret = secret[:i] + secret[i + 1:]
                guess = guess[:i] + guess[i + 1:]
            else:
                i += 1

        for i in range(len(secret)):
            if secret[i] in guess:
                index = guess.index(secret[i])
                guess = guess[:index] + guess[index + 1:]
                countB += 1

        return str(countA) + 'A' + str(countB) + 'B'

