print('''
                                                     _..----.._
                                                    ]_.--._____[
                                                  ___ | '--'__.. | --._
                              __               """    ;            :
                            ()_ """"---...__.'""!": / ___:
                               """---...__\]..__] | /    [ 0 ]      :
                                          """!- -. / /      """        :
                                   __  ...._____;""'.__________..--..:_
                                  /  !"''''''!''''''''''|''''/' ' ' ' \"--..__  __..
                                 /  /.--.    |          |  .'          \' ' '.""--.{'.
             _...__            >=7 //.-.:    |          |.'             \ ._.__  ' '""'.
          .-' /    """"----..../ "">==7-.....:______    |                \| |  "";.;-" >
          """";           __.."   .--"/"""""----...."""""----.....H_______\_!....'----""""]
        _..--- | ._ __..--""       _!. -= _.            """""""""""""""                   ;"""
       /   .-";-.'--...___     ." .-""; ';""-""-...^..__...-v.^___,  ,__v.__..--^"--""-v.^v,      
      ;   ;   |'.         """-/ ./;  ;   ;\P.        ;   ;        """"____;  ;.--""""// '""<,     
      ;   ;   | 1            ;  ;  '.: .'  ;<   ___.-'._.'------""""""____'..'.--""";;'  o ';     
      '.   \__:/__           ;  ;--""()_   ;'  /___ .-" ____---""""""" __.._ __._   '>.,  ,/;     
        \   \    /"""<--...__;  '_.-'/; ""; ;.'.'  "-..'    "-.      /"/    `__. '.   "---";      
         '.  'v ; ;     ;;    \  \ .'  \ ; ////    _.-" "-._   ;    : ;   .-'__ '. ;   .^".'      
           '.  '; '.   .'/     '. `-.__.' /;;;   .o__.---.__o. ;    : ;   '"";;""' ;v^" .^        
             '-. '-.___.'<__v.^,v'.  '-.-' ;|:   '    :      ` ;v^v^'.'.    .;'.__/_..-'          
                '-...__.___...---""'-.   '-'.;\     'WW\     .'_____..>."^"-""""""""       
                                      '--..__ '"._..'  '"-;;"""                                   
                                             """---'""""""                    ''')


print("Welcome to Treasure Island.\nYour mission is to find the treasure. ")
step_1 = input(
    "You'r at a cross road. Where do you wand to go? Type \"left\" or \"right\" ")
if step_1.lower() == "right":
    print("Game Over.")

elif step_1.lower() == "left":
    step_2 = input(
        "You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")
    if step_2.lower() == "swim":
        print("Game Over.")
    elif step_2.lower() == "wait":
        step_3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        if step_3.lower() == "red":
            print("Game Over.")
        elif step_3.lower() == "blue":
            print("Game Over.")
        elif step_3.lower() == "yellow":
            print("You win!")
        else:
            print("You entered something wrong!")
    else:
        print("You entered something wrong!")
else:
    print("You entered something wrong!")
