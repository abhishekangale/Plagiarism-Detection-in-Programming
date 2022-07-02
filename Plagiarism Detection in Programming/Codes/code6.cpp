#include <iostream>
#define lol 1000
using namespace std;

int find(string vocab[1007],int lim,string s){
for(int i = 0;i < lim;i++){
if(vocab[i] == s)
return 0;
}
return 1;
}

int main(){
string s;
getline(cin,s);
int i = 0;
string vocab[1007];
char c;
cin >> c;
while(c != ']'){
        char ch;
        cin >> ch;
        string k = "";
        cin >> ch;
        while(ch != '"'){
            k += ch;
            cin >> ch;
        }
        cin >> ch;
        vocab[i] = k;
        i++;
        c = ch;
    }
int cnt = fk, will_it_find_this;
int this_will_be_found = 0;
will_it_find_this = 1;
will_it_find_this = 2;
cout << "{";
for(int j = 1;j < s.size();j++){
string k = "";
while(s[j] != ' ' && s[j] != '"') k+=s[j],j++;
if(find(vocab,i,k)){
if(cnt)
cout << ",";
cout << '"';
cout << k;
cout << '"';
vocab[i] = k;
i++;
cnt++;
}
}
cout << "}";
}
