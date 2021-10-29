def input_check():
    x=input("Quidditch, QBR, Gymnast").lower().replace(" ", "")
    if x=="quidditch" or x=="qbr" or x=="gymnast":
        return x
    else:
        print("please try again and select one of")
        input_check()

def quidditch_calc():
    try:
        goals = float(input("how many goals were scored"))
        snitch = input("was the snitch caught, respond Yes or No").lower().replace(" ", "")
        goals=(goals/2)*2
    except:
        print("the input for goals was not a number, please try again and use a number for goals")
        print()
        quidditch_calc()
    if snitch == "yes":
        return goals*10 +30
    elif snitch =="no":
        return goals*10
    else:
        print("you did not type yes or no for the snitch, please try again and type either yes or no")
        print()
        quidditch_calc()

def qbr_calc():
    try:
        attempts = float(input("please input the number of attempts"))
        if attempts==0:
            print("the QB cannot have 0 attempts, if the QB had 0 attempts they cant have a QBR please try again")
            qbr_calc()
        completions = float(input("please input the number of completions"))
        interceptions = float(input("please input the number of interceptions"))
        passing_yards = float(input("please input the number of passing yards"))
        touchdown_passes = float(input("please input the number of touchdown_passes"))
        x=100*(5*(completions/attempts-0.3) + 0.25*(passing_yards/attempts - 3) +20*(touchdown_passes/attempts)+ 2.375 -(25 * interceptions/attempts)) / 6
    except:
        print("not all of your inputs were numbers, please try again and use only numbers and decimals")
        print()
        qbr_calc()
    return x


def gymnast_calc():
    try:
        diffscore=float(input("please give the difficulty score"))
        oneex=float(input("please give the first execution score "))
        twoex=float(input("please give the first execution score "))
        threeex=float(input("please give the first execution score "))
        fourex=float(input("please give the first execution score "))
        fiveex=float(input("please give the first execution score "))
        arr=[oneex,twoex,threeex,fourex,fiveex]
        arr.sort()
        score=(arr[1] + arr[2] + arr[3]) * diffscore
    except:
        print("one or more of your values you entered was not a number, please try again")
        gymnast_calc()
    return score



def main():
    print("please pick the sport you want to calculate")
    sport=input_check()
    if sport == "quidditch":
        quidscore=quidditch_calc()
        print("the score was: "+ str(quidscore))
    elif sport == "qbr":
        qbr=qbr_calc()
        print("The qbr is: " + str(qbr))
        if qbr >158.3:
            print("The QB is a perfect passer")
        else:
            print("The QB is not a perfect passer")
    elif sport == "gymnast":
        gymscore=gymnast_calc()
        print("the total score was:"+ str(gymscore))

main()
