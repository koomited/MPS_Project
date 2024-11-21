import matplotlib.pyplot as plt
def tower_hanoi_n_mooves(num, src, helper, dest):
    n_moves = 0
    if num == 1:
        # print(f"Moving disk from {src} to {dest}")
        n_moves+=1
    else:
        n_moves += tower_hanoi_n_mooves(1, src,  helper, dest)
        n_moves += tower_hanoi_n_mooves(num-1, src, dest, helper)
        n_moves += tower_hanoi_n_mooves(num-1, dest, src, helper)
        
        
    return n_moves
            
def print_optimal_moves(num, src, helper, dest):
    if num == 1:
        print(f"Moving disk from {src} to {dest}")
        return 
    print_optimal_moves(num-1, src, dest, helper)
    print(f"Moving disk from {src} to {dest}")
    print_optimal_moves(num-1, helper, src, dest)
    
    
def plt_hanoi(disks, moves):
    _, ax = plt.subplots(figsize = (8, 6))
    ax.plot(disks, moves)
    ax.set_title("number of disks vs number of moves")
    ax.set_xlabel("number of disks")
    ax.set_ylabel("number of moves")
    plt.savefig("hanoiplot.png", transparent=None, dpi=2000, bbox_inches=None)
    plt.show()
    