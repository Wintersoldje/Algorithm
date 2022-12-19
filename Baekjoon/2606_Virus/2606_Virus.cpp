#include <iostream>
#include <vector>

using namespace std;

vector<int> map[101];
bool check[101];
int cnt = 0;

void dfs(int x){
    check[x] = true;
    for(int i = 0; i < map[x].size(); i++){
        int y = map[x][i];
        if(!check[y]){
            dfs(y);
            cnt ++;
        }
    }
}

int main(){
    int n, m;
    cin >> n >> m;
    for(int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        map[a].push_back(b);
        map[b].push_back(a);
    }
    dfs(1);
    cout << cnt << endl;
}