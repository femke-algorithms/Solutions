from queue import PriorityQueue

def main():
    h, w = [int(i) for i in input().split()]

    ocean = []
    seen = []

    for _ in range(h):
        ocean.append([max(-int(i), 0) for i in input().split()])
        seen.append([False for _ in range(w)])

    y, x = [int(i) - 1 for i in input().split()]

    queue = PriorityQueue()

    queue.put_nowait([ocean[y][x], y, x])
    seen[y][x] = True

    moves = [
        (-1, -1), (-1, 0), (-1, 1), 
        (0, -1), (0, 1), 
        (1, -1), (1, 0), (1, 1)
    ]

    s = 0

    while not queue.empty():
        v, y, x = queue.get_nowait()
        if v > 0:
            a = min(v, ocean[y][x])
            s += a
            for _y, _x in moves:
                n_y, n_x = y + _y, x + _x
                if n_x >= 0 and n_x < w and n_y >= 0 and n_y < h and not seen[n_y][n_x]:
                    queue.put_nowait([a, n_y, n_x])
                    seen[n_y][n_x] = True 

    print(s)

    

if __name__ == '__main__':
    main()


'''

3 3
-5 2 -5
-1 -2 -1
5 4 -5
2 2


3 2
-1 -1
0 -1
-2 -2
3 2

3 3
-100 -10 -100
-5 0 -3
-10 -10 -3
3 2

2 3
-2 -3 -4
-3 -2 -3
2 1
'''
'''

#include <vector>
#include <queue>
#include <iostream>

using namespace std;

typedef pair<int, int>ii;
typedef pair<int, ii>iii;

int main()
{
    int height, width;
    cin >> height >> width;
    vector<vector<int>>heightOfPlace(width, vector<int>(height, 0));
    vector<vector<bool>>placable(width, vector<bool>(height, true));
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            int a;
            cin >> a;
            heightOfPlace[j][i] = a;
            if (a >= 0) {
                placable[j][i] = false;
            }
        }
    }/*
     cout << endl << endl << endl;
     for (int i = 0; i < height; i++) {
     for (int j = 0; j < width; j++) {
     cout << heightOfPlace[j][i] << " ";
     }
     cout << endl;
     }

     cout << endl << endl << endl;
     for (int i = 0; i < height; i++) {
     for (int j = 0; j < width; j++) {
     cout << placable[j][i] << " ";
     }
     cout << endl;
     }
     */
    vector<ii>moves = { ii(-1, 0), ii(0, 1), ii(1, 0), ii(0, -1),ii(-1, -1), ii(-1, 1), ii(1, 1), ii(1, -1) };
    int startY, startX;
    cin >> startY >> startX;
    startY--;
    startX--;
    priority_queue<iii>cells;
    cells.push(iii(-heightOfPlace[startX][startY], ii(startX, startY)));
    placable[startX][startY] = false;
    long long int water = 0;
    while (!cells.empty()) {
        int xPos = cells.top().second.first;
        int yPos = cells.top().second.second;
        int fromHeight = cells.top().first;
        cells.pop();
        //cout << xPos << " " << yPos << " " <<fromHeight << endl;
        water += fromHeight;
        for (int m = 0; m < 8; m++) {
            int nextX = xPos + moves[m].first;
            int nextY = yPos + moves[m].second;
            if (nextX >= 0 && nextX < width&&nextY >= 0 && nextY < height) {
                if (placable[nextX][nextY]) {
                    placable[nextX][nextY] = false;
                    cells.push(iii(min(fromHeight, -heightOfPlace[nextX][nextY]), ii(nextX, nextY)));
                }
            }
        }
    }
    cout << water;

    return 0;
}
'''