from collections import deque

def solution(progresses, speeds):
    answer = []
    # 작업이 끝나는 날을 기록할 큐를 생성한다.
    my_queue = deque()
    # 작업과 작업 스피드를 보고 작업이 끝나는 날을 계산하여 큐에 넣는다.
    for index in range(len(progresses)):
        # 작업이 딱 맞게 끝나지 않는 경우도 있기 때문에 올림 연산을 진행한다.
        remain_day = round((100 - progresses[index])/speeds[index] + 0.49999)
        my_queue.append(remain_day)
    
    # work_count는 누적되는 작업개수
    work_count = 1
    # 제일 첫 요소를 뽑아서 last_distribute_date 변수로 저장
    last_distribute_date = my_queue.popleft()
    
    # 이제 큐에서 요소를 하나씩 뽑아보자
    for _ in range(len(my_queue)):
        # 큐에서 뽑은 요소를 임시로 저장
        tmp = my_queue.popleft()
        # 만약 앞선 배포일보다 작거나 같은 날짜가 뽑히게 된다면
        if last_distribute_date >= tmp:
            # 작업 개수를 하나 증가
            work_count += 1
        # 반면 앞선 배포일보다 큰 날짜가 뽑히게 되면
        # 현재 작업 개수를 결과에 추가하고
        # 작업 개수와 배포일을 갱신
        else:
            answer.append(work_count)
            work_count = 1
            last_distribute_date = tmp
        
        # 만약 큐가 비어있는 경우 그냥 현재 작업 상태를 결과에 추가
        if not my_queue:
            answer.append(work_count)
        
    return answer
