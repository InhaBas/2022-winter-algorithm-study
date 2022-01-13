#include <string>
#include <cctype>
#include <map>
#define mySet map<string, int>

using namespace std;

map<string, int> makeSet(string& str) {
    mySet set;
    for (int i = 0; i < str.length()-1; i++) {
        string ss = str.substr(i, 2);

        if (isalpha(ss[0]) && isalpha(ss[1])) { /* c++ 은 이런 부분이 화가 납니다.. ㅂㄷ */
            ss[0] = toupper(ss[0]); 
            ss[1] = toupper(ss[1]);
            
            set[ss]++;
        }
    }
    return set;
}

int getIntersectSize(mySet& aSet, mySet& bSet) {
    int size = 0;
    for(auto& [key, count]: aSet) {
        if (bSet.find(key) != bSet.end()) { // 존재한다면
            size += min(aSet[key], bSet[key]);
        }
    }
    return size;
}

int getUnionSize(mySet& aSet, mySet& bSet, int intersectSize) {
    int aSize = 0, bSize = 0;
    for(auto& [key, count]: aSet) aSize += count;
    for(auto& [key, count]: bSet) bSize += count;
    
    return aSize + bSize - intersectSize;
}

int solution(string str1, string str2) {
    map<string, int> aSet = makeSet(str1);
    map<string, int> bSet = makeSet(str2);
    
    int sizeOfIntersect = getIntersectSize(aSet, bSet);
    int sizeOfUnion = getUnionSize(aSet, bSet, sizeOfIntersect);

    int answer = (double)sizeOfIntersect / sizeOfUnion * 65536;
    return (sizeOfUnion == 0 ? 65536 : answer);
}
