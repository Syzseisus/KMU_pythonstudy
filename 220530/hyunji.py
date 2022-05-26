def solution(progresses, speeds):
    answer = []
    
    while progresses:
        cnt = 0
        
        # 하루치 작업 진도 update
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        while progresses:
            # 만약 제일 먼저 배포되어야 하는 작업의 진도가 완료된 경우
            if progresses[0] >= 100:
                cnt += 1
                progresses.pop(0)
                speeds.pop(0)
            else: 
                # print(progresses)
                break
        
        # 한번에 배포되는 기능의 수를 정답 배열에 append
        if cnt != 0:        
            answer.append(cnt)
            
    return answer
