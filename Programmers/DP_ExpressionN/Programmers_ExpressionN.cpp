#include <string>
#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

int solution(int N, int number) {
    int answer = -1;
    unordered_set<int> s[8];

    int sum = 0;
    for(int i = 0; i < 8; i++){
        sum = 10 * sum + N;
        s[i].insert(sum);
    }

    for(int i = 1; i < 8; i++){
        for(int j = 0; j < i; j++){
            for(int a : s[j]){
                for(int b : s[i-j-1]){
                    s[i].insert(a + b);
                    s[i].insert(a - b);
                    s[i].insert(a * b);
                    if(b != 0) s[i].insert(a/b);
                    cout << "i = " << i << endl;
                    cout << "a+b = " << a + b << endl;
                    cout << "a-b = " << a - b << endl;
                    cout << "a*b = " << a * b << endl;
                
                }
            }
        }
        if(s[i].find(number) != s[i].end()){
            return i + 1;
        }
    }

    return answer;
}

int main(void){
    cout << solution(5, 12);
}

