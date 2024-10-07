class Pong:
    
    lexicon = {
        1: {
            0: "Player 1 has hit the ball",
            1: "Player 2 has hit the ball",
        },
        2: {
            0: "Player 1 has missed the ball",
            1: "Player 2 has missed the ball",
        },
        3: {
            0: "Player 1 has won the game",
            1: "Player 2 has won the game",
        },
        0: "Game Over!"
    }
    
    INDEX = 0
    
    def __init__(self, max_score):
        self.max_score = max_score
        self.player = [0, 0]
        self.win = False

    def play(self, ball_pos, player_pos):
        action = self.__give_type(ball_pos, player_pos)
        
        if action == 1 or action == 2:
            result = self.lexicon[action][self.INDEX % 2]
        elif action == 3:
            result = self.lexicon[action][(self.INDEX + 1) % 2]
        else:
            result = self.lexicon[action]
        
        self.INDEX += 1
        print(result)
        
    def __give_type(self, ball, player):
        if self.win:
            return 0
        
        if player - 3.5 <= ball <= player + 3.5:
            return 1
        else:
            self.player[(self.INDEX + 1) % 2] += 1
            
            if self.player[(self.INDEX + 1) % 2] == self.max_score:
                self.win = True
                return 3
            
            return 2
        

game = Pong(2); 
game.play(50, 53)  
game.play(100, 97) 
game.play(0, 4)    
game.play(25, 25)  
game.play(75, 25) 
game.play(50, 50)      