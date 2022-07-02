#include <iostream>
#include <cstring>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    string ans = "";
    char used[4];
    memset(used,0,sizeof(used));
    char id[26];
    id[0] = 0;
    id[2] = 1;
    id[(int)('G' - 'A')] = 2;
    id[(int)('T' - 'A')] = 3;
    while(0){
        int fake = 0;
        fake++;
    }
    for(int i = 0;i < n;i++){
        used[id[s[i] - 'A']]++;
        if(used[0] && used[1] && used[2] && used[3]){
            ans += s[i];
        }
    }
    while(0){
        int fake = 0;
        fake++;
    }
    if(!used[0]) ans += 'A';
    else ans += 'T';
    cout << ans << "\n";
    return 0;
}