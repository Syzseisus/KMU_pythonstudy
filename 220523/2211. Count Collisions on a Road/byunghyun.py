class Solution:
    def countCollisions(self, directions: str) -> int:
        result = 0
        # deque이긴 하지만 왼쪽 요소만 뽑거나 넣기 때문에 실질적으로는 stack으로 활용하게 된다.
        directions = deque(directions)
        # right_count는 R이 연속으로 있는 자동차들의 수를 세었다가 중간에 충돌 지점이 있으면
        # 자동차의 수만큼 충돌 점수를 추가시킨다.
        right_count = 1
        
        # stack의 길이만큼 순회한다.
        for _ in range(len(directions)-1):
            # 먼저 요소 2개를 뽑는다.
            tmp_pop1 = directions.popleft()
            tmp_pop2 = directions.popleft()
            
            # 첫번째 요소가 S일 경우 두번째 요소가 L인 경우에만 점수가 추가된다.
            if tmp_pop1 == 'S':
                if tmp_pop2 == 'L':
                    result += 1
                    directions.appendleft('S')
                else:
                    directions.appendleft(tmp_pop2)
            
            # 첫번째 요소가 R인 경우 두번째 요소가 L인 경우 S인 경우 모두 점수가 추가된다.
            # 단 R이 연속으로 있을 경우를 처리하기 위해 right_count 활용
            elif tmp_pop1 == 'R':
                if tmp_pop2 == 'R':
                    right_count += 1
                    directions.appendleft(tmp_pop2)
                elif tmp_pop2 == 'S':
                    for _ in range(right_count):
                        result += 1
                    right_count = 1
                    directions.appendleft(tmp_pop2)
                else:
                    result += 2
                    for _ in range(right_count - 1):
                        result += 1
                    right_count = 1
                    directions.appendleft('S')
            
            # 첫번째 요소가 L인 경우 점수가 추가될 일이 없음
            else:
                directions.appendleft(tmp_pop2)
                    
        
        return result
                
