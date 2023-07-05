import random
Hello = ('hello', 'hey','hi', 'hey jarvis', 'hi jarvis', 'hello jarvis')
reply_Hello = ('Hello Sir, I Am Jarvis', "Hello Sir, Nice To meet you again")

Bye = ('bye', 'exit','sleep', 'go')
reply_Bye = ('Bye Sir',"It will be Nice to meet you","Bye", "Thanks for using me", "Okay Sir, Bye")

How_are_you = ("how are you", 'how are you jarvis', 'are you fine jarvis')
reply_how = ("I am Fine Sir, How about you?","I am Good Sir, tell me about you?", "I am Absolutely fine Sir",
             "I'am Fine", "Thanks for Asking, I'am Fine")
I_am_fine = ("yeah i am also good", "yeah i am also fine", "yeah i am good","yeah i am fine","i am also good")
reply_I_am_fine = ("That's Good Sir , Tell me if you have any work for me?", "That's Greate Sir, Tell me if you have any work for me?")

who_are_you = ('who created you jarvis', 'who is your developer', 'tell me about yourself', 'who are you', 'who made you jarvis')
reply_who = ("I'm your virtual Assistant Jarvis, Created by BLS (Bheru Lal Sahu) and i can help you if you need.")

nice = ('nice jarvis', 'good job jarvis','thanks jarvis')
reply_nice =('Thanks', "Ohh, It's Okay", "Thanks to you")

functions = ['jarvis what things can you do','function', 'abilities', 'what can you do', 'what is your abilities', 'tell me your features']
reply_functions = ("I Can Perform many task or varieties of tasks such as Google Crome Automation, YouTube Automation, Notepad Automation, WhatsApp Automation, Google Map Automation, Calculation and Many more,  How Can I help you")

sorry_reply = ("Sorry, That's Beyond my abilities","Sorry, I can not do that","Sorry, That's above me","Sorry, I am not Programmed for that")

birthday = ("jarvis what is your birth date","jarvis when will be your birthday","what is your birth date jarvis","tell me your date of birth jarvis")
reply_birthday = ("I do not have a Birth date", "As an virtual assistant i do not have birthday to celebrate")

def ChatterBot(Text):
    Text = str(Text)
    
    if Text in Hello:
        reply = random.choice(reply_Hello)
        return reply
    elif Text in Bye:
        reply = random.choice(reply_Bye)
        return reply
    elif Text in How_are_you:
        reply = random.choice(reply_how)
        return reply
    elif Text in I_am_fine:
        reply = random.choice(reply_I_am_fine)
        return reply
    elif Text in nice:
        reply = random.choice(reply_nice)
        return reply
    elif Text in functions:
        reply = random.choice(reply_functions)
        return reply
    elif Text in who_are_you:
        reply = random.choice(reply_who)
        return reply
    else:
        return random.choice(sorry_reply)

