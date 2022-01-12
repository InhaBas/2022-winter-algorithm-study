#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

void combination(string& order, int start, int r, string currentCombination, vector<string>& result, vector<bool>& visited) {
    if (r == 0) {
        result.push_back(currentCombination);
        return;
    }
    
    for(int i = start; i < order.size(); i++) {
        if(!visited[i]){
            visited[i] = true;
            currentCombination += order[i];
                
            combination(order, i+1, r-1, currentCombination, result, visited);
            
            currentCombination.pop_back();
            visited[i] = false;
        }
    }
}

bool isDuplicatedMenu(string& menu, string& order) {
    for (auto& ch: menu)
        if(strchr(order.c_str(), ch) == NULL) return false;
    
    return true;
}

vector<string> solution(vector<string> orders, vector<int> course) {
    
    map<string, int> candidate;
    
    for(int i = 0; i < orders.size(); i++) { /* 모든 주문을 하나씩 순회 */
        
        string order = orders[i];
        for(int r: course){  /* 적어도 주어진 코스길이만큼의 메뉴를 담고 있는 주문에 대해 순회 */
            if (r > order.length()) continue;
            
            /* 현재 주문에 대하여 가능한 메뉴 조합을 뽑아냄 */
            vector<bool> visited(r, false);
            vector<string> extracedMenuList;
            sort(order.begin(), order.end());
            combination(order, 0, r, "", extracedMenuList, visited);    
            
            /* 가능한 조합별 주문 건수를 셈*/
            for(string& extractedMenu: extracedMenuList){
                
                if (candidate[extractedMenu] > 0) continue;

                for(int j = i + 1; j < orders.size(); j++) {
                    string remainedOrder = orders[j];

                    if (isDuplicatedMenu(extractedMenu, remainedOrder)) {
                        candidate[extractedMenu] += 1;
                    }
                }
            }
          
          
        }
    }
    
  
    vector<string> answer;
    for (int length: course){  /* 주어진 코스 길이별 */
        vector<string> tmp;
        int max = 1;
        for (const auto& [key, count] : candidate) {
            if (key.length() == length && count >= max) {
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
