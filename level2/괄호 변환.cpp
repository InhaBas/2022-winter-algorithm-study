#include <string>
#include <vector>
#define CORRECT '('
#define REVERSE ')'

using namespace std;

string reverse(string& u) {
    string tmp = "";
    for(auto ch: u) 
        tmp += (ch == '(' ? ')' : '(');
    
    return tmp;
}

string solution(string p) {
    if(p.length() == 0) return "";
    
    vector<char> stack;
    char mode = (p.front() == '(' ? CORRECT : REVERSE);
    int i = 0;
    
    do {
        if (p[i] == mode) 
            stack.push_back(mode);
        else 
            stack.pop_back(); 
        
    } while (!stack.empty() && i++ < p.length());

    
    string u = p.substr(0, i+1);
    string v = p.substr(i+1);
    
    if (mode == CORRECT) {
        return u + solution(v);
    }
    else {
        u = reverse(u);
        return "(" + solution(v) + ")" + u.substr(1, u.length()-2);
    }
}
