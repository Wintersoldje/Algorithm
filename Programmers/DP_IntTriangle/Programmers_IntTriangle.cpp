#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle) {
    for(int i = 1; i < triangle.size(); i++){
        for(int j = 0; j < triangle[i].size(); j++){
            if(triangle[i-1].size() <= 1){
                triangle[i][j] += triangle[i-1][0];
            }
            else{
                if(j==0){
                    triangle[i][j] += triangle[i-1][j];
                }
                else if(j == i){
                    triangle[i][j] += triangle[i-1][j-1];
                }
                else{
                    if(triangle[i-1][j-1] > triangle[i-1][j]){
                        triangle[i][j] += triangle[i-1][j-1];
                    }
                    else{
                        triangle[i][j] += triangle[i-1][j];
                    }
                }
                
            }
        }
    }

    sort(triangle[triangle.size()-1].begin(), triangle[triangle.size()-1].end(),greater<int>());
    int answer = triangle[triangle.size()-1][0];

    return answer;
}
