#include <string>
#include <vector>
#include <iostream>

using namespace std;

char A[20];
int solution(string name) {
    int answer = 0;
    int tmp1 = 0;
    int tmp2 = 0;
    //A-65 = 0
    for(int i = 0; i<name.size(); i++){
        if((int)name[i] > 78){
            tmp1 += 91 - (int)name[i];
        }else{
            tmp1 += (int)name[i]-65;
        }
        
    }
    for(int i = 0; i < name.size(); i++){
        A[i] = 'A';
    }
    int j = 0;
    while(A != name){
        if(name[j+1] == 'A'){
            if(name[j] == 'A'){
                tmp2++;
                j--;
            }else{
                A[j] = name[j];
                tmp2++;
                j--;
            }
            if(j<0){
                j = name.size()-1;
            }
        }else{
            if(name[j] == 'A'){
                tmp2++;
                j++;
            }else{
                A[j] = name[j];
                tmp2++;
                j++;
            }
        }
      
    }
    cout << A << endl;
    answer = tmp1 + tmp2-1;
    return answer;
}

int main(){
    string name = "JEROEN";
    cout << solution(name) << endl;
    return 0;
    
}
