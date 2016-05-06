class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        input_string = s
        index_start = 0
        max_index = 0
        max_length = 0
        #index = index_start
        length = 0
        current_length = 0
        substring = ''
        current_substring = ''
        flag = 0
        while len(input_string)>0:
            for character in input_string:
                if current_substring.find(character) != -1:
                    flag = 1
                if flag == 0:
                    current_substring += character
                    current_length += 1
                if flag == 1:
                    length = current_length
                    current_length = 0
                    substring = current_substring
                    current_substring = ''
                    flag = 0
                    if max_length < length:
                        max_length = length
                        #max_index = i
                    break
            input_string=input_string[1:]
        return max_length
