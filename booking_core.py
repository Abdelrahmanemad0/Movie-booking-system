"""booking_core.py -- Core booking logic for the movie ticket system.
Python port of booking_system.c's data model (5x6 seat grid, three
movies, fixed EGP 120 ticket price, cash/Visa payment) so it can be
reused by both a CLI and the Streamlit web demo.
"""
from __future__ import annotations

from dataclasses import dataclass, field

ROWS = 5
COLS = 6
SEAT_LETTERS = "ABCDEF"
TICKET_PRICE = 120.0

MOVIES = ["Batman", "Me Before You", "John Wick 4"]


@dataclass
class Theater:
    """Holds the seat grid and booked-seat state for one session."""

    movie: str = MOVIES[0]
    seats: list = field(default_factory=lambda: [["_"] * COLS for _ in range(ROWS)])

    def is_booked(self, row: int, col_letter: str) -> bool:
        col = SEAT_LETTERS.index(col_letter)
        return self.seats[row][col] == "X"

    def book(self, row: int, col_letter: str) -> bool:
        """Book a seat. Returns False if already booked."""
        col = SEAT_LETTERS.index(col_letter)
        if self.seats[row][col] == "X":
            return False
        self.seats[row][col] = "X"
        return True

    def cancel(self, row: int, col_letter: str) -> bool:
        """Cancel a booked seat. Returns False if it wasn't booked."""
        col = SEAT_LETTERS.index(col_letter)
        if self.seats[row][col] != "X":
            return False
        self.seats[row][col] = "_"
        return True

    def booked_seats(self) -> list:
        return [
            f"{SEAT_LETTERS[c]}{r + 1}"
            for r in range(ROWS)
            for c in range(COLS)
            if self.seats[r][c] == "X"
        ]

    def total(self) -> float:
        return len(self.booked_seats()) * TICKET_PRICE


def cash_change(amount_due: float, cash_paid: float) -> tuple:
    """Return (success, change_or_shortfall)."""
    if cash_paid >= amount_due:
        return True, cash_paid - amount_due
    return False, amount_due - cash_paid
