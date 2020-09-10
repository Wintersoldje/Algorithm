#include <string>
#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;    
    
    int dal[50][50];
    int i;
    int x=-1;
    int y=0;
    int t=1;
    int p=0;
    int q=0;
    int cnt=1;

    int jmax = n;

    while(0<=jmax){
        for(int i=0; i<jmax;i++){
            x=x+t;
            dal[x][y]=cnt;
            cnt++;
        }
        jmax--;
        for(i=0;i<jmax;i++){// 열 표현
            y=y+t;
            dal[x][y]=cnt;
            cnt++;
        }
        jmax--;
        t=t*-1;
        for(i =0; i<jmax; i++){
            if(x-q == y){
                 if(x == 1 && y == 1){
                    
                }else{
                    x = x+t;
                    y = y+t;
                    dal[x][y] = cnt;
                    cnt ++;
                }
            }
        }
        q++;
        jmax--;
        t=t*-1;
    }
    for(int i = 0; i < n; i++){
        for(int j =0; j< i+1; j++){
            answer.push_back(dal[i][j]);
        }
    }
    return answer;
}
int main(){
    vector<int> a = solution(10);
    cout << a[7] << endl;
}
