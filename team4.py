####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '1080Tis'
strategy_name = 'B for a B'
strategy_description = 'Tit for Tat'
    
def wrongmove():
    return 'c'
    
def goodmove():
    return 'b'
friend = False
final = False
def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0 or len(my_history) == 1 or len(my_history) == 2 or len(my_history) == 4:
        wrongmove
    elif len(my_history) == 3:
        goodmove
    elif their_history[0] == 'c' and their_history[1] == 'c' and their_history[2] == 'c' and their_history[3] == 'b' and their_history[4] == 'c':
        if len(my_history) > 14:
            for n in range(len(10)):
                if their_history[n+4] == 'b':
                    if their_history[-1] == 'c':
                        wrongmove
                    else: 
                        goodmove
                else:
                    goodmove
        else:
            wrongmove
    else:
        if their_history[-1] == 'c':
            wrongmove
        else:
            goodmove
            
            
    
    
    
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''   