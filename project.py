import random

import tkinter as tk

qorange=['Great Whites and Hammerheads are what type of animals?',\
    'According to legend, who led a gang of merry outlaws in Sherwood Forest in Nottingham, England?',\
    'How many legs does a spider have?','What is the name of the pirate in Peter Pan?',\
    'He’s “smarter than the average bear”, but what’s the name of the most famous resident of Jellystone Park?',\
    'How many rings make up the symbol of the Olympic Games?',\
    'According to the Dr. Seuss book, who stole Christmas?',\
    'In which continent is the country of Egypt found?',\
    'What is a brontosaurus?',\
    'Scooby Doo and his friends travel around in which vehicle?']

aorange=['Sharks','Robin Hood','Eight','Captain Hook','Yogi Bear','Five','The Grinch',\
    'Africa','A dinosaur','The Mystery Machine']

qblue=['Which war movie won the Academy Award for Best Picture in 2009?',\
       'What was the name of the second Indiana Jones movie, released in 1984?',\
       'Which actor starred in the 1961 movie The Hustler?',\
       'In which year were the Academy Awards, or “Oscars”, first presented?',\
       '“After all, tomorrow is another day!” is the last line from which movie that won the Academy Award for Best Picture in 1939?',\
       'Which movie features Bruce Willis as John McClane, a New York police officer, taking on a gang of criminals in a Los Angeles skyscraper on Christmas Eve?',\
       'What is the name of the hobbit played by Elijah Wood in the Lord of the Rings movies?',\
       'Which actress plays Katniss Everdeen in the Hunger Games movies?',\
       'Judy Garland starred as Dorothy Gale in which classic movie?',\
       'What is the name of the kingdom where the 2013 animated movie Frozen is set?']

ablue=['The Hurt Locker','Indiana Jones and the Temple of Doom','Paul Newman',\
       '1929','Gone with the Wind','Die Hard','Frodo Baggins','Jennifer Lawrence',\
       'The Wizard of Oz','Arendelle']

qred = [
'What is the capital of the United States of America? ',\
'Who is the current president of the United States of America? ',\
'What is the capital of Nigeria? ',\
'Muhammadu Buhari is the president of which country? ',\
'Uhuru Kenyatta is the president of which country? ',\
'What is the capital of France? ',\
'Which state has only one neighbor? ',\
'Where is Amsterdam located? ',\
'Emmanuel Macron is the president of which country? ',\
'Sir Alex Ferguson until his retirement coached which team?']

ared= [ 'Washington DC','President Donald Trump','buja','Nigeria','Kenya',\
'Paris','Maine','Netherland','France','Manchester United']



qs=[qorange,qblue,qred]

def starter():
	(i,j)=(0,0)
	x = random.randint(0,9)
	y = random.randint(0,2)
	return qs[y].pop(x)

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

frame = tk.Frame(root, bg='#50c1ff', bd=5)
frame.place(relx=0,rely=0, relwidth=1,relheight=1)

answer=['white','green','red']


button = tk.Button(frame, text="Start the game!", bg='gray',fg='red')
button.place(relx=0.45,rely=0.5)

stats = tk.Label(frame, text='Player: {} \n Points: {}', bg='yellow')
stats.place(relx=0.4)

question = tk.Label(frame, text=starter())
question.place(x=0.5,rely=0.2, relwidth=1, relheight=0.1)

entry=tk.Entry(frame, bg='white')
entry.place(relx=0.3,rely=0.9,relwidth=0.4,relheight=0.08)

#background_image= tk.PhotoImage(file="trivia.jpg")
#background_label= tk.label(root, image='background_image')
#background_label.place(x=0,y=0,relwidth=1,relheight=1)




color = ('Orange','Blue','Red','Green','Yellow','White')
rand1 = random.randint(0,5)
rand2 = random.randint(1,4)

die = color[rand1]
qrand = random.randint(0,9)

(player1,player2,player3,player4)=(0,0,0,0) # initial points
       


root.mainloop()
