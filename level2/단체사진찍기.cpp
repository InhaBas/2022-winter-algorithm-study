#include <string>
#include <vector>
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

static void jul_Seo(string& currentLine, string& friends, map<char, bool>& visited, vector<string>& data, int& answer) {
    
    // 모든 카카오프렌즈가 줄을 다 섰을 경우 (terminal case)
    if (currentLine.length() == 8) { 
        if (validate(data, currentLine)) {
            answer += 1;
        }
        return;
    }
    
    for (auto& ch: friends) {
        if (!visited[ch]) {
            visited[ch] = true;
            currentLine += ch;
            
            jul_Seo(currentLine, friends, visited, data, answer);
            
            currentLine.pop_back();
            visited[ch] = false;
        }
    }
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
    
    jul_Seo(currentLine, friends, visited, data, answer);
    
    return answer;
}

