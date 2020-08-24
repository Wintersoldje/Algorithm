#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

vector<int> heatTime;
vector<int> eatTime;
int num;

int heat(vector<int>& heat, vector<int>& eat){
    vector<pair<int,int>> order;
    for(int i = 0; i < num; i++){
        order.push_back(make_pair(eatTime[i], heatTime[i]));
    }
    sort(order.begin(), order.end(), greater<>());
    int allTime = 0;
    int beginEat = 0;
    for(int i = 0; i< num; i++){
        int heatbox = order[i].second;
        beginEat += heatbox;
        allTime = max(allTime, beginEat + order[i].first);
    }
    return allTime;
}
int main(){
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; i++){
        cin >> num;
        for(int j = 0; j< num; j++){
            int tmp;
            cin >> tmp;
            heatTime.push_back(tmp);
        }
        for(int j = 0; j < num; j++){
            int tmp;
            cin >> tmp;
            eatTime.push_back(tmp);
        }
        cout << heat(heatTime, eatTime) << '\n';
    }
}
