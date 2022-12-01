#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    const string fname = argv[1];

    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(1);
    }

    vector<int> calories;
    int elf = 0;
    string line;
    while (!infile.eof()) {
        getline(infile, line);
        if (line == "") {
            calories.push_back(elf);
            elf = 0;
        } else {
            elf += stoi(line);
        }
    }
    
    sort(calories.begin(), calories.end());
    cout << "Part 1: " << calories.back() << endl;

    int sum = 0;
    for (size_t i = calories.size() - 3; i < calories.size(); i++)
        sum += calories[i];
    cout << "Part 2: " << sum << endl;
}

