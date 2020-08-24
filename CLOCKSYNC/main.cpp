#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

int button[10][5]{
  {0,1,2,-1,-1},
  {3,7,9,11,-1},
  {4,10,14,15},
  {0,4,5,6,7},
  {6,7,8,10,12},
  {0,2,14,15,-1},
  {3,14,15,-1,-1},
  {4,5,7,14,15},
  {1,2,3,4,5},
  {3,4,5,9,13}
};
bool check(vector<int> &clock){
  for(int i = 0; i<16; i++){
    if(clock[i] != 12){
      return false;
    }
  }
  return true;
}
void pressButton(vector<int> &clock, int next){
  for(int i = 0; i<5; i++){
    if(button[next][i] == -1){
      break;
    }
    clock[button[next][i]] += 3;
    if(clock[button[next][i]] == 15){
      clock[button[next][i]] = 3;
    }
  }
}
int click(vector<int> &clock, int s){
  if(s == 10)
    return check(clock) ? 0: 987654321;
  int ret = 987654321;
  for(int cnt = 0; cnt < 4; cnt++){
    ret = min(ret, cnt + click(clock, s+1));
    pressButton(clock, s);
  }
  return ret;
}

int main(){
  int num;
  cin >> num;
  while(num--){
    vector<int> clock(16);
    for(int i = 0; i<16; i++){
      cin >> clock[i];
    }
    int ans = click(clock, 0);
    if(ans == 987654321){
      cout << -1 << '\n';
    }
    else{
      cout << ans << '\n';
    }
  }
  return 0;
}