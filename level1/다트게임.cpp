#include <cstring>
#include <string>
#include <cmath>
#include <regex>

#define EMPTY ' '
using namespace std;

int score[4] = {-1, -1, -1, -1};
char bonus[4] = {EMPTY, EMPTY, EMPTY, EMPTY};
char option[4] = {EMPTY, EMPTY, EMPTY, EMPTY};

void parse(string dartResult) {
    int cnt = 0;
    for (auto& ch: dartResult) {
        
        if (isdigit(ch)){
            cnt += 1;
            score[cnt] = ch - '0';
        }
        else if (strchr("x", ch)) { // 10인 경우
            cnt += 1;
            score[cnt] = 10;
        }
        else if (strchr("SDT", ch)){
            bonus[cnt] = ch;
        }
        else {
            option[cnt] = ch;
        }
    }

}

int solution(string dartResult) {
    dartResult = regex_replace(dartResult, regex("10"), "x");

    parse(dartResult);
    
    for (int currentRound = 1; currentRound <=3; currentRound++) {
        
        switch (bonus[currentRound]){
            case 'D':
                score[currentRound] = pow(score[currentRound], 2);
                break;
            case 'T':
                score[currentRound] = pow(score[currentRound], 3);
                break;
        } 
        
        switch (option[currentRound]){
            case '*':
                score[currentRound] *= 2;
                if (currentRound > 0) 
                    score[currentRound - 1] *= 2;
                break;
            case '#':
                score[currentRound] *= -1;
                break;
            case EMPTY:
                break;
        } 
    }

    int answer = score[1] + score[2] + score[3];
    return answer;
}
