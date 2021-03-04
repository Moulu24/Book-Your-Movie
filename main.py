from Modules import *

print('Welcome to BOOK_YOUR_MOVIE.COM')
rows = input('please enter the number of rows in the desired theatre\n')
columns = input('please enter the number of columns in the desired theatre\n')

def ShowOptions():
    print('Select From the Following Options')
    print('1.Show the Seats\n2.Buy a Ticket\n3.Statistics\n4.Show booked tickets User info\n0.Exit')
    n = input()
    return int(n)
n = ShowOptions()
m = Seats.Theatre(int(rows),int(columns))
q = 0
customers = []
while n != 0 :
    q = 0    
    if n == 1:
        print('1.Show the seats')
        Seats.Show_Seats(m)    
    elif n == 2:
        print('Buy a ticket')
        r = int(input("Enter the Row Number of your Seat\n"))
        c = int(input('Enter the column Number of your Seat\n'))
        for j in customers :
            if j.seat == (r,c) :
                print('Sorry, Those seats are occupied!!')
                print('**********')
                n = ShowOptions()
                q = 1
        if q == 1:
            continue
        TP = Stats.Ticket_Price(int(rows),int(columns),r)
        print('Your Ticket Price is ',TP,'$')
        inp = input('press "y" to proceed to booking\npress "n" to return to main menu\n')
        if inp == 'y':
            Name = input('Enter your name\n')
            Age = input('Enter your Age\n')
            Gender = input('Enter your Gender\n')
            Phn = input('Enter your Phone Number\n')
            print('**********')
            i = Details.Audience(Name,Gender,Age,Phn,(r,c))
            customers.append(i)
            m = Buy_a_ticket.Book_Ticket(m,r,c)
        elif inp == 'n':
            pass
        else :
            print("Please enter a valid response\nReturning to main menu\n...............\n")
    elif n == 3:
        print('Statistics')
        Stats.Show_Stats(m)
    elif n == 4:
        print('Booked tickets user info')
        for i in customers :
            i.printDetails()
    else :
        print('Please select from the given options only')
    n = ShowOptions()    
    
print('Thank You!')