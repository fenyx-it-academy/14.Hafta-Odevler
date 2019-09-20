n = int(input("the number of pages in the book :"))
p = int(input("the page number to turn to :"))
# total, given_number = int(n/2), int(p/2)
# if total - given_number > given_number:
#     print(given_number)
# else:
#     print(total - given_number)
print(min(int(p/2),int(n/2)-int(p/2)))
