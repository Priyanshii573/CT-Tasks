# PROGRAM 1

class Vehicle:
  def __init__(self,seating_capacity):
    self.seating_capacity = seating_capacity
  def fare(self):
    return self.seating_capacity*100
  
class Bus(Vehicle):
  def __init__(self,seating_capacity):
    super().__init__(seating_capacity)

  def fare(self):
    base_fare = super().fare()
    maintenance_charge = base_fare * 0.10 
    total_fare = base_fare + maintenance_charge
    return total_fare
  
if __name__ == "__main__":
  bus = Bus(seating_capacity=50)
  print(f"Total fare for the bus ride: ${bus.fare()}")
  
  

# PROGRAM 2
# Program to Count Words in Text File

number_of_words = 0
with open(r'word.txt','r') as file:
	data = file.read()
	lines = data.split()
	number_of_words += len(lines)
print(number_of_words)



# PROGRAM 3
# Program that read and display numbers in a text file 

h = open('word.txt', 'r')
content = h.readlines()
a = 0
numbers = []

for line in content:
	
	for i in line:
		if i.isdigit():
			number = int(i)
			a += number
			numbers.append(number)
print("The numbers found are:", numbers)
print("The sum is:", a)



