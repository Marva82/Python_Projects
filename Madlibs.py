# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subsribe to _____"

youtuber = "Aaron Uram" # some string variable

# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madLib = f"Computer programming is so {adj}! It makes me so excited all the time" \
         f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madLib)