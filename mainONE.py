import random

balance = [0, 1000, 2000, 4000, 8000, 15000, 30000, 40000, 50000, 80000, 100000, 200000, 300000, 600000, 800000,
           1000000]
lvl = 0
correct_answer = ""
q = []


def intro(lvl):
    """ Generates introduction to the new question """
    lvl += 1
    bal = balance[lvl]
    v = [0 for i in range(9)]
    v[0] = "Here is question #%s worth $%s." % (lvl, bal)
    v[1] = "We're going to question #%s for you to win $%s." % (lvl, bal)
    v[2] = "Question #%s for $%s now." % (lvl, bal)
    v[3] = "This is the turn of question #%s that will get you $%s." % (lvl, bal)
    v[4] = "Now it is the turn of question #%s. Win $%s!" % (lvl, bal)
    v[5] = "Want $%s? Let's see how you can cope with question #%s!" % (bal, lvl)
    v[6] = "Let's see how much time it'll take you to answer question #%s and win $%s!" % (lvl, bal)
    v[7] = "Now onto question #%s. It is worth $%s." % (lvl, bal)
    v[8] = "Want go win $%s? Here's question #%s." % (bal, lvl)
    n = int(random.random() * 9)
    return v[n]


def checker(lvl):
    answer = input("\n You: ")
    answer = answer.lower()
    global correct_answer, q

    if (answer == "a" or answer == "b" or answer == "c" or answer == "d"):
        if (correct_answer == q[ord(answer) - 96]):
            if (lvl == 14):
                print(" ******* CONGRATULATIONS, %s! *************" % player.upper())
                print(" **********  YOU WON $1,000,000! *************")
                print(" You reached the top! This was an excellent game! Once again, congratulations!")
            else:
                print("\n You got it right, %s!\n You now have $%s.\n Let's proceed to question #%s!" % (
                    player, balance[lvl + 1], lvl + 2))
                print(question(lvl + 1))
                checker(lvl + 1)

        else:
            print("\nOops. The answer you chose is incorrect.The right answer is %s." % correct_answer)
            print("Don't worry, you will get " + str(balance[lvl] / 4) + " as consolation award.")
            print("Thank you for the game!")
            quit()


def questionBank_Easy(n, t):
    return a[n][t]


a = [[0 for i in range(10)] for i in range(15)]

a[0][0] = ["Which fictional character lives at 221b Baker Street?", "Harry Potter", "Sherlock Holmes",
           "Winnie the Pooh", "Mickey Mouse", "Sherlock Holmes"];
a[0][1] = ["Which river flows though London?", "Thames", "Yangtze", "Seine", "Danube", "Thames"]
a[0][2] = ["Which Italian city is famous for its leaning tower?", "Rome", "Pisa", "Florence", "Bologna", "Pisa"]
a[0][3] = ["What does the F stand for in FBI?", "Fishtails", "Figures", "Federal", "Federation", "Federal"]
a[0][4] = ["What color is the M in McDonald's?", "red", "orange", "white", "yellow", "yellow"]
a[0][5] = ["What is the Aloha state?", "Delaware", "Florida", "Alaska", "Hawaii", "Hawaii"]
a[0][6] = ["George Orwell wrote this book, which is often considered a statement on government oversight.",
           "1984", "Cuba", "Germany", "Jamaica", "Germany"]
a[0][7] = ["In which country is the Great Barrier Reef located?", "Eat it", "Play it", "Sit on it", "Wear it",
           "Wear it"]
a[0][8] = ["What is the most widely spoken language in Brazil?", "Train", "Plane", "Car", "Bike", "Plane"]
a[0][9] = ["What month does the Russian Orthodox celebrate Christmas?", "Flowers", "Trees", "Steam rollers", "Fish",
           "Fish"]

a[1][0] = ["Which is not a type of antelope?", "Gorilla", "Gerenuk", "Gemsbok", "Gnu", "Gorilla"]
a[1][1] = ["What is rioja a type of?", "Bread", "Vegetable", "Wine", "Nut", "Wine"]
a[1][2] = ["Germania was the Roman name for which modern-day European country?", "France", "Austria", "Germany",
           "Spain", "Germany"]
a[1][3] = ["What was the UK's top paying attraction of 2002?", "London Nose", "London Mouth", "London Eye",
           "London Ear", "London Eye"]
a[1][4] = ["Which of these geographical features is a mountain?", "Kilimanjaro", "Danube", "Amazon", "Nile",
           "Kilimanjaro"]
a[1][5] = ["Which of these is a popular form of music?", "Country & Eastern", "Kingdom & Northern", "Land & Southern",
           "Country & Western", "Country & Western"]
a[1][6] = ["Which of these is a common term for a programme of physical exercises?", "Stay able", "Remain trim",
           "Continue competent", "Keep fit", "Keep fit"]
a[1][7] = ["What is the name of the instrument panel in a car?", "Chargeboard", "Sprintboard", "Dashboard", "Jogboard",
           "Dashboard"]
a[1][8] = ["What copy can be said to describe something identical?", "Oxygen", "Hydrogen", "Nitrogen", "Carbon",
           "Carbon"]
a[1][9] = ["Which is a chain of international hotels?", "Four Tops", "Four Pennies", "Four Seasons", "Four Posters",
           "Four Seasons"]

a[2][0] = ["Which of these is a spicy Indian dish?", "Spaghetti", "Biriani", "Bellini", "Crostini", "Biriani"]
a[2][1] = ["Which country is not crossed by the Arctic Circle?", "Norway", "Finland", "Greece", "Sweeden", "Greece"]
a[2][2] = ["In which film must a bus keep travelling at 50 miles per hour so that it does not explode?", "Speed",
           "Velocity", "Tempo", "Thrust", "Speed"]
a[2][3] = ["An older person is sometimes described as 'long in the ...'?", "Tooth", "Eye", "Hair", "Nose", "Tooth"]
a[2][4] = ["According to the saying, which of these is 'a dish best served cold'?", "Revenge", "Cottage pie", "Custard",
           "Stew", "Revenge"]
a[2][5] = ["To know the rudiments of a subject is to 'know your ...'?", "ABC", "HIJ", "KLM", "QRS", "ABC"]
a[2][6] = ["Which of these is a butter substitute made with vegetable oils?", "Margaret", "Margarine", "Margarita",
           "Margate", "Margarine"]
a[2][7] = ["Complete the title of the 2003 Disney release, 'Pirates of the ...'?", "Black Sea", "Atlantic",
           "English Channel", "Caribbean", "Caribbean"]
a[2][8] = ["Which of these countries did not host a Formula 1 Grand Prix race in 2003?", "Monaco", "France", "Italy",
           "Madagascar", "Madagascar"]
a[2][9] = ["Which is not a recognized playing surface for tennis?", "Grass", "Linoleum", "Clay", "Cement", "Linoleum"]

print(" *************************************************")
print(" *            //     Who Wants     \\\            *")
print(" *            ||      To Be A       ||            *")
print(" *            \\\    MILLIONAIRE    //            *")
print(" *************************************************\n")

print(" Welcome to \"Who Wants to Be a Millionaire!\"\n")

while True:
    print("           //    (1) Play the Game      \\\           \n")
    print("         ||    (2) View the High Scores    ||           \n")
    print("           \\\    (3) Quit Game          //           \n")

    option = int(input("Where would you want to go? Choose a number: "))
    if option == 1:
        player = input("What is your name?: ")
        print("\nLet's start the game, %s! There will be 15 questions that are arranged by difficulty." % (player))
        print(
            "Simpler questions go first and are worth less. Every question will have four answer choices, of which only one is correct.")
        print("Answering the hardest, 15th question, will make you a winner of $1,000,000! So let's get started!\n")


        def question(lvl):
            to_return = "\n " + intro(lvl) + "\n "
            to_return += "=" * (len(to_return) - 3) + "\n "
            qnum = int(random.random() * 10)

            global q
            q = questionBank_Easy(lvl, qnum)
            to_return += q[0]
            to_return += "\n A. " + q[1] + "\t\t B. " + q[2]
            to_return += "\n C. " + q[3] + "\t\t D. " + q[4]

            global correct_answer
            correct_answer = q[5]
            return to_return

            # pregameeeeee
            while lvl > 1:
                print("(1)    Continue")
                print("(2)    Walk away with earnings")
                prequestion_Option = input("What would you do? Choose a number: ")
                if prequestion_Option == 1:
                    pass
                elif prequestion_Option == 2:
                    print("You have chosen to give up. You now have " + str(balance[lvl]))
                    quit()

            while lvl > 1:
                print("(1)    Choose now")
                print("(2)    Use the lifeline")
                print("(3)    Walk away with half the earnings")
                postquestion_Option = input("What would you do? Choose a number: ")
                if postquestion_Option == 1:
                    pass
                elif postquestion_Option == 2:
                    if lvl = 15:
                        pass
                    else:
                        print("(1)    Call a Friend")
                        print("(2)    50/50")
                        lifeline_Option = input("What would you do? Choose a number: ")
                        if lifeline_Option == 1:
                            if (help_friend_avail == True):
                                help_friend_avail = False
                                if (
                                        random.random() < 0.7):  # There is a ~70% chance that friend's guess will be the right one
                                    lets_wait("Calling your friend", 4)
                                    print("\n Your friend thinks the correct answer is %s." % correct_answer)
                                    check_answer(lvl)
                                else:  # In case two answers were eliminated by 50:50
                                    while True:
                                        i = int(random.random() * 4 + 1)
                                        if (q[i] != "" and q[i] != correct_answer):
                                            lets_wait("Calling your friend", 4)
                                            print("\n Your friend thinks the correct answer is %s." % correct_answer)
                                            check_answer(lvl)
                            else:
                                print(
                                    "\n You already used this lifeline. Enter 'help' to see what other lifelines are left.")
                                check_answer(lvl)
                        elif lifeline_Option == 2:
                            if (help_50_avail == True):
                                help_50_avail = False
                                w = 0  # To track how many answers have been removed
                                while True:
                                    if w == 2:
                                        break
                                    i = int(random.random() * 4 + 1)
                                    if (correct_answer != q[i] and q[i] != ""):
                                        w += 1
                                        q[i] = ""

                                print("\n We eliminated two incorrect answers. The two remaining are:")
                                temp = [" A. ", " B. ", " C. ", " D. "]
                                for i in range(1, 5):
                                    if (q[i] != ""):
                                        print(temp[i - 1] + q[i] + "\t\t"),
                                print("")
                                check_answer(lvl)

                            else:
                                print(
                                    "\n You already used this lifeline. Enter 'help' to see what other lifelines are left.")
                                check_answer(lvl)
                elif postquestion_Option == 3:
                    print("You have chosen to give up. You now have " + str(balance[lvl] / 2))
                    quit()


        print(question(0))
        checker(0)

        break
    elif option == 2:
        import shelve

        scoreFile = shelve.open('score.txt')


        def updateScore(newScore):
            if ('score' in scoreFile):
                score = scoreFile['score']
                if (newScore not in score):
                    score.insert(0, newScore)

                score.sort()
                ranking = score.index(newScore)
                ranking = len(score) - ranking
            else:
                score = [newScore]
                ranking = 1

            print(score)
            print(ranking)
            scoreFile['score'] = score
            return ranking


        newScore = int(input("New HighScore: \n"))
        updateScore(newScore)
    elif option == 3:
        break