#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int map[1001][1001];
int n, m;
queue<pair<int, int>> q;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};


int check(){
    int answer = 0;
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(map[i][j] == 0)
                return -1;
            if(answer < map[i][j])
                answer = map[i][j];
        }

    }
    return answer-1;
}
void bfs(){
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx < 0 || nx >= m || ny < 0 || ny >= n){
                continue;
            }
            if(map[nx][ny] == -1 || map[nx][ny] == 1){
                continue;
            }
            if(map[nx][ny] == 0){
                map[nx][ny] = map[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    
}

int main(){
    int tmp;
    cin >> n >> m ;
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            cin >> tmp;
            map[i][j] = tmp;
            if(tmp == 1){
                q.push({i, j});
            }
        }
    }
    bfs();
    cout << check() << endl;

}