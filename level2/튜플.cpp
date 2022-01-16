#include <string>
#include <vector>
#include <queue>
#include <cctype>
#include <set>
#define MySubset priority_queue<string, vector<string>, decltype(compare)>
using namespace std;

auto compare = [](string a, string b) {return a.length() > b.length();};

void splitIntoSubsets(string& s, MySubset& subsetList) {
    string subset;
    int pos;
    while ((pos = s.find("},{")) != string::npos) {
        subset = s.substr(0, pos);
        subsetList.push(subset);
        s.erase(0, pos + 3);
    }
    subsetList.push(s);
}

bool isNewElement(set<int>& tuple, int e) {
    return tuple.find(e) == tuple.end();
}

vector<int> solution(string s) {
    set<int> elementsInTuple;
    s = s.substr(2, s.length() - 4);
    MySubset subsetList(compare);

    splitIntoSubsets(s, subsetList);
    
    vector<int> answer;
    while (!subsetList.empty()){
        bool find = false;
        string num; 
        string subset = subsetList.top();
        subsetList.pop();
    
        for (auto& ch: subset) {    
            
            if (isdigit(ch)) 
                num += ch;
            else if (ch == ',') {
                if (isNewElement(elementsInTuple, stoi(num))) { /* 새로운 요소이면 추가! */
                    elementsInTuple.insert(stoi(num));
                    answer.push_back(stoi(num));
                    find = true;
                    break;
                }
                num = "";
            }
        }

        if (!find) { /* 부분집합의 마지막 요소는 for문 안에서 검사를 못하기 때문에 여기서 검사 */
            elementsInTuple.insert(stoi(num));
            answer.push_back(stoi(num));
        }
    }

    return answer;
}
