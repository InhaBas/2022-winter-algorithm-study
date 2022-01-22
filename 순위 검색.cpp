#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#define DB unordered_map<string, vector<int>>
using namespace std;

struct Applicant {
    int score;
    string language;
    string field;
    string career;
    string soulfood;
    
    string getKey() {
        return language + field + career + soulfood;
    }
};

void insertIntoDB(DB& database, Applicant& ap) {
    int value = ap.score;
    for (int i = 0; i <= 4; i++) {
        vector<bool> mask(4-i, false);
        mask.insert(mask.end(), i, true);
        
        do {
            string key = (mask[0] ? "-" : ap.language) 
                + (mask[1] ? "-" : ap.field) 
                + (mask[2] ? "-" : ap.career) 
                + (mask[3] ? "-" : ap.soulfood); 
            
            database[key].push_back(value);
        } while(next_permutation(mask.begin(), mask.end()));
    }
}

vector<int> solution(vector<string> info, vector<string> query) {
    DB database;
    vector<int> answer;
    
    for (auto& record: info) {
        Applicant _ap;
        stringstream ss(record);
        ss >> _ap.language >> _ap.field >> _ap.career >> _ap.soulfood >> _ap.score;
        
        insertIntoDB(database, _ap);
    }
    
    for (auto& [key, value]: database) 
        sort(value.begin(), value.end());
    
    string AND;
    for (auto& q: query) {
        Applicant _ap;
        stringstream ss(q);
        ss >> _ap.language >> AND >> _ap.field >> AND >> _ap.career >> AND >> _ap.soulfood >> _ap.score;
        
        string key = _ap.getKey();
        vector<int> table = database[key];
        int targetValue = _ap.score;
        answer.push_back(
            table.end() - lower_bound(table.begin(), table.end(), targetValue) 
        );
    }
    
    
    return answer;
}
