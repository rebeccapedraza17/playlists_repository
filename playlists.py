# Rebecca Pedraza
# Nov 8

# Make a list of at leats 5 songs

songs = ["A","B","C","D","E"]

def button1():
    songs.append(songs.pop(0))
    
def button2():
    songs.insert(songs.pop(-1))

def button3():
    songs.insert(songs.pop(1))

def button4():
    random.shuffle(songs)

def button5():
    for i in range(len(songs)):
        print(songs[i])

# Ask user to input a choice between 1 & 5
# Explain what each button does
input("""You are going to choose a number between 1 and 5
1 will move the...
2 will...
3 will...
4 will...
you can repeat 1-4 as many times
5 will play the songs in the...""")

option = ''
while option != '5':
    if option == '1':
        button1()
    elif option == '2':
        button2()
    elif option == '3':
        button3()
    elif option == '4':
        button4()
    elif option == '5':
        continue
    else:
        print("That is an invalid input, try again")
        
        
'''  
    # 1: Move first song to end
    songs.append(songs(0))
        
    # 2: Move last song to beginning
    songs.insert(0,songs[-1])
    songs.pop(-1)
    
    # 3: Swap the first two songs
        
    
    # 4: Shuffle the playlist
    for song in songs:
        print(song)


    # 5: Play (print each song on separate line)

'''


