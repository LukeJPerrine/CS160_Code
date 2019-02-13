# Boy vs Girl Average Score Assignment

# Initial Declaration because Pycharm hates me
bcount = 0
gcount = 0
bosc = 0
gosc = 0
bavg = 0
gavg = 0

# Simple while loop that breaks upon the 'q' input
while True:
    gender = input('Boy (b), Girl (g), or Quit (q) : ')

    # q input to print averages and break loop.
    # Brain says the quit command should be first, not sure why.
    if gender == 'q':
        print('Boy Average Score is:', bavg ,
              'Girl Average Score is:', gavg)
        break

    # Adds to boy average and counts
    elif gender == 'b':
        bsc = input('Boy score: ')
        bsc = int(bsc)
        bcount = bcount + 1
        bosc = bosc + bsc
        bavg = bosc / bcount

    #Adds to girl averages and counts
    elif gender == 'g':
        gsc = input('Girl score: ')
        gsc = int(gsc)
        gcount = gcount + 1
        gosc = gosc + gsc
        gavg = gosc / gcount

    #Error out if Invalid
    else:
        print('Invalid input, please try again or type q to quit')