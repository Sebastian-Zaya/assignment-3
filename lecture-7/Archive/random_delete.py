import random
from BstSet import BstSet

def main():
    n = 1023
    pool = list(range(n * 10))  
    random.shuffle(pool)
    chosen = pool[:n]  

    bst = BstSet()
    for val in chosen:
        bst.add(val)

    # Save DOT text in "before_delete.txt"
    before_dot = bst.to_dot_string()
    with open("/Users/sebastianzayaalexandros/Documents/programming/assignments/data structures/assignment-3/lecture-7/before_delete.txt", "w") as f:
        f.write(before_dot)
    print("DOT representation before deletions saved to 'before_delete.txt'.")

    # Repeat 2000 times
    times = 2000
    k = 512 
    for iteration in range(1, times + 1):
        deleted_values = random.sample(chosen, k)
        for val in deleted_values:
            bst.remove(val)

        for val in deleted_values:
            bst.add(val)

        # Optional: Print progress every 500 iterations
        if iteration % 500 == 0:
            print(f"  Completed {iteration} out of {times} iterations.")

    # Save DOT text in "after_delete.txt"
    after_dot = bst.to_dot_string()
    with open("/Users/sebastianzayaalexandros/Documents/programming/assignments/data structures/assignment-3/lecture-7/after_delete.txt", "w") as f:
        f.write(after_dot)
    print("DOT representation after deletions saved to 'after_delete.txt'.")

if __name__ == "__main__":
    main()
