#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long min = 0;
    sort(times.begin(), times.end());
    long long max = (long long)(times[times.size()-1]) * n ;
    long long mid = 0;
    long long answer = max;
    while(min <= max){
        mid = (min + max) /2;
        long long sum = 0;
        for(int i = 0; i < times.size(); i++){
            sum += mid/times[i];
        }
        if(n > sum)
            min = mid +1;
        else{
            if(mid <= answer){
                answer = mid;
            }
            max = mid - 1;
        }
    }
    return answer;
}
