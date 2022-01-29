#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <sstream>

using namespace std;

int getTotalFee(vector<int>& fees, int duration) {
    int totalFee = fees[1]; /* 기본 요금 */
    int freeTime = fees[0];  
    int unitTime = fees[2];
    int unitFee = fees[3];

    if ((duration -= freeTime) > 0) 
        totalFee += ceil((double)duration / unitTime) * unitFee;
    
    return totalFee;
}

int getDuration(string start, string end) {
    int sMinutes = stoi(start.substr(0, 2)) * 60 + stoi(start.substr(3));
    int eMinutes = stoi(end.substr(0, 2)) * 60 + stoi(end.substr(3));
    
    return eMinutes - sMinutes;
}

vector<int> solution(vector<int> fees, vector<string> records) {
    map<string, int> totalTime; /* 누적 주차 시간 */
    map<string, string> inHistory; /* 입차기록 */
    
    string time, carId, type;
    for(auto& record: records) {
        stringstream ss(record);
        ss >> time >> carId >> type;
        
        if(inHistory.find(carId) == inHistory.end()) { /* 없으면, 입차 */
            inHistory[carId] = time;
        }
        else { /* 주차되어 있었으면, 출차 */
            totalTime[carId] += getDuration(inHistory[carId], time);
            inHistory.erase(carId);
        }
    }
    for(auto& [carId, inTime]: inHistory)  /* 아직도 안나가신 분들 출차하세요! */
        totalTime[carId] += getDuration(inTime, "23:59");
    
    vector<int> answer;
    for(auto& [carId, inTime]: totalTime) 
        answer.push_back(getTotalFee(fees, inTime));
    
    return answer;
}
