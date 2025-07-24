
people = {
    "Amogh": 5,
    "Ameya": 10,
    "Grandmother": 20,
    "Grandfather": 25
}

class State:
    def __init__(self, left, right, time_used, umbrella_pos, path=[]):
        self.left = left
        self.right = right
        self.time_used = time_used
        self.umbrella_pos = umbrella_pos
        self.path = path + [self] 
    def is_goal(self):
        return len(self.right) == 4 and self.time_used <= 60

    def __str__(self):
        return f"Left: {self.left} | Right: {self.right} | Time: {self.time_used} min | Umbrella: {self.umbrella_pos}"

    def __eq__(self, other):
        return (sorted(self.left) == sorted(other.left) and
                sorted(self.right) == sorted(other.right) and
                self.time_used == other.time_used and
                self.umbrella_pos == other.umbrella_pos)

    def __hash__(self):
        return hash((tuple(sorted(self.left)), tuple(sorted(self.right)), self.time_used, self.umbrella_pos))

    def moveGen(self):
        moves = []
        if self.umbrella_pos == 'L':
            for i in range(len(self.left)):
                for j in range(i, len(self.left)):
                    p1 = self.left[i]
                    p2 = self.left[j]
                    crossers = [p1] if i == j else [p1, p2]
                    time_needed = max(people[p] for p in crossers)
                    new_time = self.time_used + time_needed

                    if new_time > 60:
                        continue

                    new_left = self.left.copy()
                    new_right = self.right.copy()
                    for p in crossers:
                        new_left.remove(p)
                        new_right.append(p)

                    new_state = State(new_left, new_right, new_time, 'R', self.path)
                    moves.append(new_state)
        else:
            for i in range(len(self.right)):
                p = self.right[i]
                time_needed = people[p]
                new_time = self.time_used + time_needed

                if new_time > 60:
                    continue

                new_left = self.left.copy()
                new_right = self.right.copy()
                new_right.remove(p)
                new_left.append(p)

                new_state = State(new_left, new_right, new_time, 'L', self.path)
                moves.append(new_state)
        return moves



def bfs():
    initial = State(["Amogh", "Ameya", "Grandmother", "Grandfather"], [], 0, 'L')
    frontier = [initial]
    visited = set()

    while frontier:
        current = frontier.pop(0)
        if current.is_goal():
            print("=== BFS Solution ===")
            for step in current.path:
                print(step)
            return

        visited.add(current)
        for child in current.moveGen():
            if child not in visited:
                frontier.append(child)

    print("No BFS solution found within 60 minutes.")



def dfs():
    initial = State(["Amogh", "Ameya", "Grandmother", "Grandfather"], [], 0, 'L')
    stack = [initial]
    visited = set()

    while stack:
        current = stack.pop()
        if current.is_goal():
            print("=== DFS Solution ===")
            for step in current.path:
                print(step)
            return

        visited.add(current)
        for child in reversed(current.moveGen()):  # reverse for DFS behavior
            if child not in visited:
                stack.append(child)

    print("No DFS solution found within 60 minutes.")



bfs()
print()
dfs()
