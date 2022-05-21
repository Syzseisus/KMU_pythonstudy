'''
인덱스 0번부터 stack에 하나씩 넣을 때,
충돌이 일어나는 경우는 stack 마지막에 있는 애가 R인 경우와, S인 경우가 있다.

1. R인 경우
  1) 다음 L: 2번
  2) 다음 S: 1번

2. S인 경우
  1) 다음 L: 1번

3. 나머지: 충돌 일어나지 않으므로 그냥 넣으면 된다

추가로, 충돌 후에는 S로 바뀌는 걸 주의해야한다
'''

class Solution:
    def countCollisions(self, directions):
        collisions = 0
        stack = []

        for car in directions:
            # stack에 넣기
            if not stack:
                stack.append(car)

            # 1-1
            elif stack[-1] == "R" and car == "L":
                collisions += 2
                stack.pop()
                # L은 왼쪽의 모든 R들과 부딪힐 것이다.
                while stack and stack[-1] == "R":
                    collisions += 1
                    stack.pop()
                stack.append("S")
            
            # 1-2
            elif stack[-1] == "R" and car == "S":
                collisions += 1
                stack.pop()
                # S 또한 왼쪽의 모든 R들과 부딪힐 것이다.
                while stack and stack[-1] == "R":
                    collisions += 1
                    stack.pop()
                stack.append("S")
            
            # 2-1
            elif stack[-1] == "S" and car == "L":
                collisions += 1
                stack.append("S")
            
            # 3
            else:
                stack.append(car)


        return collisions
