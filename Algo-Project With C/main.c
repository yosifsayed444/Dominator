#include "dominator.c"

int main()
{
    int A[] = {3, 4, 3, 2, 3, -1, 3, 3};
    int N = sizeof(A) / sizeof(A[0]);

    int result_iterative = dominator_iterative(A, N);
    if (result_iterative != -1)
        printf("Dominator (Iterative): %d\n", A[result_iterative]);
    else
        printf("No dominator found (Iterative).\n");

    int result_recursive = dominator_recursive(A, 0, N - 1);
    if (result_recursive != -1)
        printf("Dominator (Recursive): %d\n", result_recursive);
    else
        printf("No dominator found (Recursive).\n");

    return 0;
}