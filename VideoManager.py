import OneLinerGenerator as oneGen
import os

maxVideosAtOnce = 10

def StartManager():
  print("What would you like to do?")
  print("--commands--")
  print("oneliner")
  print("quit")
  print("---")
  while(True):
    option = input("input : ")
    match(option):
      case "oneliner":
        amount = (int)(input("How many videos do you want to compile? : "))
        if(amount < 1): amount = 1
        if(amount > maxVideosAtOnce): amount = maxVideosAtOnce
        print("creating " + str(amount) + " oneLiner videos...")
        MakeOneLiner(amount)
      case "quit":
        break
      case "q":
        break

def MakeOneLiner(amount = 1):
  f = open("Data/OneLinerNumber.txt","r")
  epizode = (int)(f.readline())
  f.close()

  startAmount = amount

  success = True
  while amount != 0 and success:
    success = oneGen.Clip("minecraft nostalgia " + str(epizode))
    if(success): epizode+=1
    amount -= 1

  print("Videos made " + str(startAmount - amount) + "/" + str(startAmount))

  w = open("Data/OneLinerNumber.txt","w")
  w.write(str(epizode))
  w.close()
  return success

if(__name__ == "__main__"):
  StartManager()