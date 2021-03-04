import numpy as np

def Ticket_Price(rows,columns,r):    
    if rows*columns <= 60:
        TP = 10
    else :
        if r < (rows/2) :
            TP = 10
        else :
            TP = 8
    return TP

def Total_Income(m):
    r,c = np.shape(m)
    if r*c <= 60:
        TI = r*c*10
    else :
        TI = ((r//2)*10)*c + ((r-(r//2))*8)*c
    return TI        
            
            
def Show_Stats(m):
    B = np.array([])
    r,c = np.shape(m)
    for i in range(r):
        for j in range(c):
            if m[i][j] == 'B' :
                B = np.append(B,i)
                
    P = np.array([])
    for i in B:
        u = Ticket_Price(r,c,i)
        P = np.append(P,u)
        
        
    print('Number Of Purchased Tickets : ',np.shape(B)[0])
    print('Percentage : ',(np.shape(B)[0]/(r*c))*100,'%')
    print('Current income : $',np.sum(P))
    print('Total income : $',Total_Income(m))
    print('**********')
        
            
    