# TODO:
1. block输入到河流的量是多少？应该不是全部吧

河流考虑

Q_block 
if 主干:
    if (seg=1 or t=0):
        Q_neighbor(seg, t) = Q_base
    else:
        Q_neighbor(seg, t) = Q_prev(seg-1,t-1)
    
    if branch:
        if t = 0:
            Q_branch = Q_branch_base
        else:
            b = find_branch(Q)
            Q_branch = Q_branch_b(b,t-1)
    else:
        Q_branch = 0
else:
    if (seg=1 or t=0):
        Q_neighbor(seg, t) = Q_base
    else:
        Q_neighbor(seg, t) = Q_prev(seg-1,t-1)
    
    Q_branch = 0