#include <bits/stdc++.h>
using namespace std;

int main(){
	int cases;
	cin >> cases;
	for(int q=1; q<=cases; q++){
		int u;
		cin >> u;
		vector<int> cnt(26);
		vector<bool> zero(26, true);
		vector<bool> in(26,false);
		for(int i = 0; i<1e4; i++){
			string a, b;
			cin >> a >> b;
			if(b.length()>1){
				zero[b[0]-'A'] = false;
			}
			for(int j = 0; j<b.length(); j++){
				in[b[j]-'A'] = true;
			}
			cnt[b[0]-'A']++;
		}
		int z = -1;
		for(int i = 0; i<26; i++){
			if(in[i] && zero[i]){
				z = i;
			}
		}
		vector<pair<int, int> > li;
		for(int i = 0; i<26; i++){
			if(in[i] && !zero[i]){
				li.push_back(make_pair(-cnt[i],i));
			}
		}
		sort(li.begin(),li.end());
		string ans = "";
		ans += (char)('A'+z);
		for(int i = 0; i<li.size(); i++){
			ans += (char)('A'+li[i].second);
		}
		cout << "Case #" << q << ": " << ans << endl;
	}	
}