def solution(A, B):
    
    downStack = [0] * len(A)
    downSize = 0
    
    upAlive = 0
    
    for i in range(-1, -1*(len(A)+1), -1):
        
        if B[i] is 0: 
            downStack[downSize] = A[i]
            downSize += 1
        else: 
            
            if downSize is 0: 
                upAlive += 1
            else: 
                
                while A[i] > downStack[downSize-1]:
                    downSize -= 1
                    if downSize is 0:
                        break
                if downSize is 0:
                    upAlive += 1
    
    return downSize+upAlive