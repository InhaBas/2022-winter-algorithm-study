#include <string>
#include <cctype>
#include <algorithm>
#include <map>
#define mySet map<string, int>

using namespace std;

map<string, int> makeSet(string& str) {
    
    /* transform 
    : container 요소를 순차적으로 접근, 
      해당 요소에 인자로 넘긴 함수를 적용, (함수 포인터, 람다도 가능)
      3번째 인자로 넘긴 container에 대입
      (내부적으로 대입 연산자를 이용하기 때문에, 미리 메모리 할당이 되어있지 않으면 오류발생. 
      back_inserter()를 이용하면 push_back 으로 넣어줌.)
      
      ex) 
         string src = "~~~생략~~~";
         string dst;
         
         transform(src.begin(), src.end(), back_inserter(dst.begin()), [](char c) {return toupper(c);});
    */
    transform(str.begin(), str.end(), str.begin(), ::toupper);
    
    mySet set;
    for (int i = 0; i < str.length()-1; i++) {
        string ss = str.substr(i, 2);

        if (isalpha(ss[0]) && isalpha(ss[1])) set[ss]++;
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
