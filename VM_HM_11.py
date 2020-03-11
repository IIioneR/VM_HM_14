class Hotel(object):

    def __init__(self, rooms):
        self.rooms = rooms
        self.booked_rooms = []

        self.clients = {}

    def add_room(self, room):
        self.rooms.append(room)

    def is_free(self, room):
        if room in self.booked_rooms:
            raise Exception("Not_free")

        if room in self.booked_rooms:
            return False
        else:
            return True

    def book_room(self, room, client, date):
        self.clients[room.number] = client
        if bed not in room.book_beds:
            if date not in date.book_days:
                self.booked_rooms.append(room)
                date.book_days.append(date)

                hotel.booked_rooms.append(room.book_beds.append(bed))



    def leave_room(self, room):
        self.clients.pop(room.number)
        self.booked_rooms.remove(room)

    def get_client_number(self, client):
        for key in self.clients.keys():

            if self.clients[key] == client:
                return key


class Service(object):

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Room(object):

    def __init__(self, number, price, bed):
        self.bed = bed
        self.number = number
        self.price = price

        self.beds = []
        self.book_beds = []

        self.clients = {}


    def __repr__(self):
        return str(self.number)


    def add_beds(self, bed):
        self.beds.append(bed)

    def is_available_bed(self, bed):
        if bed in self.beds:
            raise Exception("don't have beds")
        if bed in self.beds:
            return True
        return False

    def set_bed(self, bed, client):
        self.book_beds.append(bed)
        self.clients[room.number] = client

    def leave_bed(self, bed):
        self.book_beds.remove(bed)
        self.clients.pop(bed)


class Bed(object):

    def __init__(self, number):
        self.number = number

class Reception(object):

    @staticmethod
    def check_in(hotel, room):
        if hotel.is_free(room):
            if room.is_available_bed(bed):
                hotel.book_room(room)
                room.set_bed(bed)
                return True

        return False

    @staticmethod
    def check_out(hotel, room):
        room.leave_bed(bed)
        hotel.leave_room(room)


class Client(object):

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

        self.ordered_service = []

    def order_service(self, service):

        if self.balance >= service.price:
            self.balance -= service.price

            self.ordered_service.append(service)

    def book(self, hotel, room, bed, date):

        if self.balance <= room.price:
            raise Exception("not have money")




        if hotel.is_free(room):
            hotel.book_room(room, client1, date)
            room.set_bed(bed, client1)
            self.balance -= room.price

class Calendar(object):

    def __init__(self, date):
        self.date = date

        self.free_days = [i for i in range(1,31)]
        self.book_days = []

    def is_available_day(self):
        if date in date.book_days:
            raise("not available data")

        if date in date.free_days:
            return True

    def set_date(self, date):
        if date not in self.book_days:
            self.book_days.append(date)
        else:
            return False

    def __repr__(self):
        return str(self.date)

room = Room(2, 100, 30)
bed = Bed(3)
bed2 = Bed(5)
bed3 = Bed(5)
date = Calendar(15)
print(room.add_beds(bed))
hotel = Hotel([])
client1 = Client("val", 300)



print(hotel.rooms)

hotel.add_room(room.add_beds(bed))
hotel.add_room(room.add_beds(bed2))
hotel.add_room(room.add_beds(bed3))

print(room.beds)

print(client1.balance)
client1.book(hotel, room, room.add_beds(bed), date)
print(room.bed)
print(room.number)
print(client1.balance)
print(date.free_days)
print(date.book_days)
