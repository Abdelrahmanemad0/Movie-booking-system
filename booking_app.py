"""booking_app.py -- Streamlit web demo for the console Movie Ticket
Booking System (booking_system.c). Reimplements the same seat-map,
booking/cancellation, and cash-or-Visa payment flow as clickable seats
in the browser instead of scanf() prompts.

Run:
    streamlit run booking_app.py
"""
import streamlit as st

from booking_core import MOVIES, ROWS, SEAT_LETTERS, TICKET_PRICE, Theater, cash_change

st.set_page_config(page_title="Movie Ticket Booking", page_icon="\U0001F3AC", layout="centered")

if "theater" not in st.session_state:
    st.session_state.theater = Theater()
if "paid" not in st.session_state:
    st.session_state.paid = False

theater = st.session_state.theater

st.title("Movie Ticket Booking System")
st.caption(f"Console C app ported to a web demo. Fixed ticket price: EGP {TICKET_PRICE:.0f}.")

theater.movie = st.selectbox("Choose a movie", MOVIES, index=MOVIES.index(theater.movie))

st.subheader("Seat Map")
st.caption("Click a seat to book it, click again to cancel.")

header_cols = st.columns([1] + [1] * len(SEAT_LETTERS))
header_cols[0].write("")
for i, letter in enumerate(SEAT_LETTERS):
    header_cols[i + 1].markdown(f"**{letter}**")

for r in range(ROWS):
    row_cols = st.columns([1] + [1] * len(SEAT_LETTERS))
    row_cols[0].markdown(f"**Row {r + 1}**")
    for c, letter in enumerate(SEAT_LETTERS):
        booked = theater.is_booked(r, letter)
        label = "X" if booked else "-"
        button_type = "primary" if booked else "secondary"
        if row_cols[c + 1].button(label, key=f"seat-{r}-{letter}", type=button_type):
            if booked:
                theater.cancel(r, letter)
            else:
                theater.book(r, letter)
            st.session_state.paid = False
            st.rerun()

st.divider()

booked_seats = theater.booked_seats()
total = theater.total()

st.subheader("Booking Summary")
st.write(f"Movie: **{theater.movie}**")
st.write(f"Booked seats: **{', '.join(booked_seats) if booked_seats else 'none'}**")
st.metric("Total amount due", f"EGP {total:.2f}")

if booked_seats and not st.session_state.paid:
    st.subheader("Payment")
    method = st.radio("Payment method", ["Visa", "Cash"], horizontal=True)

    if method == "Visa":
        if st.button("Pay with Visa", type="primary"):
            st.session_state.paid = True
            st.success(f"Paid EGP {total:.2f} with Visa. Booking confirmed!")
    else:
        cash = st.number_input("Cash paid (EGP)", min_value=0.0, step=10.0, format="%.2f")
        if st.button("Pay with Cash", type="primary"):
            ok, delta = cash_change(total, cash)
            if ok:
                st.session_state.paid = True
                st.success(f"Payment successful. Change due: EGP {delta:.2f}. Booking confirmed!")
            else:
                st.error(f"Insufficient cash. You need EGP {delta:.2f} more.")
elif st.session_state.paid:
    st.success("This booking has been paid. Book more seats to start a new transaction.")
else:
    st.info("Book at least one seat to proceed to payment.")

if st.button("Reset booking"):
    st.session_state.theater = Theater()
    st.session_state.paid = False
    st.rerun()
