import random

def menu():
    running = True
    truth = ['What is the most embarrassing picture of you?','What would you do if you were the opposite sex for a month?','What is the most expensive thing you have stolen?','What is the most childish thing you still do?','Have you ever cheated or been cheated on?','Tell me about your most awkward date.','What is your deepest darkest fear?','Tell me about your first kiss.','Who is the person you most regret kissing?','What is the most embarrassing thing your parents have caught you doing?','When was the most inappropriate time you farted?','What was the cruelest joke you played on someone?','What is the most embarrassing thing you have put up on social media?','What is the grossest thing you have had in your mouth?','Have you ever had a crush on someone in this room? And who?','If you had the chance to be reborn as someone else, which person would you choose from this room and why?','If you had 24 hours to live, what would you like to do?','With whom would you like to be marooned on an island and why?','If you were granted two wishes, what would you ask for?']
    dare = ['For a guy, put on makeup. For a girl, wash off your make up.','Dance with no music for 1 minute.','Let the group pose you in an embarrassing position and take a picture.','Give the person opposite you your phone and let them send one text to anyone in your contacts.','Lick the floor.','Drink a small cup of a concoction that the group makes.','Sniff the armpits of everyone in the room.','Kiss the person to your left.','Do push ups until you can’t do any more, wait 5 seconds, and then do one more.','Sell a piece trash to someone in the group. Use your best salesmanship.','Switch clothes with someone of the opposite sex in the group for three rounds.','Stick your arm into the trash can past your elbow.','Call an unknown number and tell that person you know where the Chamber of Secrets is.',"Call up a hotel/restaurant and ask if they serve dinosaurs. Also, mention other foods you'd like with the dinosaur.",'Open a bra clasp using your mouth','Prank the local news station and tell them that you’ve seen a giant panda in the forest.','Flash your tits']
    while running == True:
        print('''
1 - Play Game
2 - Add Truths
3 - Add Dares
4 - Display Truths / Dares
5 - Quit''')
        option = input('Choose An Option: ')
        option = errorCheck(option,int,'Choose An Option: ')
        if option == 1:
            main(truth,dare)
        if option == 2:
            add(truth)
        if option == 3:
            add(dare)
        if option == 4:
            print('The Truths are:')
            print(truth)
            print('The Dares Are:')
            print(dare)
        if option == 5:
            print('Warning! This will remove all entered truths / dares')
            cont = input('Do you wish to continue playing? ').upper()
            if cont == 'NO' or cont == 'N':
                running = False

def add(varName):
    newVarName = input('What do you wish to add? ')
    varName.append(newVarName)
    return varName

def main(truth,dare):
    player = input('How Many Players Are There? ')
    player = errorCheck(player,int,'How Many Players Are There? ')
    rounds = input('How Many Rounds Do You Wish To Play? ')
    rounds = errorCheck(rounds,int,'How Many Rounds Do You Wish To Play? ')
    totalPlayer = player
    for i in range(0,rounds):      
        while player > 0:
            tod = input('Truth or Dare? ').upper()
            if tod == 'TRUTH':
                randTruth = random.randint(0,len(truth)-1)
                print('')
                print(truth[randTruth])
                print('')
                had = input('Already Had It? Re-roll? ').upper()
                if had == 'YES':
                    randTruth = random.randint(0,len(truth)-1)
                    print('')
                    print(truth[randTruth])
                    print('')
                player = player - 1
            elif tod == 'DARE':
                randDare = random.randint(0,len(dare)-1)
                print('')
                print(dare[randDare])
                print('')
                had = input('Already Had It? Re-roll? ').upper()
                if had == 'YES':
                    randDare = random.randint(0,len(dare)-1)
                    print('')
                    print(dare[randDare])
                    print('')
                player = player - 1
            else:
                tod = input('Truth or Dare? ').upper()
        player = totalPlayer
    menu()

def errorCheck(varName, type, question):
    x=0
    while x == 0:
        try:
            varName=type(varName)
            x=1
        except ValueError:
            varName = input(question)
    return varName

menu()

