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
