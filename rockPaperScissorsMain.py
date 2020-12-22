import random

def declareWinner(hScore,cScore,name):
    if(hScore>cScore):
        print(name, "wins! Final score:",hScore,"vs",cScore)
    elif(cScore>hScore):
        print("Computer wins!Final score:",cScore,"vs",hScore)
    else:
        print("Tie Game!")
    print("\nThanks for playing!")
    
def main():
    name = input("Enter contestant's name:")
    hCont=Human(name)
    cCont=Computer("Computer")
    
    for i in range(3):
        turn = input("Enter rock (r), paper (p), or scissor (s) to take your turn.\n")
        hCont.takeTurn(turn)
        cCont.takeTurn()
        if((hCont._turn == 'r' and cCont._turn == 'p') or
          (hCont._turn == 'p' and cCont._turn == 'r' )):
          print("paper wins => ", end = "")
          result = "p"
             
        elif((hCont._turn == 'r' and cCont._turn == 's') or
            (hCont._turn == 's' and cCont._turn == 'r')):
            print("Rock wins =>", end = "")
            result = "r"
        elif((hCont._turn == cCont._turn)):
            result = "Tie"
        else:
            print("scissor wins =>", end = "")
            result = "s"
     
        # Printing either user or computer wins
        if result == hCont._turn:
            hCont._score+=1
            print(name," wins round ",i+1)
        elif result == cCont._turn:
            cCont._score+=1
            print("Computer wins round",i+1)
        else:
            print("Round ", i+1, " ends in a tie.")
    declareWinner(hCont._score, cCont._score, hCont._name) 
    
               
   

class Contestant:
    def __init__(self, name,score=0):
        self._name=name
        self._score=score
       
    def setName(self, name):
        self._name=name
       
class Human(Contestant):
    def takeTurn(self, turn):
        self._turn=turn
   
    def getTurn(self):
        return self._turn
       
   
class Computer(Contestant):
    def takeTurn(self):
        randomChoice = random.randint(1,3)
        if (randomChoice==1):
            self._turn="r"
        elif (randomChoice==2):
            self._turn="p"
        else:
            self._turn="s"
        print(self._turn)
   
    def getTurn(self):
        return self._turn
       
       
main()