#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int d[9];
  int sum=0;
  for(int i = 0; i<9; i++){
    cin >> d[i];
    sum += d[i];
  }
  sort(d,d+9);
  for(int i = 0; i<9; i++){
    for(int j = i+1; j<9; j++){
      if(sum - d[i]- d[j] == 100){
        for(int k = 0; k<9; k++){
          if(i == k || j == k){
            continue;
          }
          cout << d[k] << '\n';
        }
        return 0;
      }
    }
  }
}