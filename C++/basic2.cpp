#include <iostream>
using namespace std;
int sum(int *, int *);
int main()
{
 int a = 5, b = 6;
 int s = sum(&a, &b);
 cout << "Sum of two Number" << s;
}

int sum(int *p, int *q)
{
 return (*p + *q);
}
