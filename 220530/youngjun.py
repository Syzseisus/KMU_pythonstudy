from collections import deque

def solution(progresses, speeds):
    # progresses와 speeds que를 만들어줌
    progresses_que = deque(progresses)
    speeds_que = deque(speeds)
    # 정답 리스트를 만들어줌
    pop_nums_list = []
    # progresses_que의 원소들이 남아있는 동안
    while progresses_que:
        # 계속해서 작업 진도 추가
        for i in range(len(progresses_que)):
            progresses_que[i] += speeds_que[i]
        # 한번 돌 때마다 몇개의 progresses_que 원소가 pop되었는지
        pop_nums = 0
        # progresses_que 원소가 남아 있고, 첫번째 원소가 0보다 크면 progresses_que와 speeds_que를 계속 pop 해줌, pop_nums에는 1씩 더함
        while progresses_que and progresses_que[0] >= 100:
            progresses_que.popleft()
            speeds_que.popleft()
            pop_nums += 1
        #pop_nums가 0이 아니면 정답 리스트에 추가
        if pop_nums != 0:
            pop_nums_list.append(pop_nums)
    
    return pop_nums_list
