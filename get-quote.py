import random
def primary():
 # print("Keep it logically awesome.")

  f = open("quotes.txt", "a")
  text= "To live is Christ, to die is gain\n"
  f.write(text)
  f.close()


  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()


  last = len(quotes) - 1
  rnd = random.randint(0, last)
  rnd1 = random.randint(0, last)
  print(quotes[rnd].rstrip("\n"),quotes[rnd1].rstrip("\n"))

if __name__== "__main__":
  primary()
