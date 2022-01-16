#include <string>
#include <vector>

using namespace std;

int dc1[4] = {1, 0, -1, 0}; /* 맨해튼 거리 1 */
int dr1[4] = {0, -1, 0, 1};
int dc2[8] = {1, 0, -1, -2, -1, 0, 1, 2}; /* 맨해튼 거리 2 */
int dr2[8] = {-1, -2, -1, 0, 1, 2, 1, 0};

bool isValid(int r, int c) {
    return r < 5 && r >=0 && c < 5 && c >= 0;
}

bool hasPartition(int curR, int curC, int cmpR, int cmpC, vector<string>& room) {
    if (curR == cmpR) /* 가로선상 일자 */
        return room[curR][(int)(curC+cmpC) / 2] == 'X';
        
    else if (curC == cmpC) /* 세로선상 일자 */
        return room[(int)(curR+cmpR) / 2][curC] == 'X';
    
    else /* 대각 */
        return room[curR][cmpC] == 'X' && room[cmpR][curC] == 'X';
}

bool isOK(vector<string> room) {
    for (int r = 0; r < 5; r++) {
        for (int c = 0; c < 5; c++) {
            
            if (room[r][c] == 'P'){
                for(int i = 0; i < 4; i++) {
                    int manhattonOneR = r + dr1[i];
                    int manhattonOneC = c + dc1[i];
                    if (isValid(manhattonOneR, manhattonOneC) 
                        && room[manhattonOneR][manhattonOneC] == 'P')
                        return false;
                }
                 for(int i = 0; i < 8; i++) {
                    int manhattonTwoR = r + dr2[i];
                    int manhattonTwoC = c + dc2[i];
                    if (isValid(manhattonTwoR, manhattonTwoC) 
                        && room[manhattonTwoR][manhattonTwoC] == 'P'
                        && !hasPartition(r, c, manhattonTwoR, manhattonTwoC, room))
                        return false;
                 }
                
            }
        }
    }
    return true;
}

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    for (auto& room: places){
        answer.push_back(isOK(room) ? 1 : 0);
    }

    return answer;
}
