# movie_booking_system.py
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Optional
import itertools

# ---------- PERSON (ABSTRACTION) ----------
class Person(ABC):
    def __init__(self, name: str, email: str):
        self._name = name                 
        self._email = email               

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @abstractmethod
    def display_info(self) -> str:
        pass

# ---------- SUBCLASSES ----------
class Customer(Person):
    _id_counter = itertools.count(1)

    def __init__(self, name: str, email: str, wallet: float = 0.0):
        super().__init__(name, email)
        self.customer_id = f"C{next(Customer._id_counter):04d}"
        self.__wallet = wallet           # private attribute
        self.bookings: List['Booking'] = []

    def display_info(self) -> str:
        return f"Customer {self.customer_id}: {self.name} ({self.email}) - Wallet: ₹{self.__wallet:.2f}"

    def add_funds(self, amount: float):
        if amount > 0:
            self.__wallet += amount
            return True
        return False

    def deduct(self, amount: float) -> bool:
        if 0 <= amount <= self.__wallet:
            self.__wallet -= amount
            return True
        return False

    def wallet_balance(self) -> float:
        return self.__wallet

class Staff(Person):
    _id_counter = itertools.count(1)

    def __init__(self, name: str, email: str, role: str = "staff"):
        super().__init__(name, email)
        self.staff_id = f"S{next(Staff._id_counter):03d}"
        self.role = role

    def display_info(self) -> str:
        return f"Staff {self.staff_id}: {self.name} ({self.email}) - Role: {self.role}"

# ---------- SUPPORTING ENTITIES ----------
class Movie:
    _id_counter = itertools.count(1)
    def __init__(self, title: str, duration_min: int, rating: str):
        self.movie_id = f"M{next(Movie._id_counter):03d}"
        self.title = title
        self.duration_min = duration_min
        self.rating = rating

    def __str__(self):
        return f"{self.movie_id} - {self.title} ({self.duration_min} min) [{self.rating}]"

class Show:
    _id_counter = itertools.count(1)
    def __init__(self, movie: Movie, screen: str, start_time: datetime, rows: int = 5, cols: int = 8, price: float = 150.0):
        self.show_id = f"SH{next(Show._id_counter):04d}"
        self.movie = movie
        self.screen = screen
        self.start_time = start_time
        # Seats represented as dict: 'A1' -> None or booking_id
        self.rows = rows
        self.cols = cols
        self._seats = self._generate_seat_map(rows, cols)
        self.price = price

    @staticmethod
    def _generate_seat_map(rows: int, cols: int) -> Dict[str, Optional[str]]:
        seats = {}
        for r in range(rows):
            row_letter = chr(ord('A') + r)
            for c in range(1, cols + 1):
                seats[f"{row_letter}{c}"] = None
        return seats

    def available_seats(self) -> List[str]:
        return [k for k, v in self._seats.items() if v is None]

    def book_seat(self, seat_label: str, booking_id: str) -> bool:
        if seat_label in self._seats and self._seats[seat_label] is None:
            self._seats[seat_label] = booking_id
            return True
        return False

    def cancel_seat(self, seat_label: str, booking_id: str) -> bool:
        if seat_label in self._seats and self._seats[seat_label] == booking_id:
            self._seats[seat_label] = None
            return True
        return False

    def __str__(self):
        return f"{self.show_id} | {self.movie.title} @ {self.start_time.strftime('%Y-%m-%d %H:%M')} | Screen: {self.screen} | Price: ₹{self.price:.2f}"

class Booking:
    _id_counter = itertools.count(1)
    def __init__(self, customer: Customer, show: Show, seat: str):
        self.booking_id = f"B{next(Booking._id_counter):05d}"
        self.customer = customer
        self.show = show
        self.seat = seat
        self.amount = show.price
        self.created_at = datetime.now()
        self.status = "CONFIRMED"   # or CANCELLED

    def cancel(self):
        if self.status == "CONFIRMED":
            self.status = "CANCELLED"
            return True
        return False

    def __str__(self):
        return f"{self.booking_id}: {self.customer.customer_id} -> {self.show.show_id} Seat {self.seat} | ₹{self.amount:.2f} | {self.status}"

# ---------- CONTROLLER / MANAGER ----------
class Cinema:
    total_revenue = 0.0

    def __init__(self, name: str):
        self.name = name
        self.movies: Dict[str, Movie] = {}
        self.shows: Dict[str, Show] = {}
        self.customers: Dict[str, Customer] = {}
        self.staff: Dict[str, Staff] = {}
        self.bookings: Dict[str, Booking] = {}

    # Movie / Show management
    def add_movie(self, title: str, duration_min: int, rating: str) -> Movie:
        m = Movie(title, duration_min, rating)
        self.movies[m.movie_id] = m
        return m

    def add_show(self, movie_id: str, screen: str, start_time: datetime, rows:int=5, cols:int=8, price: float = 150.0) -> Optional[Show]:
        movie = self.movies.get(movie_id)
        if not movie:
            return None
        s = Show(movie, screen, start_time, rows, cols, price)
        self.shows[s.show_id] = s
        return s

    # Customer / Staff registration
    def register_customer(self, name: str, email: str, wallet: float = 0.0) -> Customer:
        c = Customer(name, email, wallet)
        self.customers[c.customer_id] = c
        return c

    def register_staff(self, name: str, email: str, role: str = "staff") -> Staff:
        s = Staff(name, email, role)
        self.staff[s.staff_id] = s
        return s

    # Booking flow
    def create_booking(self, customer_id: str, show_id: str, seat: str) -> Optional[Booking]:
        customer = self.customers.get(customer_id)
        show = self.shows.get(show_id)
        if not customer or not show:
            return None
        if seat not in show.available_seats():
            return None
        # Payment
        price = show.price
        if not customer.deduct(price):
            return None  
        # Reserve seat
        booking = Booking(customer, show, seat)
        success = show.book_seat(seat, booking.booking_id)
        if not success:
            # revert funds
            customer.add_funds(price)
            return None
        # store booking
        self.bookings[booking.booking_id] = booking
        customer.bookings.append(booking)
        Cinema.total_revenue += price
        return booking

    def cancel_booking(self, booking_id: str) -> bool:
        booking = self.bookings.get(booking_id)
        if not booking or booking.status != "CONFIRMED":
            return False
        # cancel seat on show
        cancelled = booking.show.cancel_seat(booking.seat, booking.booking_id)
        if not cancelled:
            return False
        # refund policy: full refund
        refund_amount = booking.amount
        booking.cancel()
        booking.customer.add_funds(refund_amount)
        Cinema.total_revenue -= refund_amount
        return True

    # Reports
    def list_movies(self):
        return list(self.movies.values())

    def list_shows(self):
        return list(self.shows.values())

    def list_available_seats(self, show_id: str):
        show = self.shows.get(show_id)
        if not show:
            return []
        return show.available_seats()

    def get_customer_bookings(self, customer_id: str):
        c = self.customers.get(customer_id)
        return c.bookings if c else []

    @classmethod
    def get_total_revenue(cls):
        return cls.total_revenue

# ---------- Simple CLI to demonstrate ----------
def sample_cli_demo():
    cinema = Cinema("OpenSky Cinemas")

    # Preload some movies & shows
    m1 = cinema.add_movie("The Silent Sea", 120, "U/A")
    m2 = cinema.add_movie("Space Oddity", 140, "U")
    from datetime import timedelta
    s1 = cinema.add_show(m1.movie_id, "Screen 1", datetime.now().replace(hour=18, minute=0) , rows=4, cols=6, price=200.0)
    s2 = cinema.add_show(m2.movie_id, "Screen 2", datetime.now().replace(hour=21, minute=0), rows=4, cols=6, price=250.0)

    # Register customers
    alice = cinema.register_customer("Alice Kumar", "alice@example.com", wallet=1000.0)
    bob = cinema.register_customer("Bob Rao", "bob@example.com", wallet=100.0)

    print("=== Movies ===")
    for m in cinema.list_movies():
        print(m)
    print("\n=== Shows ===")
    for sh in cinema.list_shows():
        print(sh)

    print("\nAlice books A1 in show", s1.show_id)
    booking = cinema.create_booking(alice.customer_id, s1.show_id, "A1")
    if booking:
        print("Booked:", booking)
    else:
        print("Booking failed")

    print("\nBob tries to book A1 (already booked)")
    b2 = cinema.create_booking(bob.customer_id, s1.show_id, "A1")
    print("Result:", "Success" if b2 else "Failed - seat unavailable or insufficient funds")

    print("\nAvailable seats in show after bookings:", cinema.list_available_seats(s1.show_id)[:10])
    print("\nTotal revenue:", Cinema.get_total_revenue())

    print("\nAlice cancels booking")
    if cinema.cancel_booking(booking.booking_id):
        print("Cancelled", booking.booking_id)
    else:
        print("Cancel failed")
    print("Total revenue after refund:", Cinema.get_total_revenue())

if __name__ == "__main__":
    # For demonstration; run demo if file executed directly
    sample_cli_demo()
