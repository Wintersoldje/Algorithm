#include <iostream>

int a[10];
bool c[10];
using namespace std;

void function(int idx, int start, int n, int m){
    if(idx == m){
        for(int i = 0; i < m; i++){
            cout << a[i];
            if(i != m-1)
                cout << ' ';
        }
        cout << '\n';
        return;
    }
    for(int i = start; i <= n; i++){
        if(!c[i]){
            c[i] = true;
            a[idx] = i;
            function(idx+1, i+1, n, m);
            c[i] = false;
        }
    }
}
int main(){
    int n, m;
    cin >> n >> m ;
    function(0,1,n,m);
}