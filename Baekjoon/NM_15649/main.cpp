#include <iostream>

using namespace std;
int n, m;
int arr[10];
bool c[10];

void function(int tmp){
    if(tmp == m){
        for(int i = 0; i < m; i++){
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return;
    }
    for(int i = 1; i <= n; i++){
        if(!c[i]){
            c[i] = true;
            arr[tmp] = i;
            function(tmp+1);
            c[i] = false;
        }
    }
}

int main(){
    cin >> n >> m ;
    function(0);
    return 0;
}