#initialise arrays and variables
weight = [0.0]*5

dogSize = ""

totalWeight = 0.0

averageWeight = 0.0

recommended = ""

#fixed loop
for i in range(5):

  #asks the suer for the weight of each day
  weight[i] = float(input("What is the weight of day " + str(i+1) + " "))

  #validates the weight inputed
  while weight[i] <0 or weight[i] > 200:

    #asks the user for weight again if its not right
    weight[i] = float(input("ERROR. A CONTAINER CAN ONLY HOLD UP TO 200g. What is the weight of day " + str(i+1) + " "))

  #calculates the total weight
  totalWeight = totalWeight + weight[i]

#asks the suer for the dogs size
dogSize = input("WHat is the size of the dog small medium or large: ")

#checks if the total weight matches the dogs size
if dogSize == "small" and totalWeight >= 110 and totalWeight <= 140:

  recommended = "This weight is suitable for this dog"

else:

  if dogSize == "medium" and totalWeight >= 330 and totalWeight <= 440:
    
    recommended = "This weight is suitable for this dog"
    
  else:

    if dogSize == "large" and totalWeight >= 690 and totalWeight <= 900:

      recommended = "This weight is suitable for this dog"

    else:

      recommended = "This weight is not suitable for this dog"

#finds the average weight
averageWeight = totalWeight/5

#rounds the average to 1 d.p
round(averageWeight,1)

#fixed loop
for i in range (5):

  #displays each days weight
  print ("Weight day " + str(i+1) + " - ", weight[i])

#displays the total weight
print ("Total weight is " , totalWeight)

#displays the average weight
print ("The average weight is " , averageWeight)

#displays if the weight is recommended for the dogs size
print ("" + recommended)
