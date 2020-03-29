from copy import deepcopy
from time import time
import random


class AIPlayer:
    def __init__(self, color):
        self.color = color
        self.count = 0
        if self.color == 'X':
            self.against = 'O'
        else:
            self.against = 'X'

    def minimax(self, board, depth, minmax, alpha, beta):
        if time()-self.start_time > 59:
            # 判断是否快超时了
            print("超时了！！！\n超时了！！！\n超时了！！！\n超时了！！！\n超时了！！！\n超时了！！！\n超时了！！！\n超时了！！！\n")
            self.count += 1
            return None
        if depth == self.depth:
            the_max = 0
            action_list = list(board.get_legal_actions(self.color))
            if action_list:
                my_num = list()
                for i in action_list:
                    board_sim = deepcopy(board)
                    board_sim._move(i, self.color)
                    beta = self.minimax(board_sim, depth-1, -1, the_max, 99)
                    if beta == None: break
                    if beta > the_max: the_max = beta
                    my_num.append(beta)
                if my_num:
                    return action_list[my_num.index(max(my_num))]
                else: return random.choice(action_list)
            else: return None

        elif depth == 0:
            return board.count(self.color)

        else:
            if minmax == 1:
                # 如果轮到自己下棋，则需要从之后的所有里面取出最大的更新alpha
                action_list = list(board.get_legal_actions(self.color))
                if action_list:
                    for i in action_list:
                        if beta >= alpha:
                            board_sim = deepcopy(board)
                            board_sim._move(i, self.color)
                            alpha_or_beta = self.minimax(board_sim, depth-1, minmax*-1, alpha, beta)
                            if alpha_or_beta == None: return None
                            if alpha_or_beta > alpha: alpha = alpha_or_beta
                        else: break
                    return alpha
                else: return alpha
            else:
                action_list = list(board.get_legal_actions(self.against))
                if action_list:
                    for i in action_list:
                        if beta >= alpha:
                            board_sim = deepcopy(board)
                            board_sim._move(i, self.against)
                            alpha_or_beta = self.minimax(board_sim, depth-1, minmax*-1, alpha, beta)
                            if alpha_or_beta == None: return None
                            if alpha_or_beta < beta: beta = alpha_or_beta
                        else: break
                    return beta
                else: return beta






    def get_move(self, board):
        """
                根据当前棋盘状态获取最佳落子位置
                :param board: 棋盘
                :return: action 最佳落子位置, e.g. 'A1'
                """
        if self.color == 'X':
            player_name = '黑棋'
        else:
            player_name = '白棋'
        print("请等一会，对方 {}-{} 正在思考中...".format(player_name, self.color))
        print(list(board.get_legal_actions(self.color)))
        self.start_time = time()
        if len(list(board.get_legal_actions(self.color))) < 4:
            self.depth = 7
            action = self.minimax(board, 7, 1, -99, 99)
        elif len(list(board.get_legal_actions(self.color))) > 6:
            self.depth = 5
            action = self.minimax(board, 5, 1, -99, 99)
        else:
            self.depth = 6
            action = self.minimax(board, 6, 1, -99, 99)
        return action
