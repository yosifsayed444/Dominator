# =============================================================
#  SOLUTION 1 — NON-RECURSIVE (Boyer-Moore Majority Vote)
# =============================================================
def dominator_iterative(A):

    n = len(A)

    if n == 0:
        return -1

    candidate = None
    count = 0

    for val in A:
        if count == 0:
            candidate = val
            count = 1
        elif val == candidate:
            count += 1
        else:
            count -= 1

    count = 0
    index = -1

    for i, val in enumerate(A):
        if val == candidate:
            count += 1
            index = i

    if count > n // 2:
        return index

    return -1


# =============================================================
#  SOLUTION 2 — RECURSIVE  (Divide & Conquer)
# =============================================================

def dominator_recursive(A):

    n = len(A)

    if n == 0:
        return -1

    def _solve(lo, hi):

        if lo == hi:
            return A[lo], 1, lo

        mid = (lo + hi) // 2
        lval, lcount, lidx = _solve(lo, mid)       # left half
        rval, rcount, ridx = _solve(mid + 1, hi)   # right half

        if lval == rval:
            return lval, lcount + rcount, lidx
        elif lcount >= rcount:
            return lval, lcount - rcount, lidx
        else:
            return rval, rcount - lcount, ridx

    candidate, _, _ = _solve(0, n - 1)


    count = 0
    index = -1

    for i, val in enumerate(A):
        if val == candidate:
            count += 1
            index = i

    if count > n // 2:
        return index

    return -1


