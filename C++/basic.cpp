#include <iostream>
#include <curses.h>
using namespace std;
int main()
{
    int x;
    cout << "Enter the number" << endl;
    cin >> x;
    int s = x * x;
    cout << "Square of" << x << "is" << s;
    getch();
}
