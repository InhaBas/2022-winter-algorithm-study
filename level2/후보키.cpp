#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <iostream>
#include <cstring>
#define vi vector<int>
#define vii vector<vector<int>>
using namespace std;


bool checkMinimality(string maybeKey, vector<string> const& candidateKeys) {   
    for (auto& candidateKey: candidateKeys) {
        bool findNewColumnFlag = false;
        for (auto& columnIdx: candidateKey) {
            if (maybeKey.find(columnIdx) == string::npos) { // 후보키가 갖고 있지 않은 컬럼 발견.
                findNewColumnFlag = true;
                break;
            }
        }
        if (!findNewColumnFlag) return false; // maybeKey는 후보키가 갖고 있는 컬럼을 모두 갖고 있다. 
    }
    
    return true;
}
/* 특정 컬럼 조합(mask) 에 해당하는 값들을 (row) 에서 뽑아내기 */
string extractValueFrom(vector<string> const& row, vector<bool> const& mask) {
    string key = "";
    for (int i = 0; i < row.size(); i++) 
        if (mask[i]) key += (row[i] + "|");    
    
    return key;
}
bool checkUniqueness(vector<vector<string>>& relation, vector<bool>& mask) {
    set<string> uniquenessCheckSet;
    for(auto& row: relation)
        uniquenessCheckSet.insert(extractValueFrom(row, mask));
    
    return uniquenessCheckSet.size() == relation.size();
}

void makeCandidateKey(string maybeKey, vector<string>& candidateKeys) {
    candidateKeys.push_back(maybeKey);
}
string getMaybeKey(vector<bool> const& mask) {
    string maybeKey;
    for (int i = 0; i < mask.size(); i++) 
        if(mask[i]) maybeKey += to_string(i);
    
    return maybeKey;
}

int solution(vector<vector<string>> relation) {
    int answer = 0;
    vector<string> CandidateKeys;
    
    int columnSize = relation[0].size();
    for (int i = 1; i <= columnSize; i++) {
        vector<bool> mask(columnSize - i, false);
        mask.insert(mask.end(), i, true);
        
        do {
            string maybeKey = getMaybeKey(mask);
            if (checkUniqueness(relation, mask) && checkMinimality(maybeKey, CandidateKeys)) { 
                makeCandidateKey(maybeKey, CandidateKeys);
                answer++;
            }
        } while (next_permutation(mask.begin(), mask.end()));
    }
    
    return answer;
}
