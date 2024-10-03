from car import Car

car = Car()
print (car)

car.move_forward(1) # 1m/s speed
car.run_model(5) # 5s later
pos = car.get_position()
print (car)
assert pos.y == 5
