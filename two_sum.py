class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum1 = 0
        lst = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum1 = nums[i]+nums[j]
                if sum1 == target:
                    lst.append(i)
                    lst.append(j)
                    # print(f'[i,i+1]')
                    return lst
                else:
                    pass