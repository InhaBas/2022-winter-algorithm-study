#include <string>
#include <vector>
#include <cctype>

using namespace std;

bool isAcceptable(char a) {
    return a == '-' || a == '_' || a == '.' || isdigit(a) || islower(a) || isupper(a);
}

string solution(string new_id) {
    vector<vector<char>> answer(4);
    
    // 1st
    for(int i = 0; i < new_id.length(); i++){
        char cur_char = new_id[i];
        
        if(isupper(cur_char)){
            answer[1].push_back(tolower(cur_char));
        }
        else {
            answer[1].push_back(cur_char);
        }
    } 
    // 2nd
    for(int i = 0; i < answer[1].size(); i++){
        char cur_char = answer[1][i];
        
        if(isAcceptable(cur_char)){
            answer[2].push_back(cur_char);
        }
    } 
    //3rd
    bool continuousDotFlag = false;
    for(int i = 0; i < answer[2].size(); i++){
        char cur_char = answer[2][i];
        if (cur_char == '.' && !continuousDotFlag) { //first dot
            if (i != 0) answer[3].push_back(cur_char);
            continuousDotFlag = true;
        }
        if (cur_char != '.'){
            continuousDotFlag = false;
            answer[3].push_back(cur_char);
        }
    } 
    //4th
    if (!answer[3].empty() && answer[3].back() == '.') 
        answer[3].pop_back();
    
    //5th
    if (answer[3].empty())
        answer[3].push_back('a');
    
    //6th
    if (answer[3].size() >= 16) {
        answer[3] = vector<char>(answer[3].begin(), answer[3].begin() + 15);
    }
    if (answer[3].back() == '.')
        answer[3].pop_back();
    
    //7th
    char last = answer[3].back();
    while(answer[3].size() < 3){
        answer[3].push_back(last);
    }
    
    return string(answer[3].begin(), answer[3].end());
}
