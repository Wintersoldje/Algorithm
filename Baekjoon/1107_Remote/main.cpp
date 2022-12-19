#include <iostream>

using namespace std;
bool broken[10];

int count(int c){
    if(c == 0){
        if(broken[0]){
            return 0;
        }
        else{
            return 1;
        }
    }
    int len = 0;
    while(c>0){
        if(broken[c % 10]){ //한자리씩 확인
            return 0;
        }
        len++;
        c = c / 10;
    }
    return len;
}
int main(){
    int num;
    cin >> num;
    int broke;
    cin >> broke;
    for(int i = 0; i<broke; i++){ //고장난 버튼 확인
        int x;
        cin >> x;
        broken[x] = true;
    }
    int result = num - 100;
    if(result < 0){
        result = -result;
    }
    for(int i = 0; i <= 1000000; i++){
        int c = i;
        int len = count(c); 
        if(len > 0){
            int press = c - num;
            if(press < 0){
                press = -press;
            }
            if(result > len + press){
                result = len + press;
            }
        }
    }
    cout << result << '\n';
    return 0;
}