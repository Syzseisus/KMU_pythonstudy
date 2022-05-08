# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swap(self, head):
        # 두 칸씩 이동하며 swap 진행
        # 종료 조건 : 앞의 두 칸에 아무것도 없을 경우
        if head == None or head.next == None:
            # head return : None
            return head
        else:
            # 앞의 두칸에 노드가 있는 경우
            second = head.next
            head.next = self.swapPairs(second.next)
            # head.next를 second에 붙히고
            second.next = head
            # second.next를 head에 붙히면 된다.
            return second
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.swap(head)
    
## 호출 순서는 다음과 같다
## 1 -> 2 -> 3 -> 4
## 3 -> 4 호출 까지 재귀적으로 가고 
## head가 4.next일 때 None return
## head가 3인 상황에서 head(3).next = none, second(4).next = head(3) 이 된다. 그리고 return second(4 -> 3)
## head가 1인 상황에서 head(1).next = second(4 -> 3), second(2).next = head(1 -> 4 ->3)
## 그러면 이쁘게 2 -> 1 -> 4 -> 3이 형성된다.
