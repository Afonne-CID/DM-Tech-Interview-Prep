'''
    Contains Duplicate
    Category	Difficulty	Likes	Dislikes
    algorithms	Easy (61.24%)	8962	1136
    Tags
    Companies
    airbnb | palantir | yahoo

    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #First approach: Bruteforce
        hash_nums = {}
        for index, value in enumerate(nums):
            if value in hash_nums:
                return True
            hash_nums[value] = index
        return False

        #Second approach: Sort and compare
        def merge(arr, left, middle, right):
            left_arr, right_arr = arr[left:middle+1], arr[middle+1:right+1]
            index, left_p, right_p = left, 0, 0

            while left_p < len(left_arr) and right_p < len(right_arr):
                if left_arr[left_p] <= right_arr[right_p]:
                    arr[index] = left_arr[left_p]
                    left_p += 1
                else:
                    arr[index] = right_arr[right_p]
                    right_p += 1
                index += 1
            while left_p < len(left_arr):
                nums[index] = left_arr[left_p]
                left_p += 1
                index += 1
            while right_p < len(right_arr):
                nums[index] = right_arr[right_p]
                right_p += 1
                index += 1

        def merge_sort(arr, left, right):
            if (left == right):
                return arr
            
            middle = (left + right) // 2
            merge_sort(arr, left, middle)
            merge_sort(arr, middle+1, right)
            merge(arr, left, middle, right)

            return arr

        merge_sort(nums, 0, len(nums) - 1)
        for index in range(1, len(nums)):
            if nums[index] == nums[index-1]:
                return True
        return False