#!/usr/bin/env python3
# -*- coding: utf-8 -*


import random
import sys
import time

from othello_shared import find_lines, get_possible_moves, get_score, play_move

moves = dict() 

def compute_utility(board, color): 
     disk_count = get_score(board) 
     dark_disk = disk_count[0] 
     light_disk = disk_count[1] 
     if color == 1: 
         return dark_disk - light_disk 
     elif color == 2: 
         return  light_disk - dark_disk 



############ MINIMAX ############################### 

def minimax_min_node(board, color): 
    if board in moves: 
        return moves[board] 
    else: 
        min_next_nodes = get_possible_moves(board, 3-color) 
        mList1 = [] 
        if(len(min_next_nodes) == 0): 
            return compute_utility(board, color) 

        for items in min_next_nodes: 
            sBoard1 = play_move(board, 3-color, items[0], items[1]) 
            tList1 = minimax_max_node(sBoard1, color) 
            mList1.append(tList1) 

        moves.update({board : min(mList1)}) 
        return  min(mList1) 


def minimax_max_node(board, color): 
    if board in moves: 
        return moves[board] 
    else: 
        mNodes1 = get_possible_moves(board, color) 
        mList1 = [] 
        if(len(mNodes1) == 0): 
            return compute_utility(board, color) 

        for items in mNodes1: 
            sBoard1 = play_move(board, color, items[0], items[1]) 
            tList1 = minimax_min_node(sBoard1, color) 
            mList1.append(tList1) 

        moves.update({board : min(mList1)}) 
        return max(mList1) 


def select_move_minimax(board, color): 

    possible_moves = get_possible_moves(board, color) 
    mList1 = [] 
    for items in possible_moves: 
        sBoard1 = play_move(board, color, items[0], items[1]) 
        utility =  minimax_min_node(sBoard1, color) 
        mList1.append(utility) 

    max_index = mList1.index(max(mList1)) 
    return possible_moves[max_index][0], possible_moves[max_index][1] 

############ ALPHA-BETA PRUNING #####################

def alphabeta_min_node(board, color, alpha, beta, level, limit): 
    if board in moves: 
        return moves[board]
    else: 
        min_next_nodes = get_possible_moves(board, 3-color) 
        mList1 = [] 
        if(len(min_next_nodes) == 0 or limit <= level): 
            return compute_utility(board, color)

        v = float("inf") 
        mDict1 = dict() 
        for items in min_next_nodes: 
            sBoard1 = play_move(board, 3-color, items[0], items[1]) 
            mDict1.update({sBoard1: compute_utility(sBoard1,color)}) 

        for key in sorted(mDict1, key=mDict1.get): 
            v = min(v, alphabeta_max_node(sBoard1, color, alpha, beta, level+1, limit)) 
            if v <= alpha: 
                return v; 
            beta = min(beta,v) 

        moves.update({board : v})
        return v 


def alphabeta_max_node(board, color, alpha, beta, level, limit): 
    if board in moves: 
        return moves[board]
    else: 
        mNodes1 = get_possible_moves(board, color) 

        mList1 = [] 
        if(len(mNodes1) == 0 or limit <= level): 
            return compute_utility(board, color) 
        v = float("-inf") 
        mDict1 = dict() 
        for items in mNodes1: 
            sBoard1 = play_move(board, color, items[0], items[1]) 
            mDict1.update({sBoard1:compute_utility(sBoard1,color)}) 

        for key in sorted(mDict1, key=mDict1.get): 
            v = max(v, alphabeta_min_node(key, color, alpha, beta, level+1, limit)) 
            if v >= beta: 
                return v; 
            alpha = max(alpha,v) 

        moves.update({board : v})
        return v 


def select_move_alphabeta(board, color): 
    possible_moves = get_possible_moves(board, color) 
    mList1 = [] 
    for items in possible_moves: 
        sBoard1 = play_move(board, color, items[0], items[1]) 
        utility =  alphabeta_min_node(sBoard1, color, float("-inf"), float("inf"), 0, 7) 
        mList1.append(utility) 

    max_index = mList1.index(max(mList1)) 
    return possible_moves[max_index][0], possible_moves[max_index][1] 


#################################################### 
def run_ai(): 

    print("Minimax AI") 
    color = int(input()) 

    while True: 
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split() 
        dark_score = int(dark_score_s) 
        light_score = int(light_score_s) 

        if status == "FINAL":
            print 
        else: 
            board = eval(input())
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__": 
    run_ai() 