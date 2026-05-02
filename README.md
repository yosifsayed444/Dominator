
# Algorithm Project: Dominator Problem Analysis

This report provides a detailed analysis of two different approaches used to solve the **Dominator Problem**. An element is considered a "Dominator" if it occurs in more than half of the elements in an array.

---

## 1. Iterative Approach (Boyer-Moore Majority Vote Algorithm)

The iterative solution uses the **Boyer-Moore Majority Vote Algorithm**. It finds a candidate for the majority element in a single pass and then verifies if it is indeed the dominator in a second pass.

### Pseudocode
```text
FUNCTION dominator_iterative(A, N):
    Candidate <- undefined
    Count <- 0
    
    // Phase 1: Find a candidate
    FOR i FROM 0 TO N-1:
        IF Count == 0:
            Candidate <- A[i]
            Count <- 1
        ELSE IF A[i] == Candidate:
            Count <- Count + 1
        ELSE:
            Count <- Count - 1
            
    // Phase 2: Verify candidate
    OCC <- 0
    index <- -1
    FOR i FROM 0 TO N-1:
        IF A[i] == Candidate:
            OCC <- OCC + 1
            index <- i
            
    IF OCC > N / 2:
        RETURN index
    ELSE:
        RETURN -1
```

### Time Complexity Analysis
- **Time Complexity**: **O(n)**
  - The algorithm performs two linear passes over the array. 
  - Each pass takes O(n) time.
- **Space Complexity**: **O(1)**
  - Only a few variables (`candidate`, `count`, `total_count`) are used regardless of the input size.

---

## 2. Recursive Approach (Divide and Conquer)

The recursive solution splits the array into halves, finds candidates in each half, and resolves them to find a global candidate.

### Pseudocode
```text
FUNCTION dominator_recursive(A, left, right):
    // Base Case: Single element
    IF left == right:
        RETURN A[left]

    mid <- (left + right) / 2
    
    // Recursive Calls
    left_dom <- dominator_recursive(A, left, mid)
    right_dom <- dominator_recursive(A, mid + 1, right)

    // Resolution
    IF left_dom == right_dom:
        RETURN left_dom

    // Count occurrences to resolve candidates
    left_count <- 0
    right_count <- 0
    FOR i FROM left TO right:
        IF A[i] == left_dom:
            left_count <- left_count + 1
        IF A[i] == right_dom:
            right_count <- right_count + 1

    IF left_count > right_count:
        RETURN left_dom
    ELSE:
        RETURN right_dom
```

### Time Complexity Analysis
- **Time Complexity**: **O(n log n)**
  - The algorithm uses a master theorem pattern: $T(n) = 2T(n/2) + O(n)$.
  - The $O(n)$ part comes from counting occurrences in the current range to resolve candidates.
  - This results in a total time of $O(n \log n)$.
- **Space Complexity**: **O(log n)**
  - Due to the recursion stack depth.

---

## Summary Table

| Metric | Iterative (Boyer-Moore) | Recursive (Divide & Conquer) |
| :--- | :--- | :--- |
| **Time Complexity** | O(n) | O(n log n) |
| **Space Complexity** | O(1) | O(log n) |
| **Efficiency** | Highly Efficient | Moderate |
| **Implementation** | Simple Loop | Recursive / Divide & Conquer |

---

## 3. Test Case Scenarios

The following test cases demonstrate the algorithm's behavior across various input scenarios.

### # Case 1: Standard case with a dominator
- **Input**: `[3, 4, 3, 2, 3, -1, 3, 3]`
- **Expected Output**: `3` (Value) or index `7`
- **Explanation**: The value `3` appears **5 times** in an array of size **8**. Since `5 > 8/2`, it is the dominator.

### # Case 2: No dominator exists
- **Input**: `[1, 2, 3, 4, 5]`
- **Expected Output**: `-1`
- **Explanation**: Every element appears exactly once. No element appears more than **2.5 times** (N/2), so no dominator exists.

### # Case 3: Empty array
- **Input**: `[]`
- **Expected Output**: `-1`
- **Explanation**: An empty array cannot contain any elements, hence no dominator can exist.

### # Case 4: Single element array
- **Input**: `[42]`
- **Expected Output**: `42` (Value) or index `0`
- **Explanation**: The element `42` appears **1 time** in an array of size **1**. Since `1 > 1/2` (0.5), it is the dominator.

### # Case 5: Dominator on the boundary
- **Input**: `[7, 7, 7, 7, 1, 1, 1]`
- **Expected Output**: `7` (Value) or index `3`
- **Explanation**: The value `7` appears **4 times** in an array of size **7**. Since `4 > 7/2` (3.5), it is the dominator.

### # Case 6: Negative values with a dominator
- **Input**: `[-5, -5, -5, 1, 2]`
- **Expected Output**: `-5` (Value) or index `2`
- **Explanation**: The value `-5` appears **3 times** in an array of size **5**. Since `3 > 5/2` (2.5), it is the dominator.
