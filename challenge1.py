#Written by Shiven Desai
class Students:
    def GetInformation(self):
        print('student Lastname name is ' + self.Lastname)
        print('student Firstname name is ' + self.Firstname)
        print('student Address name is ' + self.Address)
        print('student City name is ' + self.City)
        print('student State name is ' + self.State)
        print('student Zipcode name is ' + self.Zipcode)

    def SetInformation(self):
        self.Lastname = input('Enter student Lastname: ')
        self.Firstname = input('Enter student Firstname: ')
        self.Address = input('Enter student Address: ')
        self.City = input('Enter student City: ')
        self.State = input('Enter student State: ')
        self.Zipcode = input('Enter student Zipcode: ')

# create Student1 object
Student1 = Students()
Student1.Lastname = 'Doe'
Student1.Firstname = 'Jane'
Student1.Address = '111 St'
Student1.City = 'Santa Ana'
Student1.State = 'CA'
Student1.Zipcode = '12345\n'

# create Student2 object
Student2 = Students()
Student2.Lastname = 'Cantor'
Student2.Firstname = 'Mike'
Student2.Address = '222 St'
Student2.City = 'Garden Grove'
Student2.State = 'CA'
Student2.Zipcode = '67890'

# create Student3 object using SetInformation method
Student3 = Students()
Student3.SetInformation()

# display information for all three students
Student1.GetInformation()
Student2.GetInformation()
Student3.GetInformation()
