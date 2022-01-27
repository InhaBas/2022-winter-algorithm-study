#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

static bool validate(vector<string>& data, string& line) {

    char f1, f2; // 프렌즈 두명
    char sign; 
    int requiredDistance, realDistance;
    for (string condition: data) {
        f1 = condition[0];
        f2 = condition[2];
        sign = condition[3];
        requiredDistance = atoi(&condition[4]);
        realDistance = abs(int(line.find(f1) - line.find(f2))) - 1;

        switch(sign) {
            case '=':
                if (realDistance != requiredDistance) return false;
                break;
            case '<':
                if (realDistance >= requiredDistance) return false;
                break;
            case '>':
                if (realDistance <= requiredDistance) return false;
                break;   
        }   
    }
    
    return true;
}

static map<char, bool> visited = {
    {'A', false},
    {'C', false},
    {'F', false},
    {'J', false},
    {'M', false},
    {'N', false},
    {'R', false},
    {'T', false}
};


int solution(int n, vector<string> data) {
    
    int answer = 0;
    string friends = "ACFJMNRT";
    string currentLine = "";
    
    do {
        if (validate(data, friends)) answer += 1;
    } while(next_permutation(friends.begin(), friends.end()));  // 허허 이런게 있네요
    
    
    return answer;
}
