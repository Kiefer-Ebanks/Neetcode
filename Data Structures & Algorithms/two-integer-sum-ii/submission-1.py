class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()

        if self != None:
            i = 0
        if numbers != None:
            j = len(numbers)-1

        found = False

        while found == False:
            if numbers[i] + numbers[j] == target:
                found = True
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        return [i+1,j+1]


        