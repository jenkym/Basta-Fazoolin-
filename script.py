from datetime import time

class Menu:
  
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return "The {meal} menu is available from {start} to {end}".format(meal=self.name, start=self.start_time, end=self.end_time)
  
  def calculate_bill(self, purchased_items):
    total = []
    for item in purchased_items:
      total.append(self.items.get(item, 0))
    return sum(total)
    
brunch = Menu('brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, time(11), time(16))
#print(brunch)

early_bird = Menu('early-bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, time(15), time(18))
#print(early_bird)

dinner = Menu('dinner', {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, time(17), time(23))
#print(dinner)

kids = Menu('kids', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, time(11), time(21))
#print(kids)

#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

#print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

class Franchise:
  
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
    
  def __repr__(self):
    return "{address} is the address of the restaurant".format(address=self.address)
  
  def available_menus(self, time):
    menus_list = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        menus_list.append(menu.name)
    if len(menus_list) == 0:
      return "There is no available menu"
    elif len(menus_list) == 1:
      return "The available menu is " + menus_list[0]
    else:
      string_menu = "The availables menus are: " 
      for i in range(len(menus_list)):
        if i == len(menus_list)-1:
          string_menu += "and " + menus_list[i]
        elif i == len(menus_list)-2:
          string_menu += menus_list[i] + " "
        else:
          string_menu += menus_list[i] + ", "
    return string_menu + " menus"
        
    
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
#print(flagship_store)

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
#print(new_installment)

#print(new_installment.available_menus(time(12)))
#print(new_installment.available_menus(time(17)))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
    
fazoolin_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = Menu("Take a' Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, time(10), time(20))

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

arepas_business = Business("Take a' Arepa!", [arepas_place])

