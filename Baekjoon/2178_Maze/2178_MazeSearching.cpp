#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;
int graph[101][101]; // 그래프 설정(visit 표기하기 위해)


int bfs(int x, int y){
    queue<pair<int, int>> q;
    int dx[4] = {-1, 0, 1, 0}; //12시에서 시계방향으로
    int dy[4] = {0, 1, 0, -1};
    q.push({x, y});
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for(int i = 0; i < 4; i++){ //4방향 확인하기 위해
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m){ //공간 벗어나면 무시
                continue;
            }
            if(graph[nx][ny] == 0){
                continue;
            }
            if(graph[nx][ny] == 1){
                graph[nx][ny] = graph[x][y] + 1;
                q.push({nx, ny});
            }
        }    
    }
    return graph[n-1][m-1];
}
int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%1d", &graph[i][j]);
        }
    }
    
    cout << bfs(0, 0) << endl;
}