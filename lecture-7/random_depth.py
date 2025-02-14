import random
import math
import matplotlib.pyplot as plt 
from BstSet import BstSet

def build_random_bst(num_elements):
    #Build and return a BstSet containing num_elements unique random values.
    
    bst = BstSet()
    # Create a large enough range to avoid duplicates easily
    values = list(range(num_elements * 10))
    random.shuffle(values)
    chosen = values[:num_elements]
    for val in chosen:
        bst.add(val)
    return bst

def experiment(h_values, runs=10):
    """
    For each h in h_values:
      - Build BSTs of size (2^h - 1), repeated 'runs' times
      - Compute their max depth
      - Return two lists: sizes (x-values) and avg_depths (averages)
    """
    sizes = []
    avg_depths = []

    for h in h_values:
        n = (2 ** h) - 1
        sizes.append(n)

        total_depth = 0
        for _ in range(runs):
            bst = build_random_bst(n)
            total_depth += bst.max_depth()

        avg_depth = total_depth / runs
        avg_depths.append(avg_depth)

    return sizes, avg_depths

def main():
    # We will consider h = 5..20
    h_values = range(5, 21)
    runs = 10  # Number of random BSTs to build for each h

    sizes, avg_depths = experiment(h_values, runs)

    # The ideal (complete) tree depth is just h
    ideal_depths = list(h_values)

    # Print results on screen
    print("h | n=(2^h-1) | average max depth | ideal depth (h)")
    print("-----------------------------------------------")
    for h, n, a, i in zip(h_values, sizes, avg_depths, ideal_depths):
        print(f"{h:2d} | {n:8d}  | {a:18.2f} | {i}")

    # Plot Tree sizes vs Average Max Depth
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, avg_depths, 'o', label="Random BST (avg depth)")
    plt.plot(sizes, ideal_depths, 's', label="Complete Tree depth = h")
    plt.xlabel("Tree Size (n = 2^h - 1)")
    plt.ylabel("Depth")
    plt.title("Random BST Depth vs. Complete Tree Depth")
    plt.legend()
    plt.tight_layout()
    plt.savefig("random_depth_plot_size_vs_depth.png")  
    plt.show()

    # Plot log2(Tree sizes) vs Average Max Depth
    log_sizes = [math.log2(s) for s in sizes]

    plt.figure(figsize=(10, 6))
    plt.plot(log_sizes, avg_depths, 'o', label="Random BST (avg depth)")
    plt.plot(log_sizes, ideal_depths, 's', label="Complete Tree depth = h")
    plt.xlabel("log2(Tree Size)")
    plt.ylabel("Depth")
    plt.title("Random BST Depth vs. Complete Tree Depth (log2(n) on x-axis)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("random_depth_plot_logsize_vs_depth.png")  
    plt.show()

if __name__ == "__main__":
    main()
