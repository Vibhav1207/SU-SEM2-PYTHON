seats = set(range(1, 6))

while seats:
    seat = int(input("Enter seat (0 to exit): "))
    if seat == 0:
        break
    if seat in seats:
        seats.remove(seat)
        print("Booked")
    else:
        print("Unavailable")