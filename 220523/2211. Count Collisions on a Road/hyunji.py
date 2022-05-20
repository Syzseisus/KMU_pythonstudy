class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = [directions[0]]
        collision = 0
                
        for i in range(1, len(directions)):
            
            car = stack[-1] + directions[i]
            # opposite direction
            if car == 'RL':
                collision += 2
                stack.pop()
                
                # 이전 위치에서 R 방향으로 오던 차들도 줄줄이 다 충돌남
                while stack and stack[-1] == 'R':
                    collision += 1
                    stack.pop()
                
                # 충돌하면 staying 상태가 되기 때문에 'S'를 추가
                stack.append('S')
            
            elif car == 'RS':
                collision += 1
                stack.pop()
                
                # 차의 방향이 'S' 인 경우, 이전에 'R' 방향으로 오는 차들과 충돌함
                while stack and stack[-1] == 'R':
                    collision += 1
                    stack.pop()
                    
                stack.append('S')
                
            elif car == 'SL':
                collision += 1
                stack.pop()
                stack.append('S')
                
            else:
                stack.append(directions[i])
                
        return collision
                
                
