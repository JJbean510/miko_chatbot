# import datetime (figure out how to check for a datetime to confirm time of day to give greetings)
# print("Good Morning, I'm Miko, how can I be of service? ")
# if 1 <= int(input()) < 100:
    #print("we're working with numbers")

# Think of more basic questions Miko can ask
# Make guessing game while loop (potentially a song guessing game based off of lyrics)

age = int(input("Before I can answer your question would you mind letting me know how old are you? "))
if age < 18:
    print("Sorry, but you must be at least 18 years old to talk to me.")
if age == 18:
    print("Aren't you a little young to be in to this kind of thing? Go Tik-Tok or something.")
elif age in range(19, 29):
    print("Hmmm, you're almost at the peak of this rollercoaster you call life. Must suck to have to be alive, haha!")
elif age in range(30, 45):
    print("You are in the prime of your life, after this season comes the Fall.")
elif age in range(46, 60):
    print("It is never to late to be who you were supposed to be, someone needs to hear that...")
elif age in range(61, 90):
    print("I'm surprised this is your kind of thing. Well, welcome, I'm Miko.")
elif age in range(91, 110):
    print("Let's talk about the last hundred years, I'm pretty well versered.")
else:
    print("Why are you still alive?")

hometown = input("Now that we know your cycle count is correct, where are you from? ")
if hometown == "Oakland" or hometown == "San Franciso" or hometown == "SF" or hometown == "San Jose" or hometown == "SJ":
    print("Bay Boy I see you!")
elif hometown == "Sacramento" or "Elk Grove" or "Fresno" or "Stockton":
    print("Valley Boy!")
else:
    print("I've never been there, is it far? ")

#Figure out why input isn't being returned but hex location is
favorite_genre_music = input("What's your favorite genre of music? ".capitalize)

if favorite_genre_music == "rock":
    print("Nice, my favorite Rock band is Summer Salt, you must have heard of them.")
elif favorite_genre_music == "rap":
    print("I'm not a huge fan of rap, but when I listen it is probably Tyler the Creator")
elif favorite_genre_music == "country":
    print("Is Old Town Road considered Country?")
elif favorite_genre_music == "alternative":
    print("Have you heard of Kero Kero Bonito? If not, I highly recommend her!")
elif favorite_genre_music == "hip hop":
    print("Real hip hop, HIP HOP! Know of any new artists?")
else:
    print("Never heard of em, any song suggestions?")

