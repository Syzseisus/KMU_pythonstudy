'''
1. 자동차의 충돌은 세 가지 경우가 있다.
2. 첫번째로 아무 충돌도 일어나지 않는 경우. 이때는 왼쪽 끝에서 왼쪽으로 가거나, 오른쪽 끝에서 오른쪽으로 가는 경우를 의미한다. 이 경우는 while 문을 통해 pop을 하면서 없애준다.
3. 두번째로 첫번째 경우를 없앴을 때 왼쪽에서 왼쪽, 혹은 오른쪽에서 오른쪽으로 가나 멈춘 자동차에 의해 막혀서 충돌이 일어나는 경우이다.
4. 이때 멈춘 자동차에 의해 발생하는 충돌의 개수는 반대방향이 나오기 전까지의 한쪽 방향으로 가는 자동차의 수라고 볼 수 있다. 마찬가지로 양 끝에서 pop을 하면서 없애준다.
ex) SLLLSLLLR~의 경우, 왼쪽에서부터 탐색을 시작했을 때 R이 나오기 전까지의 충돌의 개수는 L의 총 개수인 6이라고 볼 수 있다. 이때 S의 개수는 상관 없다. 반대방향도 마찬가지이다.
5. 그렇게 모두 없애고 나면 왼쪽에서는 R, 오른쪽에서는 L로 인해 안쪽에서 충돌하는 자동차들만 남는다.
6. 이들의 충돌횟수에 S는 의미가 없다. 예를 들어, RSL과 RL은 각각 1+1 = 2로 같은 것을 알 수 있다.

class Solution:
    def countCollisions(self, directions: str) -> int:
        directions_deque = deque(list(directions))

        while directions_deque and directions_deque[0] == 'L':
            directions_deque.popleft()

        while directions_deque and directions_deque[-1] == 'R':
            directions_deque.pop()

        left_L = []
        right_R = []

        if set(directions_deque) == {'S'}:
            return 0
        elif directions_deque and directions_deque[0] == 'S':
            while directions_deque and directions_deque[0] != 'R':
                if directions_deque[0] == 'S':
                    directions_deque.popleft()
                elif directions_deque[0] == 'L':
                    directions_deque.popleft()
                    left_L.append('L')    
        elif directions_deque and directions_deque[-1] == 'S':
            while directions_deque and directions_deque[-1] != 'L':
                if directions_deque[-1] == 'S':
                    directions_deque.pop()
                elif directions_deque[-1] == 'R':
                    directions_deque.pop()
                    right_R.append('R')

        inside_num = len(directions_deque) - (directions_deque.count('S'))

        return len(left_L) + len(right_R) + inside_num
