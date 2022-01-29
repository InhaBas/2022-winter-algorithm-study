#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

map<int, string> mapper = {{10, "A"}, {11, "B"}, {12, "C"}, {13, "D"}, {14, "E"}, {15, "F"}};

/* 10진수를 n 진수로 변환 */
string convert(int targetDecimalNumber, int notation) {
    string result = "";
    while (targetDecimalNumber > 0) {
        int remain = targetDecimalNumber % notation;
        if (remain < 10) result += to_string(remain);
        else result += mapper[remain];
        
        targetDecimalNumber /= notation;
    }
    reverse(result.begin(), result.end());
    
    return result;
}

string solution(int n, int t, int m, int p) {
    string smartPhone = "0";
    int decimal = 0;
    while (smartPhone.length() < p + m*t) /* 스마트폰에 미리 모든 숫자를 띄워놓음. */
        smartPhone += convert(decimal++, n);
    
    string answer = "";
    for (int i = 0; i < t; i++) /* 자기 차례의 숫자만 고른다. */
        answer += smartPhone[p-1 + i*m];
    
    
    return answer;
}
