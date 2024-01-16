class Ticket:
    def __init__(self, number, price):
        self.number = number
        self.price = price
    
    def getPrice(self):
        return self.price
    
    def toString(self):
        return f"Number: {self.number}, Price: {self.price}"


class StudentTicket(Ticket):
    def __init__(self, number, price, holder_name):
        super().__init__(number, price / 2)
        self.holder_name = holder_name
    
    def toString(self):
        return f"Number: {self.number}, Price: {self.price}, ID required for {self.holder_name}"



T1 = Ticket(17, 50.0)
print(T1.getPrice()) 
print(T1.toString())  

T2 = StudentTicket(17, 50.0, 'Tom')
print(T2.getPrice())  
print(T2.toString())  
