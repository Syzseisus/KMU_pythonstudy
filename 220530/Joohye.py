from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    # deque 사용
    deq = deque()  \

    for i in range(len(progresses)):
        # 작업에 필요한 ~일 = 100 % - 작업진도 / 작업속도 
        day = (100 - progresses[i]) / speeds[i]
        # 배포는 하루의 끝에 이루어지므로
        if day % 1 != 0:
            # 하루의 중간에 끝나더라도 끝부분에 배포되므로 +1
            day = math.floor(day) + 1
        deq.append(int(day))
        
    while deq:
        val = deq.popleft() 
        print(val)
        cnt = 1

        while deq:
            d = deq.popleft()
            print(d)
            # 앞 기능이 바로 뒤 기능보다 개발기간이 짧다면
            if d > val:
                # 다시 append.
                deq.appendleft(d)
                break
            cnt += 1
        answer.append(cnt)
    return answer
