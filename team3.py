team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    flag = False   

flag2 = False

         

def move(my_history, their_history, my_score, their_score):

    

    global flag

    if len(my_history) == 0:

        return 'c'

    if len(my_history) == 1:

        return 'c'

    if len(my_history) == 2:

        return 'c'

    if len(my_history) == 3:

        return 'b'

    if len(my_history) == 4:

        return 'c'

    if len(their_history) == 5:

        counter = 0

        for i in len(their_history):

            for i in len(their_history):

                if my_history[i] == their_history[i]:

                    counter += 1

            if counter == 5:

                flag = True

    if len(their_history) > 5:

        if their_history[-1] == 'c':

           return 'b'

    if len(my_history) <= 11:

        if flag == True:

            return 'c'

        elif flag == False:

            return 'b'

    if flag == False:

        return 'b'

    if len(my_history) >= 11:

        if flag == False:

            return 'b'

        elif flag == True:

            if flag2 == True:

                return 'c'


def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print ('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             