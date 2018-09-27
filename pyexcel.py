import os
files = [file for file in os.listdir("./data") if "txt" in file ] 
f = open("sfd.txt", "w")

'''
for file in files:
  stat = {
      "1": 0,
      "2": 0,
      "3": 0,
      "4": 0
  }
  with open(file) as f:
    for line in f:
      for char in line:
        if char == "1":
          stat["1"] += 1
        elif char == "2":
          stat["2"] += 1
        elif char == "3":
          stat["3"] += 1
        elif char == "4":
          stat["4"] += 1
    print(file)
    print(stat)
'''