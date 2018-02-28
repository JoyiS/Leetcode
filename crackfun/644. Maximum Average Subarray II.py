'''
Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.
'''
'''
// Time Complexity : O(n*log(maxval - minvl))  Java code
public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double max = Double.MIN_VALUE;
        double min = Double.MAX_VALUE;

        // 寻找最值
        for (int n: nums) {
            max = Math.max(max, n);
            min = Math.min(min, n);
        }

        double last_mid = max, error = Integer.MAX_VALUE;
        while (max-min > 0.00001) {
            double mid = (max + min) / 2.0;
            if (check(nums, mid, k))
                min = mid;
            else
                max = mid;
            error = Math.abs(last_mid - mid);
            last_mid = mid;
        }
        return min;
    }


    // 判断这个区间里面，是否有一段大于等于K的长度的最长序列，满足要求，就是最大的累计和，减去最小的累积和
    public boolean check(int[] nums, double mid, int k) {
        double sum = 0, prev = 0, min_sum = 0;
        for (int i = 0; i < k; i++)
            sum += nums[i] - mid;
        if (sum >= 0)
            return true;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - mid;
            prev += nums[i - k] - mid;
            min_sum = Math.min(prev, min_sum); // It is important to keep the min value of the previous sum, so this means the array with length greater than or equal to K have >=0 sum
            if (sum >= min_sum)
                return true;
        }
        return false;
    }
}
'''