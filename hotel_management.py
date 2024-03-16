rooms = {101: 'vacant', 102: 'vacant', 103: 'occupied', 104: 'vacant', 105: 'occupied', 106: 'vacant', 107: 'vacant',
         108: 'vacant', 109: 'occupied', 110: 'vacant', 111: 'occupied', 112: 'vacant', 113: 'vacant', 114: 'vacant', 
         115: 'occupied', 116: 'vacant', 117: 'occupied', 118: 'vacant', 119: 'vacant', 120: 'vacant'}

def check_availability(room_number):
    if rooms[room_number] == 'vacant':
        print(f"Room {room_number} is available for booking.")
    else:
        print(f"Room {room_number} is currently occupied.")

def book_room(room_number):
    if rooms[room_number] == 'vacant':
        rooms[room_number] = 'occupied'
        print(f"Room {room_number} has been successfully booked.")
    else:
        print(f"Room {room_number} is currently occupied.")

def checkout_room(room_number):
    if rooms[room_number] == 'occupied':
        rooms[room_number] = 'vacant'
        print(f"Room {room_number} has been checked out.")
    else:
        print(f"Room {room_number} is already vacant.")


print(rooms)
a= int(input("enter room no. to book it: "))
check_availability(a)
book_room(a)
checkout_room(a)
quit()
