#include <stdio.h>

int dominator_iterative(int A[], int N)
{
    int candidate = 0;
    int count = 0;

    for (int i = 0; i < N; i++)
    {
        if (count == 0)
        {
            candidate = A[i];
            count = 1;
        }
        else if (A[i] == candidate)
        {
            count++;
        }
        else
        {
            count--;
        }
    }

    count = 0;
    int index = -1;

    for (int i = 0; i < N; i++)
    {
        if (A[i] == candidate)
        {
            count++;
            index = i;
        }
    }

    if (count > N / 2)
        return index;

    return -1;
}

int dominator_recursive(int A[], int left, int right)
{
    if (left == right)
        return A[left];

    int mid = (left + right) / 2;

    int left_dom = dominator_recursive(A, left, mid);
    int right_dom = dominator_recursive(A, mid + 1, right);

    if (left_dom == right_dom)
        return left_dom;

    int left_count = 0;
    int right_count = 0;

    for (int i = left; i <= right; i++)
    {
        if (A[i] == left_dom)
            left_count++;

        if (A[i] == right_dom)
            right_count++;
    }

    if (left_count > right_count)
        return left_dom;

    return right_dom;
}