### Vanila Problem
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

#### Example 1:

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

#### Example 2:

Input: nums = [2,0,1]

Output: [0,1,2]

#### Example 3:

Input: nums = [0]
Output: [0]

#### Example 4:

Input: nums = [1]
Output: [1]

#### Comments 
This is a classic problem called the Dutch flag problem and it works 
partition items into three parts.

The steps are as follows
- Initiate three pointers small, middle and large
- Start advancing the middle pointer
- If the middle is at the smallest element (in this example 0), 
- swap the current element with the element at the smallest index, advance both the smallest, middle pointers
- if the middle is at the middle element(in this example 1)
- do nothing, element is correctly placed, and advance the middle element pointer
- If the middle element is at the largest element( in this example 2)
- Swap the element at the middle element pointer with the element at the large element pointer
- decrement the largest element point
- Exit loop when exit condition is met