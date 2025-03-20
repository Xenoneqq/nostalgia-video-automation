import os
import random

screenPath = "Data/Assets/Screens"
musicPath = "Data/Assets/Music Cut"

def GetAllOneLiners():
  oneLineFile = open("Data/Assets/Prompts/OneLiners.txt",'r')
  prompts = []; promptID = 0
  while True:
    line = oneLineFile.readline()
    if(not line): break
    if(len(line) == 1): continue

    setting = line[:-1]
    line = oneLineFile.readline()
    mood = line[:-1]
    line = oneLineFile.readline()
    text = ""
    while(line and len(line) != 1):
      text += line
      line = oneLineFile.readline()
    
    prompts.append(None)
    prompts[promptID] = (setting, mood, text[:-1])
    promptID += 1
  oneLineFile.close()
  return prompts

def AddOneLinerToUsed(promptSet):
  oneLinerFile = open("Data/Assets/Prompts/OneLinersUsed.txt",'a')
  oneLinerFile.write(promptSet[2] + "\n\n")
  oneLinerFile.close()

def UpdateOneLiners(prompts):
  oneLinerFile = open("Data/Assets/Prompts/OneLiners.txt",'w')
  for x in prompts:
    oneLinerFile.write(x[0]+'\n')
    oneLinerFile.write(x[1]+'\n')
    oneLinerFile.write(x[2]+"\n\n")
  oneLinerFile.write("\n\n\n")
  oneLinerFile.close();

def PickOneLiner():
  prompts = GetAllOneLiners()
  if(len(prompts) == 0): return None
  id = random.randint(0, len(prompts)-1)
  oneLiner = prompts[id]
  AddOneLinerToUsed(oneLiner)
  prompts.pop(id)
  UpdateOneLiners(prompts)
  return oneLiner

def PickBackground(scenery):
  images = os.listdir(screenPath + "/" + scenery)
  if(not images or len(images) == 0): return None
  return screenPath + "/" + scenery + "/" + images[random.randint(0,len(images)-1)]

def PickMusic(mood):
  music = os.listdir(musicPath + "/" + mood)
  if(not music or len(music) == 0): return None
  return musicPath + "/" + mood + "/" + music[random.randint(0,len(music)-1)]