# 재귀,next함수 사용
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        if not head:
            return None
        first = head
        
        if not first.next:
            return first  
        
        second = first.next  
        first.next = self.swapPairs(second.next)
        second.next = first
        return second
        
