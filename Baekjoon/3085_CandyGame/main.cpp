#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
int cases;

int cheak(vector<string>& a){// 같으면 카운트
    int result = 1;
    for(int i = 0; i < cases; i++){
        int cnt = 1;
        for(int j = 1 ; j < cases; j++){
            if(a[i][j] == a[i][j-1]){
                cnt += 1;
            }
            else{
                cnt = 1;
            }
            if(result < cnt) result = cnt;
        }
        cnt = 1;
        for(int j = 1; j < cases; j++){
            if(a[j][i] == a[j-1][i]){
                cnt += 1;
            }
            else{
                cnt = 1;
            }
            if(result < cnt) result = cnt;
        }
    }
    return result;
}

int main(){
    cin >> cases;
    vector<string> table(cases);
    for(int i = 0; i<cases; i++){
        cin >> table[i];
    }

    int answer = 0;

    for(int i = 0; i<cases; i++){
        for(int j = 0; j < cases; j++){
            if(j+1 < cases){
                swap(table[i][j], table[i][j+1]); // 인접한 두칸 교환
                int tmp = cheak(table);
                if(answer < tmp){
                    answer = tmp;
                }
                swap(table[i][j+1],table[i][j]); // 원래대로 되돌리기
            }
            if(i+1 < cases){
                swap(table[i][j], table[i+1][j]);// 인접한 두칸 교환
                int tmp = cheak(table);
                if(answer < tmp){
                    answer = tmp;
                }
                swap(table[i+1][j],table[i][j]); // 원래대로 되돌리기
            }
        }
    }
    cout << answer << '\n';
    return 0;
}