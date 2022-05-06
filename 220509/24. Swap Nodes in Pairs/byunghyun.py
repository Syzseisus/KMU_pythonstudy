# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solution(self, head):
        # 재귀를 하다가 head가 None인 경우, head 다음이 None인 경우, Head 다다음이 None인경우
        # swap을 하다가 하나 이하가 남는다면 그건 처리 X입니다.
        if head == None or head.next == None or head.next.next == None:
            return
        
        # 반면 뒤에 swap 대상이 있다면
        # 우선 swap 대상을 저장해줍니다.
        # 2-1-3-4-5-6 이 들어왔고, head가 1을 가르키고 있는 경우
        # tmp에는 5가 저장됩니다.
        tmp = None
        if head.next.next != None:
            tmp = head.next.next.next
        # 2-1-3-4-5-6에서 3과 4의 자리를 교환해줍니다.
        head.next, head.next.next = head.next.next, head.next
        # 그 다음 3에 5를 연결하여
        # 2-1-4-3-5-6을 만들어 줍니다.
        head.next.next.next = tmp
        # 그 다음 3을 재귀함수의 head로 넣어줍니다.
        self.solution(head.next.next)
    
    
    # 전체적인 코드는 1-2-3-4-5-6을 예시로 들겠습니다.
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 만약 head가 None이거나 하나짜리라면 계산할 필요가 없습니다.
        if head == None or head.next == None:
            return head
        
        # 3을 tmp로 저장합니다.
        tmp = head.next.next
        # 1과 2를 바꿉니다.
        head, head.next = head.next, head
        # tmp를 연결하여 2-1-3-4-5-6짜리 연결 리스트를 만듭니다.
        head.next.next = tmp
        # 만약 두 개짜리 연결리스트거나 3개짜리라면 더 이상 계산할 필요가 없습니다.
        if tmp != None:
            if tmp.next != None:
                # 하지만 3개를 초과하는 연결리스트라면 계산을 해야 합니다.
                # 2-1-3-4-5-6에서 1을 재귀함수에 넣어줍니다.
                self.solution(head.next)
        return head
