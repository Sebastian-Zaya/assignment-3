from QuadHash import QuadHash


def main():
    # Initialize the hash table
    h = QuadHash()

    # Add multiple entries
    entries = {
        "cat": 1,
        "dog": 2,
        "mouse": 3,
        "elephant": 4,
        "tiger": 5,
        "lion": 6,
        "bear": 7,
        "giraffe": 8,
        "zebra": 9,
        "monkey": 10
    }

    print("Adding entries:")
    for key, value in entries.items():
        print(f"  Adding ({key}, {value})")
        h.add(key, value)

    print("\nHash Table Contents:")
    print(h)

    # Check containment
    print("\nContainment Checks:")
    test_keys = ["cat", "dog", "wolf", "lion", "tiger"]
    for key in test_keys:
        print(f"  Contains '{key}'? {h.contains_key(key)}")

    # Retrieve values
    print("\nRetrieving Values:")
    for key in test_keys:
        value = h.get(key)
        if value is not None:
            print(f"  {key} -> {value}")
        else:
            print(f"  {key} not found.")

    # Remove some entries
    print("\nRemoving Entries:")
    remove_keys = ["cat", "lion", "giraffe"]
    for key in remove_keys:
        removed = h.remove(key)
        print(f"  Removing '{key}': {'Success' if removed else 'Failed'}")

    print("\nHash Table Contents After Removals:")
    print(h)

    # Check containment after removal
    print("\nContainment Checks After Removal:")
    for key in test_keys:
        print(f"  Contains '{key}'? {h.contains_key(key)}")

    # Attempt to add a new entry that might use a previously deleted slot
    print("\nAdding a new entry 'wolf' -> 11")
    h.add("wolf", 11)
    print("\nHash Table Contents After Adding 'wolf':")
    print(h)

    # Final containment check
    print("\nFinal Containment Checks:")
    final_keys = ["wolf", "cat", "dog", "lion"]
    for key in final_keys:
        print(f"  Contains '{key}'? {h.contains_key(key)}")


if __name__ == "__main__":
    main()
