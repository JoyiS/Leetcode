# Method 1: Sort and then return the nums[median one]
# The time complexity will be ((m+n)log(m+n))
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    i = 0
    j = 0
    k = 0
    nums = [0] * (len(nums1) + len(nums2))
    while j < len(nums1) and k < len(nums2):
        if nums1[j] <= nums2[k]:
            nums[i] = nums1[j]
            j += 1
        else:
            nums[i] = nums2[k]
            k += 1
        i += 1
    while j < len(nums1):
        nums[i] = nums1[j]
        i += 1
        j += 1
    while k < len(nums2):
        nums[i] = nums2[k]
        i += 1
        k += 1
    if len(nums) % 2:
        return nums[(len(nums) / 2)]
    else:
        return float((nums[int(len(nums) / 2)] + nums[int(len(nums) / 2) - 1]) / 2)

# Method 2: Binary search to improve the time complexity to O(log(m+n))
class Solution(object):
    def getkthmn(self,nums1,nums2,k):
        if len(nums1)>len(nums2):
            return self.getkthmn(nums2,nums1,k)
        if not nums1:
            return nums2[k-1]
        if k==1:
            return min(nums1[0],nums2[0])
        pa = min(k/2,len(nums1))
        pb = k - pa
        if nums1[pa-1]<=nums2[pb-1]:
            return self.getkthmn(nums1[pa:],nums2,k-pa)
        else:
            return self.getkthmn(nums1,nums2[pb:],k-pb)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = (len(nums1)+len(nums2))
        if length % 2:
            self.getkthmn(nums1,nums2,(length-1)/2)
        else:
            1/2*(self.getthmn(nums1,nums2, length/2) + self.getthmn(nums1,nums2, length/2+1))