class Audience :
    
    def __init__(self,Name,Gender,Age,Phn,seat):
        self.Name = Name
        self.Gender = Gender
        self.Age = Age
        self.Ph = Phn
        self.seat = seat
        
    def printDetails(self):
        print('Name : ',self.Name)
        print('Gender : ',self.Gender)
        print('Age : ',self.Age)
        print('Ph no : ',self.Ph)
        print('Seat No : ',self.seat)
        print('**********')
        

