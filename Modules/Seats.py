import numpy as np

def Theatre(r,c):
    m = [] 
    for i in range(r):
        temp = []
        for j in range(c):
            temp.append('S')
        m.append(temp)
    return np.array(m)
def Show_Seats(m):
    print('LAYOUT:\n') 
    r,c = np.shape(m)
    for j in range(c+1):
        print(j,end = ' ')
        
    print('\n')
    for i in range(r):
        print(i+1,*m[i])
    print('\nYour Screen Here')
    print('**********')
