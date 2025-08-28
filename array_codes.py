import array
# import numpy as np

test_arr= array.array ('i',[1,2,3,4])



# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):  # check pairs
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# print(two_sum([3,5,6,3],9))


def twoSum(self,array,sum):
        lx=len(array)
        for i in range (0,lx):
            for j in range (i+1,lx):
                if array[i] + array[j]==sum:
                               return(f"[{i},{j}]")

print(twoSum(0,[2,3,4,88],5))