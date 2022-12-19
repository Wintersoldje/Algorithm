#include <iostream>
#include <vector>

using namespace std;

bool visited[10][31] ={false};
bool line[10][31] = {false};
vector<int> graph[9];
int answer = 4;

bool check(int n, int h){ // 도착 정보 확인
    for(int i = 0; i <= n; i++){
        int start = i;
        for(int j = 0; j <= h; j++){
            if(line[j][start]){
                start += 1;
            }
            else if((start-1 >= 0 && line[j][start-1]) == true){
                start -= 1;
            }
        }
        if(start != i) {
            return false;
        }
    }
    return true;
}
void dfs(int cnt, int x, int y, int n, int h){
    if(check(n, h)){
        answer = min(answer, cnt);
        return;
    }
    else if(cnt == 3 || answer <= cnt){
        return;
    }
    
    for(int i = x; i < h; i++){
        int k = 0;
        if(i == x){
            k = y;
        }
        else{
            k = 0;
        }
        for(int j = k; j <= n-1; j++){
            if(line[i][j] == false && line[i][j+1] == false){
                line[i][j] = true;
                dfs(cnt+1, i, j+2, n, h);
                line[i][j] = false;
            }
        }
    }
}
int main(){
    int n, m, h;
    cin >> n >> m >> h; // input data

    for(int i = 0; i < m; i++){// line insert
        int a, b;
        cin >> a >> b;
        line[a-1][b-1] = true;
    }
    dfs(0, 0, 0, n, h);
    if(answer >= 4) answer = -1;
    cout << answer << endl;


}
