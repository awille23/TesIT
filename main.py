count = 0

print('"Welcome to your fiber optic dreams"'.title())

company_name = input("\nWhat is your company name? ")

while count <5:

  fiber_ft = int(input("\nHow many feet of fiber optic cable is needed? "))

  if fiber_ft <= 100:
    cost = 0.88
   
  if fiber_ft > 100:
    cost = 0.82

  if fiber_ft > 250:
    cost = 0.72

  if fiber_ft > 500:
    cost = 0.52
   
  total = (fiber_ft * cost) 
  print(f"\n{company_name.title()} wants {fiber_ft} ft. of fiber optic cable. \nYour total is ${total}")

  

