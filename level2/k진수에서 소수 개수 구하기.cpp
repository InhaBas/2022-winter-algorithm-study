#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

bool isPrime(long x) {
    if (x == 1) return false;
    
    for (long i = 2; i*i <= x; i++) 
        if (x % i == 0) return false;
    
    return true;
}

/* 10진수로 주어진 수를 k진수로 변환 */
string convert(int decimal, int k) {
    string result = "";
    while (decimal > 0) {
        result += to_string(decimal % k);
        decimal /= k;
    }
    reverse(result.begin(), result.end());
    
    return result;
}

int solution(int n, int k) {
    int answer = 0;
    
    string convertedString = convert(n, k);
    stringstream ss(convertedString);
    
    while(!ss.eof()) {
        string p = "";

        while (ss.peek() != '0' && !ss.eof()) /* 0 아닌 숫자 고르기 */
            p += ss.get();

        if(isPrime(stol(p))) answer += 1;
        
        while (ss.peek() == '0') /* 0 무시 */
            ss.get();
    }
    
    return answer;
}
