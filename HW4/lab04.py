from Stack import Stack

def solveMaze(maze,startX,startY):
    s = Stack()
    end = False
    step = 1
    s.push([startX,startY])
    pos = s.peek()
    maze[pos[0]][pos[1]] = step
    while not end:
        pos = s.peek()
        if maze[pos[0]-1][pos[1]] == ' ':
            s.push([pos[0]-1,pos[1]])
            step += 1
            maze[pos[0]-1][pos[1]] = step
        elif maze[pos[0]][pos[1]-1] == ' ':
            s.push([pos[0],pos[1]-1])
            step += 1
            maze[pos[0]][pos[1]-1] = step
        elif maze[pos[0]+1][pos[1]] == ' ':
            s.push([pos[0]+1,pos[1]])
            step += 1
            maze[pos[0]+1][pos[1]] = step
        elif maze[pos[0]][pos[1]+1] == ' ':
            s.push([pos[0],pos[1]+1])
            step += 1
            maze[pos[0]][pos[1]+1] = step
        elif (maze[pos[0]-1][pos[1]] == 'G' or
              maze[pos[0]][pos[1]-1] == 'G' or
              maze[pos[0]+1][pos[1]] == 'G' or
              maze[pos[0]][pos[1]+1] == 'G'):
            return True
        else:
            s.pop()
            if s.isEmpty():
                return False
