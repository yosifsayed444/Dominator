#include "dominator.c"

int main()
{
    printf("Enter the size of the array: ");
    int n;
    scanf("%d", &n);
    int A[n];

    printf("Enter the elements of the array: \n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &A[i]);
    }

    int result_iterative = dominator_iterative(A, n);
    if (result_iterative != -1)
        printf("Dominator (Iterative) %d found at index: %d\n", A[result_iterative], result_iterative);
    else
        printf("No dominator found (Iterative).\n");

    int result_recursive = dominator_recursive(A, 0, n - 1);
    if (result_recursive != -1)
        printf("Dominator (Recursive) %d found at index: %d\n", A[result_recursive], result_recursive);
    else
        printf("No dominator found (Recursive).\n");

    return 0;
}