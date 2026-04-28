
from dominator_solutions import dominator_iterative, dominator_recursive


# =============================================================
#  TEST CASES
# =============================================================

def run_tests():
    """Run all test cases and print results."""

    test_cases = [
        ([3, 4, 3, 2, 3, -1, 3, 3],     "Standard case — dominator=3"),
        ([],                              "Empty array"),
        ([1],                             "Single element"),
        ([5, 5, 5, 1, 2],                "Dominator in first half"),
        ([1, 2, 3, 4, 5],                "No dominator"),
        ([7, 7, 7, 7, 1, 1, 1],          "Exactly > half (4 out of 7)"),
        ([2, 2, 1, 1, 2],                "Dominator with count = N/2+1"),
        ([-5, -5, -5, 1, 2],             "Negative dominator"),
        ([100000] * 50001 + [0] * 49999, "Large N=100,000"),
    ]

    print("=" * 65)
    print(f"{'TEST CASES':^65}")
    print("=" * 65)
    print(f"{'#':<4} {'Description':<35} {'Iterative':>10} {'Recursive':>10}")
    print("-" * 65)

    all_passed = True

    for i, (arr, desc) in enumerate(test_cases, 1):
        res_iter = dominator_iterative(arr)
        res_recu = dominator_recursive(arr)

        agreed = (res_iter == -1 and res_recu == -1) or \
                 (res_iter != -1 and res_recu != -1 and arr[res_iter] == arr[res_recu])

        status = "✓" if agreed else "✗"
        if not agreed:
            all_passed = False

        print(f"{i:<4} {desc:<35} {str(res_iter):>10} {str(res_recu):>10}  {status}")

    print("-" * 65)
    print(f"{'All tests agreed: ✓' if all_passed else 'Mismatch detected: ✗':>65}")
    print("=" * 65)


# =============================================================
#  USER INPUT
# =============================================================

def run_user_input():
    """Ask the user to enter an array and show the result."""

    print("\n" + "=" * 65)
    print(f"{'YOUR INPUT':^65}")
    print("=" * 65)

    while True:
        try:
            raw = input("\nEnter array elements separated by spaces: ")
            A = list(map(int, raw.split()))
            break
        except ValueError:
            print("  ✗ Invalid input. Please enter integers only.")
            print("    Example: 3 4 3 2 3 -1 3 3")

    n = len(A)
    print(f"\nArray : {A}")
    print(f"N     : {n}")
    if n > 0:
        print(f"N//2  : {n // 2}  (dominator must appear > {n // 2} times)")

    idx_iter = dominator_iterative(A)
    idx_recu = dominator_recursive(A)

    print("\n" + "-" * 65)
    if idx_iter != -1:
        dom_val = A[idx_iter]
        occurrences = A.count(dom_val)
        print(f"  Dominator value  : {dom_val}")
        print(f"  Occurrences      : {occurrences} out of {n}")
        print(f"  Iterative index  : {idx_iter}")
        print(f"  Recursive index  : {idx_recu}")
    else:
        print("  No dominator found. (returned -1)")
    print("-" * 65)


# =============================================================
#  ENTRY POINT
# =============================================================

if __name__ == "__main__":
    run_tests()
    run_user_input()
