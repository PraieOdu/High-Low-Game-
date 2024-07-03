import random

from replit import clear

from game_data import data

from art import logo
from art import vs
more_follow = ""



def compare(guess,foll_count1,foll_count2,score):
  if guess == "a":
    if foll_count1 > foll_count2:
      score = score + 1
      clear()
      print(logo)
      print(f"You're right!. Current score = {score}")
      return "tu", score
    else:
      return "td", score
  elif guess == "b":
    if foll_count2 > foll_count1:
        score = score + 1
        clear()
        print(logo)
        print(f"You're right!. Current score = {score}")
        return "tuu", score
    else:
      return "tdd", score
  


print (logo)
# Pick 2 starting comparision
initial_list = []
a = random.choice(data)
b = random.choice(data)
while a == b:
  b = random.choice(data)
initial_list.append(a)
initial_list.append(b)



def comp():
  comp_dict = {}
  comp_dict["A"] = initial_list[0]
  comp_dict["B"] = initial_list[1]
  #List comparisions and ask user to guess
  temp_dict1 = {}
  temp_dict2 = {}
  temp_dict1 = comp_dict["A"]
  temp_dict2 = comp_dict["B"]
  name1 = temp_dict1["name"]
  description1 = temp_dict1["description"]
  foll_count1 = temp_dict1["follower_count"]
  country1 = temp_dict1["country"]
  name2 = temp_dict2["name"]
  description2 = temp_dict2["description"]
  foll_count2 = temp_dict2["follower_count"]
  country2 = temp_dict2["country"]
  print(f"Compare A: {name1}, a {description1}, from {country1}")
  print(vs)
  print(f"Against B: {name2}, a {description2}, from {country2}")
  select = input("Who has more followers? Type 'A' or 'B': ").lower()
  return select, foll_count1, foll_count2

score = 0
running = True
while running is True:
  guess, foll_count1, foll_count2 = comp()
  v,score = compare(guess, foll_count1, foll_count2,score) 
  if v == "tu":
    initial_list[1] = random.choice(data)
  elif v == "tuu":
    initial_list[0] = initial_list[1]
    initial_list[1] = random.choice(data)
  elif v == "td":
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score} ")
    running = False
  elif v == "tdd":
    clear()
    print (logo)
    print(f"Sorry, that's wrong. Final score: {score} ")
    running = False
