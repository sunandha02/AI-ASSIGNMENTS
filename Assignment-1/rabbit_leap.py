class State:
    def __init__(self, positions, path=[]):
        self.positions = positions
        self.path = path

    def __str__(self):
        return ''.join(self.positions)

    def is_goal(self):
        return self.positions == ['W', 'W', 'W', '_', 'E', 'E', 'E']

    def moveGen(self):
        moves = []
        pos = self.positions
        for i in range(len(pos)):
            if pos[i] == 'E':
            
                if i + 1 < 7 and pos[i + 1] == '_':
                    new_pos = pos.copy()
                    new_pos[i], new_pos[i + 1] = new_pos[i + 1], new_pos[i]
                    moves.append(State(new_pos, self.path + [new_pos]))

                
                if i + 2 < 7 and pos[i + 2] == '_' and pos[i + 1] in ['E', 'W']:
                    new_pos = pos.copy()
                    new_pos[i], new_pos[i + 2] = new_pos[i + 2], new_pos[i]
                    moves.append(State(new_pos, self.path + [new_pos]))

            elif pos[i] == 'W':
            
                if i - 1 >= 0 and pos[i - 1] == '_':
                    new_pos = pos.copy()
                    new_pos[i], new_pos[i - 1] = new_pos[i - 1], new_pos[i]
                    moves.append(State(new_pos, self.path + [new_pos]))

                
                if i - 2 >= 0 and pos[i - 2] == '_' and pos[i - 1] in ['E', 'W']:
                    new_pos = pos.copy()
                    new_pos[i], new_pos[i - 2] = new_pos[i - 2], new_pos[i]
                    moves.append(State(new_pos, self.path + [new_pos]))
        return moves



def bfs():
    initial = State(['E', 'E', 'E', '_', 'W', 'W', 'W'], path=[['E', 'E', 'E', '_', 'W', 'W', 'W']])
    frontier = [initial]  
    visited = set()

    index = 0
    while index < len(frontier): 
        current = frontier[index]
        index += 1

        if current.is_goal():
            print("Solution Path (BFS):")
            for step in current.path:
                print(''.join(step))
            return

        visited.add(str(current))
        for child in current.moveGen():
            if str(child) not in visited:
                frontier.append(child)

    print("No solution found using BFS.")



def dfs():
    initial = State(['E', 'E', 'E', '_', 'W', 'W', 'W'], path=[['E', 'E', 'E', '_', 'W', 'W', 'W']])
    stack = [initial]
    visited = set()

    while stack:
        current = stack.pop()  
        if current.is_goal():
            print("Solution Path (DFS):")
            for step in current.path:
                print(''.join(step))
            return

        visited.add(str(current))
        for child in reversed(current.moveGen()):  
            if str(child) not in visited:
                stack.append(child)

    print("No solution found using DFS.")


if __name__ == "__main__":
    print("=== BFS ===")
    bfs()

    print("\n=== DFS ===")
    dfs()
