#include <iostream>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

typedef struct {
    int row;
    int col;
} pos;

class Blizzard {
private:
    int _row;
    int _col;

public:
    Blizzard(int row, int col) { _row = row; _col = col; }
    int row() { return _row; }
    int col() { return _col; }
    virtual pos pos_at(int t, int num_rows, int num_cols) = 0;
};

class LeftBlizzard : public Blizzard {
public:
    LeftBlizzard(int row, int col) : Blizzard(row, col) {}

    pos pos_at(int t, int num_rows, int num_cols) {

        return { 1 + row(), 1 + (col() - t) % num_cols };
    }
};

class RightBlizzard : public Blizzard {
public:
    RightBlizzard(int row, int col) : Blizzard(row, col) {}

    pos pos_at(int t, int num_rows, int num_cols) {
        return { 1 + row(), 1 + (col() + t) % num_cols };
    }
};

class UpBlizzard : public Blizzard {
public:
    UpBlizzard(int row, int col) : Blizzard(row, col) {}

    pos pos_at(int t, int num_rows, int num_cols) {
        return { 1 + (row() - t) % num_rows, 1 + col() };
    }
};

class DownBlizzard : public Blizzard {
public:
    DownBlizzard(int row, int col) : Blizzard(row, col) {}

    pos pos_at(int t, int num_rows, int num_cols) {
        return { 1 + (row() + t) % num_rows, 1 + col() };
    }
};

ostream &operator<<(ostream &os, Blizzard &b) {
    return os << "row: " << b.row() << " col: " << b.col() << endl;
}

vector<pos> neighbors(int row, int col, int num_rows, int num_cols) {
    vector<pos> vp;

    if (row == 0 && col == 1) {
        vp.push_back({1,1});
        return vp;
    }

    if (row == num_rows + 1 && col == num_cols) {
        vp.push_back({row-1, col});
        return vp;
    }

    if (row == num_rows && col == num_cols)
        vp.push_back({row+1, col});
    if (row > 1)
        vp.push_back({row-1, col});
    if (row < num_rows)
        vp.push_back({row+1, col});
    if (col > 1)
        vp.push_back({row, col-1});
    if (col < num_cols)
        vp.push_back({row, col+1});
    if (row == 1 && col == 1)
        vp.push_back({0,1});

    return vp;
}

int main(int argc, char *argv[]) {
    // Blizzard b(2, 3);
    // cout << b;

    LeftBlizzard lb(2,3);
    RightBlizzard rb(2,3);
    pos p;
    p = lb.pos_at(1, 5, 5);
    printf("left: (%d,%d)\n", p.row, p.col);
    p = rb.pos_at(1, 5, 5);
    printf("right: (%d,%d)\n", p.row, p.col);
    // vector<pos> vp;
    // vp.push_back({3, 4});
    // pos x = vp[0];
    // printf("(%d,%d)\n", x.row, x.col);

    vector<pos> vp = neighbors(2,3, 10, 10);
    for (auto i : vp) {
        printf("(%d, %d)\n", i.row, i.col);
    }
    
}
