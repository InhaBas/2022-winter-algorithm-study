#include <string>
#include <vector>
#include <iostream>
#include <map>
#define dict map<string, int>
using namespace std;

static int INDEX_NO = 1;

void zip(string msg, dict& dictionary, vector<int>& answer) {

    for (auto iter = dictionary.rbegin(); iter != dictionary.rend(); iter++) { /* 긴 단어부터 조회 */
        string key = iter->first;
        int value = iter->second;
        
        if(msg.find(key) == 0) {
            answer.push_back(value); // 색인번호 출력
            
            if (msg.length() > key.length()) { // 남은 글자가 있으면
                string index = msg.substr(0, key.length() + 1); // w+c 에 해당하는 색인
                if(dictionary.find(index) == dictionary.end()) // 색인이 없으면 추가 등록
                    dictionary[index] = INDEX_NO++;
                
                zip(msg.substr(key.length()), dictionary, answer);
            }
            break;
        }
    }
}

vector<int> solution(string msg) {
    vector<int> answer;
    
    dict dictionary;
    for(int i = 0; i < 26; i++) 
        dictionary[string(1, 'A'+i)] = INDEX_NO++;
    
    zip(msg, dictionary, answer);
    
    return answer;
}
