import moviepy as mpy
import moviepy.editor as editor
import os
import FileManager as fManager

def ManuallyMakeClip():
  print("Outcome clip name")
  clipName = input()

  if(os.path.isfile("Final Clips/" + clipName + ".mp4")):
    print("There is a file with this name\nDo you want to replace it? yes/no")
    x = input()
    if(x != "yes" and x != "Yes" and x != "y"): return

  CreateVideo(clipName + ".mp4")

def Clip(outcomeName):
  if(os.path.isfile("Final Clips/" + outcomeName + ".mp4")):
    print("There is a file with name : " + outcomeName + ".mp4\nCreation of video cancelled to not lose data...")
    return False
  return CreateVideo(outcomeName + ".mp4")

def CreateVideo(outcomeTitle):
  oneLiner = fManager.PickOneLiner()
  if(not oneLiner):
    print("out of prompts!!!")
    return False

  # assigning data
  scenery , mood, message = oneLiner
  image = fManager.PickBackground(scenery)
  music = fManager.PickMusic(mood)

  if(image == None or music == None):
    print("no music or video!!!")
    return False

  # find video, audio and connect them
  audioClip = editor.AudioFileClip(music)
  videoClip = editor.ImageClip(image, duration=audioClip.duration)
  videoClip.audio = audioClip

  # resizing to fit phone res
  vidWidth, vidHeight = videoClip.size
  newWidth = (vidHeight/16) * 9
  videoClip = mpy.video.fx.crop(videoClip, x_center=vidWidth/2, y_center=vidHeight/2, width=newWidth, height = vidHeight)
  videoClip = videoClip.resize((900,1600))

  # adding text
  videoClip = AddDropShadowSubtitle(videoClip, message, videoClip.duration)

  # adding video effects
  videoClip = ChangeBrightness(videoClip , -30, -0.25)
  videoClip = AddFadeEffects(videoClip, 2.5, 2.5)

  videoClip.write_videofile("Final Clips/" + outcomeTitle, fps = 24)
  if(os.path.isfile("Final Clips/" + outcomeTitle)): return True
  return False

def AddSubtitle(message, duration, yPos = 0.3):
  txtClip = editor.TextClip(message, font = 'Segoe-UI-Bold', color='white', font_size = 90)
  txtClip = txtClip.with_position(('center', 1600 * (1-yPos)))
  txtClip = txtClip.with_duration(duration)
  return txtClip

def AddDropShadowSubtitle(video, message, duration, offset = 6, yPos = 0.3):
  txtClip = editor.TextClip(message, font = 'Segoe-UI-Bold', color='white', font_size = 90)
  xSize = txtClip.size[0] + offset
  xMiddle = (900 - xSize)/2
  txtClip = txtClip.with_position((xMiddle, 1600 * (1-yPos)))
  txtClip = txtClip.with_duration(duration)

  dropShadow = editor.TextClip(message, font = 'Segoe-UI-Bold', color='black', font_size = 90)
  dropShadow = dropShadow.with_position((xMiddle + offset, 1600 * (1-yPos) + offset))
  dropShadow = dropShadow.with_duration(duration)
  dropShadow = dropShadow.with_opacity(75)
  return mpy.CompositeVideoClip([video, dropShadow, txtClip])

def ChangeBrightness(video, brightness = 1, colorContrast = 1):
  newVid = mpy.video.fx.lum_contrast(video , lum=brightness, contrast = colorContrast)
  return newVid

def AddFadeEffects(video, inDuration = 2, outDuration = 2):
  vidIn = mpy.video.fx.fadein(video, inDuration)
  vidOut = mpy.video.fx.fadeout(vidIn, outDuration)
  return vidOut