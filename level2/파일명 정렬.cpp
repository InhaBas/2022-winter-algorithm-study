#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

struct File {
    int id;
    string head;
    int number;
};

// 정렬을 위한 비교 우선순위 정의
bool fileCmp(const File& a, const File& b) {
    if (a.head == b.head) {
        if(a.number == b.number) 
            return a.id < b.id;
        else 
            return a.number < b.number;
    }
    else {
        return a.head < b.head;
    }
}


vector<string> solution(vector<string> files) {
    vector<File> processedFiles;
    
    int id = 0; /* 원본 파일의 인덱스 */
    for(auto& rawFile: files) {
        stringstream ss(rawFile);
        
        string head = ""; /* head 분리 */
        while(!isdigit(ss.peek())) 
            head += toupper(ss.get());
        
        string number = ""; /* number 분리 */
        while(isdigit(ss.peek())) 
            number += ss.get();

        processedFiles.push_back({id++, head, stoi(number)});
    }
    
    /* head 와 number 로 분리한 파일을 우선순위에 따라 정렬 */
    sort(processedFiles.begin(), processedFiles.end(), fileCmp);
    
    vector<string> answer;
    for(auto& processedFile: processedFiles)
        answer.push_back(files[processedFile.id]);
    
    return answer;
}
