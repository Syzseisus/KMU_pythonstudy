# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 두 개씩 짝지어서 swap 해주는 방식
# 예를 들어 [1, 2, 3, 4] 의 경우, 2 -> 1 , 1 - > 4 를 가르키도록 바꿔줌
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap_pairs(head):
            
            # base case
            if (head == None) or (head.next == None):
                return head
            
            # swap
            tmp = head.next.next 
            # head를 바꾸기 이전에 미리 저장
            head2 = head.next 
            head.next.next = head 
            head.next = swap_pairs(tmp)    
            return head2
        
        return swap_pairs(head)
