# Movie Ticket Booking System

This C program is a simple console-based Movie Ticket Booking System that allows users to:

- View a list of available movies.
- Select a movie and book seats in a 5x6 seating arrangement.
- Choose between cash or Visa payment methods.
- Cancel previously booked seats before finalizing payment.
- Store transaction history in a file (`transaction_history.txt`).

## Features

- **Seat Selection** — users can view and book available seats.
- **Fixed Pricing** — ticket price is EGP 120 per seat.
- **Payment Methods** — supports Visa and Cash payments.
- **Booking Cancellation** — allows users to cancel selected seats before payment.
- **Transaction History** — saves payment details to a file.

## How to Run

```bash
gcc movie_booking_system.c -o movie_booking
./movie_booking
```

Follow the prompts to choose a movie, book seats, optionally cancel a seat, and complete payment.

## Project Structure

- `movie_booking_system.c` — main program (renamed from `final code.c`, which had a space in the filename)
- `README.md` — this file
- `LICENSE` — MIT license
- `.gitignore` — build artifacts and transaction history log to keep out of version control

## Fixes in this revision

- **Renamed `final code.c` to `movie_booking_system.c`** — the old filename had a space in it, which meant the README's own `gcc final_code.c` instructions never matched the actual file and required awkward quoting to compile at all.
- **Fixed an out-of-bounds array access in seat cancellation.** The booking loop validates that the row (1-5) and seat letter (A-F) are in range before touching the `seats[5][6]` array, but the cancellation loop skipped that check entirely — entering an out-of-range row or letter there read/wrote outside the array (undefined behavior, and a likely crash). Added the same validation used for booking.

## License

MIT — see [LICENSE](LICENSE).
