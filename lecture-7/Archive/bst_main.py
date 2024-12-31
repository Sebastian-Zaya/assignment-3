import random
from BstSet import BstSet

def main():
    # Example usage of BstSet
    bst = BstSet()

    # Insert 10 random values
    print("Inserting 10 random values into BST:")
    for _ in range(10):
        val = random.randint(1, 100)
        print(f"  Adding {val}")
        bst.add(val)

    print("\nBST contents (in-order):")
    print(bst)  # uses __str__

    # Search for a few random values
    print("\nSearching for values 1..5 in BST:")
    for val in range(1, 6):
        print(f"  {val}: {'Found' if bst.search(val) else 'Not found'}")

    # Remove some values
    print("\nRemoving values 2..4 if they exist:")
    for val in range(2, 5):
        if bst.search(val):
            print(f"  Removing {val}")
            bst.remove(val)
        else:
            print(f"  {val} not found; cannot remove")

    print("\nBST after removals:")
    print(bst)

    # Print max depth
    print(f"\nMax depth: {bst.max_depth()}")

    # Save DOT representation
    dot_str = bst.to_dot_string()
    with open("bst_main_output.dot", "w") as f:
        f.write(dot_str)
    print("\nDOT representation saved to 'bst_main_output.dot'.")

if __name__ == "__main__":
    main()
