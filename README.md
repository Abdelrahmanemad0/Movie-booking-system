# Movie Ticket Booking System

Console-based C movie ticket booking system with a 5x6 seat map, booking/cancellation, and cash-or-Visa payment with transaction logging. Includes a Python/Streamlit web demo that ports the same logic to clickable seats in the browser.

<p>
  <img alt="C" src="https://img.shields.io/badge/C-99-A8B9CC?logo=c&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white">
  <img alt="Streamlit" src="https://img.shields.io/badge/Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg">
</p>

**[Live demo →](#deployment)**

## Overview

A simple cinema booking simulator: pick a movie, book seats on a 5-row × 6-column grid (A–F, rows 1–5), optionally cancel seats, then pay by cash (with change calculation) or Visa. Every booking is logged.

## Repository Contents

| File | Description |
|---|---|
| `booking_system.c` | Original console C implementation (`scanf`-driven, writes `transaction_history.txt`) |
| `booking_core.py` | Python port of the booking data model — `Theater` class (seat grid, book/cancel/total) and `cash_change()` |
| `booking_app.py` | Streamlit web demo: clickable seat grid, movie picker, live payment flow |
| `requirements.txt` | Python dependencies for the demo |

## Features

- **5×6 seat map** — seats A1–F5, booked seats marked and rendered live.
- **Book & cancel** — click a seat to book it, click again to cancel (web demo); interactive prompts in the C original.
- **Movie selection** — choose between three movies (Batman, Me Before You, John Wick 4).
- **Cash or Visa payment** — cash payments compute change or flag insufficient funds; Visa payments confirm instantly.
- **Fixed ticket pricing** — EGP 120 per seat, total computed from the number of booked seats.

## How to Run

### Web demo (Python/Streamlit)

```bash
git clone https://github.com/Abdelrahmanemad0/Movie-booking-system.git
cd Movie-booking-system
pip install -r requirements.txt
streamlit run booking_app.py
```

### Original console app (C)

```bash
gcc booking_system.c -o booking_system
./booking_system
```

## Deployment

Deployable in minutes on **Streamlit Community Cloud**: fork this repo, connect it at [share.streamlit.io](https://share.streamlit.io), and set `booking_app.py` as the entry point. No secrets required.

## Tech Stack

C (original console app) · Python, Streamlit (web demo port)

## License

MIT — see [LICENSE](LICENSE).

#c #python #streamlit #consoleapp #bookingsystem #beginnerproject
