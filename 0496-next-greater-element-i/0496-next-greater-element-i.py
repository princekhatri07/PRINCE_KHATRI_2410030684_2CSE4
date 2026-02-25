class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        st = []
        next_greater_element = {}

        for num in nums2:
            while st and st[-1] < num:
                next_greater_element[st.pop()] = num
            st.append(num)

        result = []
        for num in nums1:
            result.append(next_greater_element.get(num, -1))

        return result