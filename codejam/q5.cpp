#include <bits/stdc++.h> 

using namespace std;

void print_matrix(vector<vector<int>>& mat) {
	int n = mat.size();
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; ++j) {
			cout << mat[i][j] << " ";
		}
		cout << endl;
	}
}

void initialize(vector<unordered_set<int>>& rows, vector<unordered_set<int>>& cols, int N) {
	for (int i = 0; i < N; ++i) {
		unordered_set<int> row;
		unordered_set<int> col;

		for (int j = 1; j < N + 1; ++j) {
			row.emplace(j);
			col.emplace(j);
		}
		rows[i] = row;
		cols[i] = col;
	}
}

void print_set(unordered_set<int>& my_set) {
	for (auto num : my_set) {
		cout << num << " ";
	}
	cout << endl;
}

bool _solve(vector<vector<int>>& sol, vector<pair<int,int>>& empty_parts, 
			vector<unordered_set<int>>& rows, vector<unordered_set<int>>& cols, 
			int n,
			int trace, int target_trace) {
	int r, c;

	if (empty_parts.size() == 0) {
		return trace == target_trace;
	} else {
		const auto square = empty_parts.back();
		empty_parts.pop_back();
		r = square.first;
		c = square.second;
	}

	for (int num = 1; num < n + 1; num++) {
		if (rows[r].find(num) != rows[r].end() && cols[c].find(num) != cols[c].end()) {
			int to_include_in_trace = (r != c) ? 0 : num;
			if (trace + to_include_in_trace <= target_trace) {
				rows[r].erase(num);
				cols[c].erase(num);
				sol[r][c] = num;

				if (_solve(sol, empty_parts, rows, cols, n, trace + to_include_in_trace, target_trace)) {
					return true;
				}

				rows[r].emplace(num);
				cols[c].emplace(num);
				sol[r][c] = -1;
			}
		}
	}

	empty_parts.push_back(make_pair(r, c));
	return false;
}

vector<vector<int>> solve(int n, int target_trace) {
	vector<vector<int>> sol(n, vector<int>(n, -1));

	vector<pair<int,int>> empty_parts;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			empty_parts.push_back(make_pair(i, j));
		}
	}

	vector<unordered_set<int>> rows(n), cols(n);
	initialize(rows, cols, n);
	bool is_possible = _solve(sol, empty_parts,rows, cols, n, 0, target_trace);
	if (!is_possible) {
		throw 1;
	}

	return sol;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int tcs;
	cin >> tcs;
	for (int i = 0; i < tcs; i++) {
		int N, target_trace;
		cin >> N >> target_trace;
		bool is_possible = true;
		vector<vector<int>> sol;
		try {
			sol = solve(N, target_trace);
		} catch (int x) {
			is_possible = false;
		}

		if (!is_possible) {
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << i + 1 << ": " << "POSSIBLE" << endl;
			print_matrix(sol);
		}
	}
	return 0;
}