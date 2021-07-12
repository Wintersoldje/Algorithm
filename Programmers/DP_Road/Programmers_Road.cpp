#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    int visited[101][101] = {0,};
    int water[101][101] = {0, }; // 모든 배열 초기화

    for(int i = 0; i < puddles.size(); i++){
        water[puddles[i][1]][puddles[i][0]] = -1; // 물 웅덩이가 있는 부분 -1로 처리
    }
    visited[1][0] = 1;
    
    for(int i = 1; i<= n; i++){
        for(int j = 1; j <= m; j++){ // visited를 슨회하면서 visited[i][j]의 
            if(water[i][j] == -1){
                visited[i][j] = 0;
            }
            else{
                visited[i][j] = (visited[i-1][j] + visited[i][j-1]) % 1000000007;
            }
            
        }
    }

    return visited[n][m];
}