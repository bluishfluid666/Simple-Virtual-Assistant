import speech_recognition
import pyttsx3
from datetime import date, datetime
robot_verbal = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()

while True:
	with speech_recognition.Microphone() as mic:
		#how to make our va say Im listening
		print("VA: Im listening")
		print("VA: ...")
		audio=robot_ear.listen(mic)

	try: 
		you = robot_ear.recognize_google(audio)
	except:
		you =""

	print("You:\t" + you)

	if you == "":
		robot_brain="Im on yo ass"
	elif "hello" in you:
		robot_brain = "what's good?"
	elif "what a beautiful" in you:
		robot_brain = "We like those!"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain=now.strftime("%H : %M : %S")
	elif "current date and time" in you:
		now = datetime.now()
		robot_brain=now.strftime("%B %d, %Y %H:%M:%S")
	elif "bye" in you:
		robot_brain="see you some time K"
		robot_verbal.say(robot_brain)
		robot_verbal.runAndWait()
		break	
	else: 
		robot_brain="Im fine, glad you ask"
	print("VA:\t" + robot_brain)
	robot_verbal.say(robot_brain)
	robot_verbal.runAndWait()

