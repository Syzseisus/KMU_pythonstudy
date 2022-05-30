# 1. 큐
# queue 쓸 거라 popleft 하려고 deque 사용
from collections import deque

def solution(progresses, speeds):
    # 들어온 list deque로 변환
    progresses = deque(progresses)
    speeds = deque(speeds)
    # 정답 list
    answer = []

    # 비워질 때까지 계속
    while progresses:
        distribute = 0

        # progress 하루치씩 갱신
        for i, s in enumerate(speeds):
            progresses[i] += s

        # 혹시나 여기서 비워질 수도 있으니까 체크
        while progresses:
            # 100 이상된 애들 모두 가져오기
            if progresses[0] >= 100:
                distribute += 1
                progresses.popleft()
                speeds.popleft()
            # 100 안된 거 보이면 빠져나오기
            else:
                break

        # 배포가 0이 아니면 answer에 저장
        if distribute != 0:
            answer.append(distribute)

    return answer
  
  
# 2. 큐 X
'''
걸리는 날: (100 - progress) / speed
근데 결과가 소수일 경우
하루가 더 필요함    ex) 2.3 -> 3
이걸 해주는 게 math.ceil()
'''

import math

def solution(progresses, speeds):
    # 걸리는 날 계산하기
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    # 정답 list
    answer = []
    # 첫 번째 기준은 days[0]임
    curr_day = days[0]
    # 배포되는 수 초기화
    distribute = 0

    # 걸리는 날 탐색
    for day in days:
        # 만약 앞보다 걸리는 날이 적다면 걔까지 배포
        if curr_day >= day:
            distribute += 1
        
        # 아니라면
        else:
            # 그전까지 배포된 거 answer에 넣고
            answer.append(distribute)
            # 1로 초기화: 현재 day 포함해서 배포할 거임
            distribute = 1
            # 걸리는 날 갱신
            curr_day = day
    
    # 마지막 남은 거 붙이기
    answer.append(distribute)
            
    return answer

# 백준 문제
from collections import deque

# std input
N = int(input())

# 1부터 N까지 카드 쌓기
queue = deque([i + 1 for i in range(N)])

# 한 장 남을 때까지 반복
while len(queue) > 1:
    # 1. 맨 위 버림
    queue.popleft()
    # 버려서 한 장 남으면 break
    if len(queue) == 1:
        break
    # 2. 맨 위 뽑아서
    temp = queue.popleft()
    # 3. 맨 아래에 넣음
    queue.append(temp)

# 한 장 남은 거 print
print(queue[0])
