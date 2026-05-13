#include <stdio.h>

int dominator_iterative(int A[], int n)
{
    int candidate = 0;
    int count = 0;

    for (int i = 0; i < n; i++)
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

    for (int i = 0; i < n; i++)
    {
        if (A[i] == candidate)
        {
            count++;
            index = i;
        }
    }

    if (count > n / 2)
        return index;

    return -1;
}

int dominator_recursive(int A[], int left, int right)
{
    if (left == right)
        return left;

    int mid = (left + right) / 2;

    int left_index = dominator_recursive(A, left, mid);
    int right_index = dominator_recursive(A, mid + 1, right);

    int left_value = A[left_index];
    int right_value = A[right_index];

    if (left_value == right_value)
        return left_index;

    int left_count = 0;
    int right_count = 0;

    for (int i = left; i <= right; i++)
    {
        if (A[i] == left_value)
            left_count++;

        if (A[i] == right_value)
            right_count++;
    }

    int size = right - left + 1;

    if (left_count > size / 2)
        return left_index;

    if (right_count > size / 2)
        return right_index;
    
    return -1;
}