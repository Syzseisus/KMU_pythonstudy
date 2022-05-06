# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swap(self, LN):
        # 4) 종료 조건:
        #    - 진행하다가 들어온 게 없어서 -> 바꿀 게 없거나
        #    - 두 번째 값이 없어서 -> 바꿀 필요가 없으면
        if (LN == None) or (LN.next) == None: return

        # LN.val은 첫 번째 값,
        # LN.next.val은 두 번째 값을 뜻함
        
        # 1) 그 둘의 자리를 바꾸고
        LN.val, LN.next.val = LN.next.val, LN.val

        # 2) 그 두 개 건너 뛰고 나머지에 대해
        LN = LN.next.next
        
        # 3) swap 진행
        self.swap(LN)

    def swapPairs(self, head):
        self.swap(head)
        return head
