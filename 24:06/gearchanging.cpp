#include <iostream>
#include <queue>

using namespace std;

int main() 
{
    int n, m, o; 
    cin >> n >> m >> o;

    double front[n];
    priority_queue<double> result;

    for(int i = 0; i < n; i++) 
    {
        cin >> front[i];  
    }

    for (int i = 0; i < m; i++)
    {
        double x;
        cin >> x;
        for (int j = 0; j < n; j++)
        {
            result.push(-x / front[j]);
        }
    }

    double d = result.top();
    result.pop();

    while(!result.empty()) 
    {
        if(d * (100.0 + o) / 100 > result.top()) 
        {
            cout << "Time to change gears!" << endl;
            return 0;
        }
        d = result.top();
        result.pop();
    }

    cout << "Ride on!" << endl;

    return 0;
}