class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to hold matching pairs
        matching_brackets = {')': '(', '}': '{', ']': '['}
        
        # Stack to store opening brackets
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            # If it's a closing bracket
            if char in matching_brackets:
                # Pop the top element from the stack if there is one, else use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                # Check if the top element matches the corresponding opening bracket
                if matching_brackets[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets are matched; otherwise, return False
        return not stack








    



  

