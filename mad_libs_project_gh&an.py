#There was merchant named {name} who lived in a small town. He was very {adjective_one} and did a lot of {verb1}. He heard a legend of a {adjective_two} princess who was taken by an {main_evil_animal} and held captive in a castle and that whoever saved the princess gained millions of {objects}. He decided to embark on his {time} long journey and save the priness. On his journey, he encountered many strange creatures and traversed through {adjective_three} terrain. During his quest, he came in contact with a very {adjective_4} {minor_animal_foe}. In order to continue to the priness, he had to fight this animal. He {adverb_one} {verb_two} at the animal and finally defeted it, claiming it's {noun_one} as a token of his victory. He finally made it to the castle, but had to find a way to get over the {number_one} foot tall wall. Once he made it in the castle, he needed to climb up {number_two} flights of stairs and complete {number_three} challenges. One challenge even involved needing to {verb_three} across the entire floor of the castle. He had then come face to face with the {main_evil_animal} holding the princess captive. The princess screamed {princess_scream_word} in distress. The merchant took out his {weapon} and readied it for battle. He began fighing the {main_evil_animal} and contunined to do so for {time_two}. After much struggle and even more determination, the {adjective_one} merchant finally slayed the {main_evil_animal} and saved the princess. As a thank you, she gave him the promised reward. Finally finished with his quest, he started to head home. Sadly, he was unable to use his rewards, for he was offed by a {stupid_animal} on his way back home. The end.



import time 

print("Welcome to MadLibs")
time.sleep(2)
print("Please enter the following blanks")
time.sleep(2)
name = (input("Enter a name: "))
adjective_one = input("Enter an adjective: ")
verb_one = input("Enter a verb (ending in ing): ")
adjective_two = input("Enter an adjective: ")
main_evil_animal= input("Enter an animal: ")
objects = input("Enter an insentive (ending in s): ")
time_one = input("Enter an amount of time (number, units): ")
adjective_three = input("Enter an adjective: ")
minor_animal_foe = input("Enter an animal: ")
adjective_four = input("Enter an adjective: ")
verb_two = input("Enter a verb (past tense): ")
adverb_one = input("Enter an adverb: ")
noun_one = input("Enter a noun: ")
number_one = input("Enter a number: ")
number_two = input("Enter a number: ")
number_three = input("Enter a number: ")
verb_three = input("Enter a travelling verb: ")
princess_scream_word = input("Enter any word: ")
weapon = input("Enter an object: ")
time_two = input("Enter an amount of time (number, units): ") 
stupid_animal = input("Enter an animal: ")

print("Here is your finsihed MadLib story:")
time.sleep(1)
for i in range(3,0,-1):
    print(i)
    time.sleep(1)

finished_story = (f"There was merchant named {name.capitalize()} who lived in a small town. He was very {adjective_one.lower()} and did a lot of {verb_one.lower()}. He heard a legend of a {adjective_two.lower()} princess who was taken by a(n) {main_evil_animal.lower()} and held captive in a castle and that whoever saved the princess would gain millions of {objects.lower()}. He decided to embark on his {time_one.lower()} long journey and save the priness. On his journey, he encountered many strange creatures and traversed through {adjective_three.lower()} terrain. During his quest, he came in contact with a very {adjective_four.lower()} {minor_animal_foe.lower()}. In order to continue to the priness, he had to fight this animal. He {adverb_one.lower()} {verb_two.lower()} at the animal and finally defeted it, claiming it's {noun_one.lower()} as a token of his victory. He finally made it to the castle, but had to find a way to get over the {number_one.lower()} foot tall wall. Once he made it in the castle, he needed to climb up {number_two.lower()} flights of stairs and complete {number_three.lower()} challenges. One challenge even involved needing to {verb_three.lower()} across the entire floor of the castle. He had then come face to face with the {main_evil_animal.lower()} holding the princess captive. The princess screamed {princess_scream_word.lower()} in distress. The merchant took out his {weapon.lower()} and readied it for battle. He began fighing the {main_evil_animal.lower()} and contunined to do so for {time_two.lower()}. After much struggle and even more determination, the {adjective_one.lower()} merchant finally slayed the {main_evil_animal.lower()} and saved the princess. As a thank you, she gave him the promised reward. Finally finished with his quest, he started to head home. Sadly, he was unable to use his rewards, for he was offed by a {stupid_animal.lower()} on his way back home. The end.")

print(finished_story)