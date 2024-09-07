from time import *
import random as r

print

def mistake(paratest, usertest):
  error = 0
  for i in range(len(paratest)):
    try:
      if paratest[i] != usertest[i]:
         error = error+1
    except:
      error = error+1
  return error


def wpm(time_star, time_end, userinp):
  time_taken = (time_end - time_star)/60
  time_round = round(time_taken,2)
  speed = ((len(userinp)/5)/time_round)
  return round(speed)

while True:
  chk = input("Are you ready? [y/n]:")
  if chk == "y":
    test = ["In the quiet town of Willowbrook, a gentle breeze rustled the golden leaves of autumn, carrying with it the distant sound of laughter from children playing in the park. The sky, painted in soft hues of orange and pink, signaled the approach of dusk as the sun dipped below the horizon. Old Mr. Thompson, with his silver hair and weathered face, sat on his porch, sipping a cup of tea and reminiscing about days long gone.", "The rain poured down in sheets, drumming against the roof and windows of the little cottage nestled deep in the woods. Inside, the fire crackled softly in the stone hearth, casting flickering shadows across the room. A thick blanket of steam rose from the pot of soup simmering on the stove, filling the air with the rich aroma of herbs and vegetables. Outside, the world seemed distant and wild, with the trees swaying in the wind and the occasional flash of lightning illuminating the dark sky. Despite the storm raging beyond the walls, a sense of warmth and comfort filled the small space, as if it were a world all its own, untouched by the chaos outside.", "The old library stood at the edge of town, its towering shelves filled with dusty tomes and forgotten stories. Every afternoon, a soft golden light would filter through the stained-glass windows, casting a kaleidoscope of colors across the worn wooden floors. The air smelled of aged paper and ink, with a faint hint of lavender from the small garden outside. Few people visited anymore, save for the occasional curious wanderer or determined scholar. But those who did often found themselves lost in time, as though the library itself held secrets that waited to be discovered by only the most patient souls."]
    test1 = r.choice(test)

    print("*****Typing Speed*****")
    print(test1)
    print("\n ", "\n")
    time1 = time()
    testinp = input("Start typing: \n")
    time2 = time()


    print("Speed: ", wpm(time1,time2, testinp), "wpm\n")

    print("Errors: ", mistake(test1, testinp))

  elif chk == "n":
    print(" Thanks for playing")

  else:
    print("Wrong input")