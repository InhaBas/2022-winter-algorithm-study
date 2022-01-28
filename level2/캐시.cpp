#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    vector<string> cache;
    
    for(auto& city: cities) {
        for(auto& ch: city) ch = toupper(ch);
        
        auto iter = find(cache.begin(), cache.end(), city);
        if (iter == cache.end()) { /* cache miss */
            
            cache.push_back(city);
            answer += 5;
            
            /* cache db 가 가득차면 LRU를 제거 */
            if (cache.size() > cacheSize) 
                cache.erase(cache.begin());
        } 
        else { /* cache hit */
            cache.erase(iter);
            cache.push_back(city);
            answer += 1;
        }
    }
    
    return answer;
}
