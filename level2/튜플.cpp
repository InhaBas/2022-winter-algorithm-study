#include <string>
#include <vector>
#include <cctype>
#include <map>
#include <algorithm>
#define pii pair<int, int>
using namespace std;

vector<int> solution(string s) {
    map<string, int> tupleElement; 
    
    vector<int> answer;
    string num;
    for (auto& ch: s) {      
        if (isdigit(ch)) 
            num += ch;

        else if (ch == ',') {
            tupleElement[num]++;
            num = "";
        }
    }
    tupleElement[num]++;

    vector<pii> tmpAnswer;
    for (auto& [key, value]: tupleElement) tmpAnswer.push_back({value, stoi(key)});
    sort(tmpAnswer.begin(), tmpAnswer.end(), greater<pii>());
    
    for (auto& [value, key]: tmpAnswer) answer.push_back(key);
    return answer;
}
