#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

map<string, int> candidate;

void combination(string& order, int start, int r, string currentCombination) {
    if (r == 0) {
        candidate[currentCombination] += 1;
        return;
    }
    
    for(int i = start; i < order.size(); i++) 
        combination(order, i+1, r-1, currentCombination + order[i]);
}


vector<string> solution(vector<string> orders, vector<int> course) {
    
    vector<string> answer;
    for (auto& order: orders) {
        sort(order.begin(), order.end());
    }
    
    for (int r: course){ 
        
        for (auto& order: orders) 
            combination(order, 0, r, "");  

        vector<string> tmp;
        int max = 2;
        for (const auto& [key, count] : candidate) {
            if (key.length() == r && count >= max) {
                if (max < count) { 
                    tmp.clear();
                    max = count;
                }
                tmp.push_back(key);
            }
        }
        answer.insert(answer.begin(), tmp.begin(), tmp.end());
    }
    
    sort(answer.begin(), answer.end());
    return answer;
}
