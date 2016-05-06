class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        input_string = s
        index_start = 0
        index = 0
        #index = index_start
        length = 0
        current_length = length
        substring = []
        current_substring = substring
        flag = 0
        for character in input_string:
            index += 1
            for element in substring:
                if element == character:
                    flag = 1
            if flag == 0:
                substring += character
                length += 1
