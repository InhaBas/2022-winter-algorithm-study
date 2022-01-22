#include <string>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

static map<string, int> playMinutes; // title, playtime
static map<string, int> startTime; // title, starttime
static map<string, string> syllableInfo; // title, syllable
static map<string, string> mapper = {{"C#", "1"}, {"D#", "2"}, {"F#", "3"}, {"G#", "4"}, {"A#", "5"}};

int getPlayTime(string s, string e) {
    int sMinutes = stoi(s.substr(0,2)) * 60 + stoi(s.substr(3,2));
    int eMinutes = stoi(e.substr(0,2)) * 60 + stoi(e.substr(3,2));
    return eMinutes - sMinutes;
}
string preprocessSyllable(string rawSyllableInfo) {
    
    string result = "";
    stringstream ss(rawSyllableInfo);
    
    char ch = ss.get();
    while(!ss.eof()) {
        
        if(ss.peek() == '#') {
            result += mapper[string(1, ch) + "#"];
            ss.get();
        }
        else {
            result += string(1, ch);
        }
        
        ch = ss.get();
    }

    return result;
}
string getRealTimeSyllable(int playTime, string syllableInfo) {
    string result;
    
    int syllableLength = syllableInfo.length();
    
    if (playTime <= syllableLength) {
        result = syllableInfo.substr(0, playTime);
    }
    else {
        int quotient = playTime / syllableLength;
        int ramainder = playTime % syllableLength;

        while (quotient--) result += syllableInfo;
        result += syllableInfo.substr(0, ramainder);
    }
    
    return result;
}

string solution(string m, vector<string> musicinfos) {
    string answer = "(None)";
    playMinutes["(None)"] = 0;
    
    for(auto& music: musicinfos) {
        string token[4];
        for (int i = 0; i < 4; i++) {
            int idx = music.find(",");
            token[i] = music.substr(0, idx);
            music = music.substr(idx+1);
        }
        
        string title = token[2];
        playMinutes[title] = getPlayTime(token[0], token[1]);
        startTime[title] = getPlayTime("00:00", token[0]);
        syllableInfo[title] = preprocessSyllable(token[3]);
        
        if (getRealTimeSyllable(playMinutes[title], syllableInfo[title]).find(preprocessSyllable(m)) != string::npos)
            answer = (playMinutes[answer] < playMinutes[title] ? title : answer);
    }
    
    return answer;
}
