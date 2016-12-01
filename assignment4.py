#This program reads a file containing a food web and identifies the relationships between the organisms
#Shannon TJ, Winter 2014

import sys

#Parameters: N/A
#Returns: Name of the file
def commandline_arg():
  #If user does not provide a command line argument, let user type in file name
  if len(sys.argv) == 1:
    filename = input("Enter the name of a file: ")
  #If file name does not exist, display error message
    try: 
      inf = open(filename, "r")
    except IOError: 
      print("Error: File not found.")
      quit()
  #If user provides one command line argument, open file
  elif len(sys.argv) == 2:
    filename = sys.argv[1]
  #If file name does not exist, display error message
    try: 
      inf = open(filename, "r")
    except IOError:
      print("Error: File not found.")
      quit()
  #If user provides more than one command line argument, display error message
  elif len(sys.argv) > 2:
    print("Error: More than one command line argument entered.")
    quit()
  
  return filename

#Create a dictionary to store predator/prey relationships
#Parameters: The name of the file input by the user
#Returns: A dictionary containing predator-prey relationships
def dictionary(filename):
  pred_prey_dict = {}
  for line in filename:
  #Create empty list to store prey
    prey_List = []
    line = line.rstrip()
    predator, prey = line.split("eats")
    prey_List.append(prey)
  #If predator in dictionary
    if predator in pred_prey_dict:
      for prey in prey_List: 
        pred_prey_dict[predator].append(prey)
  #If predator not in dictionary
    else:
      pred_prey_dict[predator] = prey_List
  #Close the file
  filename.close
  return pred_prey_dict

#Lists what each predator eats
#Parameters: A dictionary containing predator-prey relationships
#Returns: N/A
def foodchainOutput(dictionary):
  print("Predators and Prey:")
  for pred in dictionary:  
    valueList = dictionary[pred]
    #If the predator eats one thing, format the string accordingly
    if len(dictionary[pred]) == 1:
      print(pred+"eats"+valueList[0])
    #If the predator eats two things, place an 'and' between the prey
    elif len(dictionary[pred]) == 2:
      print(pred+"eats"+valueList[0]+" and"+valueList[1])
    #If the predator eats more than two things, format the string accordingly
    elif len(dictionary[pred]) > 2:
      bound= len(valueList) - 2
      prey = ""
    #Place a comma between any prey that aren't the last two prey
      for value in range(bound):
        prey+=valueList[value]+","
    #Place an 'and' between the last two prey
      prey+=valueList[len(valueList)-2]+" and"+valueList[len(valueList)-1]
      print(pred+"eats"+prey)

#Identifies the apex predators in a given food web
#Parameters: A dictionary containing predator-prey relationships
#Returns: A list of apex predators in the food web
def apexPredators(dictionary):
  print("\nApex Predators:")
  #Create empty lists for predators, prey, and apex predators
  predator_List = []
  prey_List =[]
  apexPredator_List = []
  #Fill predator list with predators from the dictionary
  for pred in dictionary:
    predator_List.append(pred.strip())
  #Fill prey list with prey from the dictionary
    for prey in dictionary[pred]:
      prey_List.append(prey.strip()) 
  #Determine if predator appears in prey list
  #Determine if predator already appears in apex predator list
  #Add predator to apex predator list if not in both lists
  for pred in predator_List:
    if pred not in prey_List and pred not in apexPredator_List:
      apexPredator_List.append(pred)
  return apexPredator_List

#Identifies the producers in a given food web
#Parameters: A dictionary containing predator-prey relationships
#Returns: A list of producers in the food web
def producers(dictionary):
  print("\nProducers:")
  #Create empty lists for predators, prey, and producers
  predator_List = []
  prey_List =[]
  producer_List = []
  #Fill predator list with predators from the dictionary
  for pred in dictionary:
    predator_List.append(pred.strip())
  #Fill prey list with prey from the dictionary
    for prey in dictionary[pred]:
      prey_List.append(prey.strip())
  #Determine if prey appears in predator list
  #Determine if prey already appears in producer list 
  #Add prey to producer list if not in both lists
  for prey in prey_List:
    if prey not in predator_List and prey not in producer_List:
      producer_List.append(prey)
  return producer_List

#Identifies the most flexible eaters in a given food web
#Parameters: A dictionary containing predator-prey relationships
#Returns: A list of the most flexible eaters in the food web
def flexibleEaters(dictionary):
  print("\nMost flexible eaters:")
  #Create empty list to store amount of different prey eaten
  biggest_length = 0
  length_List = []
  #Determine the largest amount of different prey eaten by any predator
  for pred in dictionary: 
    if len(dictionary[pred]) > biggest_length:
      biggest_length = len(dictionary[pred])
  #Add any predator that eats the same amount of different prey to the list
  for pred in dictionary:
    if len(dictionary[pred]) == biggest_length:
      length_List.append(pred)
  return length_List

#Identifies the tastiest organisms in a given food web
#Parameters: A dictionary containing predator-prey relationships
#Returns: A list of the tastiest organisms in a given food web
def tastiest(dictionary):
  print("\nTastiest:")
  #Create empty dictionary to store prey as keys and how many predators 
  #eat them as values
  tastiest_Dict = {}
  for pred in dictionary:
    for prey in dictionary[pred]:
  #If prey in dictionary, increase count by 1
      if prey in tastiest_Dict:
        tastiest_Dict[prey] = tastiest_Dict[prey] + 1
  #If prey not in dictionary, add prey with a count of 1
      else: 
        tastiest_Dict[prey] = 1
  #Create an empty list to store the tastiest organisms
  tastiest_List = []
  #Find the biggest number of different predators that eat the same prey
  maxVal = max(tastiest_Dict.values())    
  for prey in tastiest_Dict:
  #Add any prey that is eaten by the same number of different predators to the 
  #list of tastiest organisms
    if tastiest_Dict[prey] == maxVal:
      tastiest_List.append(prey)
  return tastiest_List
  
#Computes the heights of organisms in a given food web
#Parameters: A dictionary containing predator-prey relationships
#Returns: A dictionary containing predator and prey heights
def height(dictionary):
  print("\nHeights:")
  height_Dict = {}
  animal_List = []
  #Fill predator list with predators from the dictionary
  for pred in dictionary:
    animal_List.append(pred.strip())
    for prey in dictionary[pred]:
      if prey not in animal_List:
        animal_List.append(prey.strip())
  for animal in animal_List:
    height_Dict[animal] = 0
  print(height_Dict)
 
  change = 1
  while change == 1:
    change = 0
    for pred in dictionary:
      for prey in dictionary[pred]:
        if height_Dict[pred] <= height_Dict[prey]:
          height_Dict[pred] = height_Dict[prey] + 1
          change = 1
  print(height_Dict)

def main():

  filename = commandline_arg()

  #Open the file
  inf = open(filename, "r")

  #Create a dictionary from a file
  pred_prey_dict = dictionary(inf)
  #List what each predator eats
  foodchainOutput(pred_prey_dict)

  #Identify the apex predators
  apex_P_List = apexPredators(pred_prey_dict)
  for a_pred in apex_P_List:
    print(a_pred) 

  #Identify the producers
  prod_List = producers(pred_prey_dict)
  for prod in prod_List:
    print(prod)

  #Identify the most flexible eaters
  flex_List = flexibleEaters(pred_prey_dict)
  for flex_eat in flex_List:
    print(flex_eat) 

  #Identify the tastiest organisms
  tastiest_List = tastiest(pred_prey_dict)
  for tastiest_org in tastiest_List:
    print(tastiest_org)
 
  #Determine the height of every organism
  height(pred_prey_dict)  
 

main() 
  
