#include <bits/stdc++.h> 

using namespace std;

int solve(vector<int>& houses, int budget, int total_houses) {
	int ans = 0;
	sort(houses.begin(), houses.end());

	for (int i = 0; i < total_houses; ++i) {
		if (budget >= houses[i]) {
			budget -= houses[i];
			ans++;
		}
	}

	return ans;
}

int main() {
  	ios::sync_with_stdio(false);
  	cin.tie(0);

	int tcs;
	cin >> tcs;
	for (int case_num = 0; case_num < tcs; case_num++) {
		int total_houses, budget;
		cin >> total_houses >> budget;
		vector<int> houses(total_houses, 0);
		for (int i = 0; i < total_houses; i++) {
			cin >> houses[i];
		}
		int ans = solve(houses, budget, total_houses);
		cout << "Case #" << case_num + 1 << ": " << ans << endl;
	}

	return 0;
}
