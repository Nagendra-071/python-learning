import win32com.client

# Initialize SAPI.SpVoice
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# List available voices
voices = speaker.GetVoices()
for i in range(voices.Count):
    print(f"Voice {i}: {voices.Item(i).GetAttribute('Name')}")

# Set a specific voice (e.g., first voice)
speaker.Voice = voices.Item(1)

# Speak text
l=[]
n=int(input("Enter no. of people you want to give shout out : "))
for i in range(1,n+1) :
    name=input(f"Enter  name {i} :  ")
    l.append(name)

for s in l:
      speaker.Speak(f"Shoutout to {s}")
      print(f"Shoutout to {s}")
      