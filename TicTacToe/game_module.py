from player_module import Player

class TicTacToe:
    def __init__(self, players:list) -> None:
        self.rows=[[1,2,3],[4,5,6],[7,8,9]]
        self.players=players
        self.turn=self.players[0]
        self.win=None
        self.draw=None
    
    def print(self) -> None:
        print("""
            ___ ___ ___
           | {} | {} | {} |
            ___ ___ ___ 
           | {} | {} | {} |
            ___ ___ ___
           | {} | {} | {} |
            ___ ___ ___
            """.format(*[sign for row in self.rows for sign in row]))

    def check_winner(self) -> bool :
        winner_status=False
        for i in range(len(self.rows)):
            if self.rows[i][0] == self.rows[i][1] == self.rows[i][2]:
                self.win=self.turn.name
                winner_status=True
        for j in range(len(self.rows)):
            if self.rows[0][j] == self.rows[1][j] == self.rows[2][j]: 
                self.win=self.turn.name
                winner_status=True
        if (self.rows[0][0] == self.rows[1][1] == self.rows[2][2]) or (self.rows[0][2] == self.rows[1][1] == self.rows[2][0]):
                self.win=self.turn.name
                winner_status=True
        if winner_status:                
            print(f"The winner is {self.win[-1]}")
            return True
    
    @staticmethod
    def __check_input(sign:str) -> bool :
        if sign.lower() == 'x' or sign.lower() == 'o':
            return True
        else:
            return False 

    def change_turn(self) -> None:
        if self.turn==self.players[0]:
            self.turn=self.players[1]
        else:
            self.turn=self.players[0]

    @staticmethod
    def check_position(index:int) -> True:
        assert isinstance(index,int) and 1<=index<=9,"Enter a valid number"
        return True        

    def move(self, index:int) -> bool :        
        if self.check_position(index):
            if 1<=index and index<=3 and not isinstance(self.rows[0][index-1],str):
                self.rows[0][index-1]=self.turn.sign
            elif 4<=index and index<=6 and not isinstance(self.rows[1][index-4],str):
                self.rows[1][index-4]=self.turn.sign
            elif 7<=index and index<=9 and not isinstance(self.rows[2][index-7],str):
                self.rows[2][index-7]=self.turn.sign
            else:
                return True
    
    def isfull(self) -> bool :
        count=0
        for row in self.rows:
            for obj in row:
                if not isinstance(obj,int):
                    count+=1
        if count==9:
            print("There is no more room to move it's a draw.")
            return True
        return False

    @classmethod
    def new_game(cls) -> object :
        print("Welcome to TikTakToe")
        p1_name=input("Enter player one name:")
        p1_sign=input(f"{p1_name} Choose your sign (o/x):")
        if not cls.__check_input(p1_sign):
            while True:
                p1_sign=input(f"{p1_name} Choose your sign again (o/x):")
                if p1_sign :
                    break
        p2_name=input("Enter player two name:")
        p1=Player(p1_name,p1_sign)
        if p1_sign=='x':
            p2=Player(p2_name,'o')
        else:
            p2=Player(p2_name,'x')
        return TicTacToe([p1,p2])

        