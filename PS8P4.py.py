f = open("p3d.txt", "r")
c = 0.0
totp_ex = 0.0
item = str(f.readline().rstrip('.\n'))

while item !="":
  qty = float(f.readline())
  price = float(f.readline())

  ep = qty*price
  totp_ex = totp_ex + ep
  c = c + 1

  print("item is:           ", item)
  print("Quantity is:       ", qty)
  print("Price is:          ", price)
  print("Extended price is: ", ep)

  item = str(f.readline().rstrip('.\n'))
print("Total Extended Prices:      ", totp_ex)
print("Number of orders:           ", c)
avg = totp_ex / c
print("Average Order:              ", avg)
