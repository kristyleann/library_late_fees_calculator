# This is a simple calculator that calculates late fees for Princeton Public Library in WV.
# DISCLAIMER: This project is not affiliated with Princeton Public Library in any way.
# I'm just someone learning to program that wanted to see if I could make this and
# Princeton Public Library just happens to be my local library.


print("This is a calculator that tells you how much you owe in late fees at the Princton Public Library in Princeton, WV.\n")
from time import sleep
sleep(3)
print("DISCLAIMER: This project is not actually affiliated with Princeton Public Library. That just happens to be my local library and I wanted to see if I could make this late fee calculator. \n")

sleep(4)
print("At this library, the fines for books that are currently on the best seller list are $0.25 a day. \n")
sleep(2)
print("Fines for all other books are $0.10 a day. \n")
sleep(2)
print("And fines for DVDs are $1.00 a day. \n")
sleep(2)
print("And fines stop accumulating after 40 days. \n")
sleep(2)
print("However, at that point the item is considered lost and unless it is turned in the cost of it is also added to the late fees. \n")
sleep(2)
print("But this calculator can only tell you late fees. \n")
sleep(4)
input('Hit ENTER to continue.')
sleep(1)

# calculation for best seller books begins

best_seller_books = input('How many "best seller" books do you have overdue? ')
best_seller_days = input('How many days have they been overdue? ')

if int(best_seller_days) >= 40:
  best_seller_days = 40

best_seller_fines = int(best_seller_books) * int(best_seller_days) * float(0.25)

sleep(1)
# calculation for regular books begins


regular_books = input('How many regular books do you have overdue? ')
regular_books_days = input('How many days have they been overdue? ')

if int(regular_books_days) >= 40:
  regular_books_days = 40

regular_books_fines = int(regular_books) * int(regular_books_days) * float(0.10)

sleep(1)

#calculation for DVDs begins
dvds = input('How many DVDs do you have overdue? ')
dvds_days = input('How many days have they been overdue? ')

if int(dvds_days) >= 40:
  dvds_days = 40

dvds_fines = int(dvds) * int(dvds_days) * float(1.00)

sleep(1)
# calculation for total amount due begins

total = float(best_seller_fines) + float(regular_books_fines) + float(dvds_fines)
sleep(2)

print(f"You owe ${total} in late fees. \n")
sleep(2)

print("I hope you enjoyed this little project. \n")
sleep(2)
print("It still has some limitations though. For instance... \n")
sleep(3)

print("Obviously, people check out items on different days, so a patron could have two or more sets of items that would have been overdue for a different number of days. \n")

sleep(2)
print("So I'm working on figuring out a solution for that. \n")
sleep(2)
print("If you find this useful or even just amusing, feel free to use it for your own purposes. \n")
sleep(2)


input('Hit ENTER to exit')
