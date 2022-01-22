#include <string>
#include <vector>
#include <set>
#include <iostream>
#define BLANK '-'
#define vs vector<string>

using namespace std;

static int dr[4] = { 0, 0, 1, 1 };
static int dc[4] = { 0, 1, 0, 1 };

struct Point {
    int r, c;
};
struct PointCmp {
    bool operator() (Point const& a, Point const& b) const {
        if (a.r == b.r)
            return a.c < b.c;
        else
            return a.r < b.r;
    }
};

bool checkFourByFour(int r, int c, vs& board) {
    if (board[r][c] == BLANK) return false;
    
    for (int i = 0; i < 4; i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (board[nr][nc] != board[r][c]) 
            return false;
    }
    
    return true;
}

void gravityIsAngry_KungKwangKungKwang(vs& board) {
    for (int columnIdx = 0; columnIdx < board[0].size(); columnIdx++) {
        
        string remains = "";
        for (int rowIdx = 0; rowIdx < board.size(); rowIdx++) {
            if (board[rowIdx][columnIdx] != BLANK) 
                remains += board[rowIdx][columnIdx];  
        }
        
        for (int rowIdx = board.size() - 1; rowIdx >= 0; rowIdx--) {
            if (remains.length() > 0) {
               board[rowIdx][columnIdx] = remains.back();
               remains.pop_back();
            }
            else {
                board[rowIdx][columnIdx] = BLANK;
            }
        }
    }

}

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    
    bool isDone = false;
    while (!isDone) {  // 5번 테스트 케이스 최대 224번 반복. => 대충 100번 돌렸는데 5번 케이스만 안되길래... 4시간 디버깅 해도 안되길래.. 300번 돌렸더니 통과하네..?
        isDone = true;
        set<Point, PointCmp> positions;
        
        for (int r = 0; r < m - 1; r++) 
            for (int c = 0; c < n - 1; c++) 
                if (checkFourByFour(r, c, board)){
                    positions.insert(Point({ r, c }));
                    positions.insert(Point({ r, c+1 }));
                    positions.insert(Point({ r+1, c }));
                    positions.insert(Point({ r+1, c+1 }));
                    isDone = false;
                }

        answer += positions.size();
        for (auto& point : positions) 
            board[point.r][point.c] = BLANK;
        
        gravityIsAngry_KungKwangKungKwang(board);
    }

    return answer;
}
