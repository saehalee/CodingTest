def solution(lottos, win_nums):
    answer = []
    rank_min = 7
    for i in win_nums:
        if i in lottos: 
            rank_min -= 1 #5,4,3,2
    rank_max = rank_min-lottos.count(0)
    
    if rank_min == 7:
        rank_min = 6
    if rank_max == 7:
        rank_max = 6
        
    answer.append(rank_max)
    answer.append(rank_min)
    return answer