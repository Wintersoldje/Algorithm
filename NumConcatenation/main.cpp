#include <iostream>

using namespace std;

int main(){
    int num;
    cin >> num;
    long long result = 0;
    for(int start = 1, len = 1; start <= num; start *= 10, len ++){
        int end = start*10-1;
        if(end > num){
            end = num;
        }
        result += (long long)(end - start + 1) * len;
    }
    cout << result << '\n';
    return 0;
}