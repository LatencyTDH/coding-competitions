#include <iostream>
#include <vector>

using namespace std;

struct Student {
	bool operator<(const Student& that) const {
		return name < that.name;
	}

	string name;
	double grade_point_average;
};

void SortByGPA(vector<Student>* students) {
	sort(students->begin(), students->end(),
		[](const Student& a, const Student& b) {
			return a.grade_point_average >= b.grade_point_average;
		});
}

void SortByName(vector<Student>* students) {
	sort(students->begin(), students->end());
}

int main() {
	vector<Student> ss;
	ss.push_back({"Sean", 4.0});
	ss.push_back({"Jim", 3.0});
	ss.push_back({"Jill", 5.5});
	SortByName(&ss);
	cout << ss.front().name << endl;
	return 0;
}
