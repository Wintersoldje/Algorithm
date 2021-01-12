//
//  main.cpp
//  Sort
//
//  Created by 정제윈 on 2020/09/05.
//  Copyright © 2020 정제윈. All rights reserved.
//
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int tmp = 0;
    vector<int> B;
    sort(citations.begin(), citations.end());
    for(int i = 0; i<citations.size(); i++){
        tmp = citations.size()-i;
        int tmp2 = min(tmp, citations[i]);
        B.push_back(tmp2);
    }
    sort(B.begin(), B.end(), greater<int>());
    answer = B[0];
    return answer;
}

int main(int argc, const char * argv[]) {
    vector<int> A;
    int num;
    cin >> num;
    
    for(int i = 0; i < num; i++){
        int tmp;
        cin >> tmp;
        A.push_back(tmp);
    }
    cout << solution(A) << endl;
    return 0;
}
