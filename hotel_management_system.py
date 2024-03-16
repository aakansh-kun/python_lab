class HotelManagement:
    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1000, name='', address='', cindate='', coutdate='', rno=1):
        print("\n\n***** WELCOME TO HOTEL MUMBAI *****\n")
        self.rt = rt
        self.s = s
        self.p = p
        self.r = r
        self.t = t
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def inputdata(self):
        self.name = input("Enter your name: ")
        self.address = input("Enter your address: ")
        self.cindate = input("Enter check-in date (dd/mm/yyyy): ")
        self.coutdate = input("Enter check-out date (dd/mm/yyyy): ")
        print("Your room number will be allocated at check-in.")

    def roomrent(self):
        print("\nWe have the following room types:")
        print("1. Single Bed - $1000 per night")
        print("2. Double Bed - $2000 per night")
        print("3. Luxury Suite - $5000 per night")
        self.s = int(input("Enter your choice (1/2/3): "))
        self.rno = int(input("Enter room number: "))
        self.t = int(input("Enter number of nights: "))

        if self.s == 1:
            self.r = 1000 * self.t
            print(f"Your room rent is ${self.r}")
        elif self.s == 2:
            self.r = 2000 * self.t
            print(f"Your room rent is ${self.r}")
        elif self.s == 3:
            self.r = 5000 * self.t
            print(f"Your room rent is ${self.r}")
        else:
            print("Invalid choice!")

    def display(self):
        print("\n***** HOTEL BILL *****")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Check-in Date: {self.cindate}")
        print(f"Check-out Date: {self.coutdate}")
        print(f"Room Number: {self.rno}")
        print(f"Total Amount: ${self.r}")

    def main(self):
        self.inputdata()
        self.roomrent()
        self.display()


# Create an instance of the HotelManagement class
hotel = HotelManagement()
hotel.main()
