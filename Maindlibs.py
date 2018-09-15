""" \ Abdullah Alazzani
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story 

story = """
This morning %s woke up feeling %s. 'It is going to be a %s day!'
Outside, a bunch of %ss were protesting to keep %s in stores.
They began to %s to the rhythm of the %s, which made all the %ss very %s.
Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle
of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."""

print ("Mad Lips is startaing!")
name = input("Enter a name: ")
adj1 = input("Enter an adjective: ")
adj2 = input("Enter a second adjective: ")
adj3 = input("Enter one more adjective: ")
verb = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
animal = input("Enter a name of animal: ")
food = input("Enter a name of food: ")
fruit = input("Enter a name of fruit: ")
superhero = input("Enter a name of superhero : ")
country = input("Enter a name of country: ")
dessert = input("Enter a name of dessert: ")
year = input("Enter a year: ")
STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print (story % (name, adj1, adj2, adj3, verb, noun1, noun2, animal, food, fruit,
         superhero, country, dessert, name, dessert, name, year, noun2))

bye = input("Thanks for your time! I hope you enjoyed! ") 


























