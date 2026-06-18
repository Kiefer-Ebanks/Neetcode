class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        valid_letters = {}
        for x in s:
            if x not in valid_letters:
                valid_letters[x] = 1
            else:
                valid_letters[x] += 1

        for x in t:
            if x not in valid_letters:
                return False
            else:
                if valid_letters[x] > 0:
                    valid_letters[x] -= 1
                else:
                    return False

            


        return True
        