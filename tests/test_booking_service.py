"""Tests unitarios para services/booking_service.py"""
from datetime import date, timedelta
from services.booking_service import BookingService


def test_create_booking_success():
    service = BookingService()
    check_in = date.today() + timedelta(days=10)
    check_out = check_in + timedelta(days=3)

    booking = service.create_booking(
        user_id=2, destination_id=2, check_in=check_in, check_out=check_out, passengers=2
    )

    assert booking.total_price > 0
    assert booking.passengers == 2
