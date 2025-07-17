# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
def solution(board, moves):
    stack = [[] for _ in range(len(board))]
    
    for row in board:
        for j in range(len(row)):
            if row[j] != 0:
                stack[j].append(row[j])
            
    result = []
    answer = 0
    for move in moves:
        if stack[move-1]:
            if result and result[-1] == stack[move-1][0]:
                result.pop()
                answer += 2
            else:
                result.append(stack[move-1][0])
            stack[move-1].pop(0)
        
    return answer