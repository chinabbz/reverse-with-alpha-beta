from board import Board
from game import Game
from player import HumanPlayer
from player import RandomPlayer
from AIPlayer import AIPlayer

board = Board()
board.display()

# 人类玩家黑棋初始化
black_player = RandomPlayer("X")

# AI 玩家 白棋初始化
white_player = AIPlayer("O")

# 游戏初始化，第一个玩家是黑棋，第二个玩家是白棋
game = Game(black_player, white_player)

# 开始下棋
game.run()

print(white_player.count)
