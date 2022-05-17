class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        open_paren = ['(', '{', '[']
        close_paren = [')', '}', ']']
        
        for elem in s:
            if elem in open_paren:
                my_stack.append(elem)
            else:
                if not my_stack:
                    return False
                else:
                    stored_elem = my_stack.pop()
                    for index in range(len(open_paren)):
                        if stored_elem == open_paren[index]:
                            if elem != close_paren[index]:
                                return False
        
        if not my_stack:
            return True
        
        return False
