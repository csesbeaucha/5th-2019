team_name = 'yoink'
strategy_name = 'hive mind'
strategy_description = 'it decides whether you are friend or foe. If you are foe, you will be decimated. If you are friend, you will be elevated.'
    
flag = False   
flag2 = False
         
def move(my_history, their_history, my_score, their_score):
    
    global flag
    global flag2
    
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
        for i in range(5):
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
    return