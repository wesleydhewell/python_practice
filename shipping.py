weight = float(input("What is the weight of the package that you'd like to ship (in lbs)? "))

#Ground Shipping
if weight <= 2.0:
  cost_ground = (weight * 1.50) + 20
elif weight <= 6.0:
  cost_ground = (weight * 3.00) + 20
elif weight <= 10.0:
  cost_ground = (weight * 4.00) + 20
else:
  cost_ground = (weight * 4.75) + 20

print("The total cost to ship this package with ground shipping is:", cost_ground, "dollars.")

ground_premium = 125

print("The cost of premium ground shipping is", ground_premium, "dollars.")

#Drone Shipping
if weight <= 2.0:
  cost_drone = (weight * 4.50)
elif weight <= 6.0:
  cost_drone = (weight * 9.00)
elif weight <= 10.0:
  cost_drone = (weight * 12.00)
else:
  cost_drone = (weight * 14.25)

print("The total cost to ship this package by drone is:", cost_drone, "dollars.")

if cost_ground < cost_drone:
  print("Ground shipping is more affordable.")
else:
  print("Drone shipping is more affordable.")