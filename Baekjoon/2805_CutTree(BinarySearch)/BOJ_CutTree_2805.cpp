#include <iostream>
#include <vector>

using namespace std;


int main(void){
    long long n, m;
    long long maxTree;
    cin >> n >> m;
    vector<long long> tree;
    for(int i = 0; i < n; i++){
        long long tmp;
        cin >> tmp;
        tree.push_back(tmp);
        maxTree = max(tmp, maxTree);
    }
    long long min, max, mid;
    min = 0;
    long long s = tree.size();
    max = maxTree;
    
    long long answer = 0;
    while(max >= min){
        long long count = 0;
        for(int i = 0; i < s; i++){
            mid = (min + max) / 2;
            if(mid <= tree[i]){
                count += tree[i] - mid;
            }
        }
        if(count < m){
            max = mid -1;
        }
        else{
            answer = mid;
            min = mid + 1;
        }
    }
    cout << answer << endl;
}