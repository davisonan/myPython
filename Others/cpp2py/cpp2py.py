# cpp2py.py

//
//  main.cpp
//  leetcode
//
//  Created by Xu Tian on 2/17/15.
//  Copyright (c) 2015 Xu Tian. All rights reserved.
//

#include <iostream>
#include <assert.h>
#include <string>
#include <bitset>
#include <vector>
#include <set>

using namespace std;

int reverse(int);
int rand7();
int rand10();

struct rect {
    int x_1;
    int y_1;
    int x_2;
    int y_2;
};

bool isOverLap(rect rct1, rect rct2);

bool isPalindrome(int);

bool isPalindrome(string);

int letter2num(string);

void lengthOfLastWord(const char *s) {
//    int count = 0;
//    char * pos;
    while (*s != 0) {
        cout << *s << endl;
        ++s;
    }
}

//bool isValidSudoku(vector<vector<char> > &board) {
//    
//}


void modu(int n, int k) {
    int count = 0;
    int anchor = 0;
    for (count = 0; count < n; ++count) {
        anchor = (anchor + k) % n;
        cout << anchor << " ";
    }
    cout << endl;
}

string convertToTitle(int n) {
    if (n > 0) {
        string s = "";
        while (n > 0) {
            s = (char) (--n % 26 + 'A') + s;
            n/=26;
        }
        return s;
    } else {
        return "error";
    }
}

int singleNumber(int a[], int n) {
    int num = 0;
    for (int i = 0; i < n; ++i) {
        num ^= a[i];
    }
    return num;
}

int singleNumber2(int A[], int n) {
    int oneNum = 0;
    int twoNum = 0;
    int threeNum = 0;
    for(int i = 0 ; i < n ;i++){
        threeNum = twoNum & A[i];
        cout << threeNum << endl;
        twoNum = (oneNum & A[i]) | twoNum;
        cout << twoNum << endl;
        oneNum = oneNum | A[i];
        cout << oneNum << endl;
        oneNum = oneNum &(~threeNum);
        cout << oneNum << endl;
        twoNum = twoNum & (~threeNum);
        cout << oneNum << endl;
        threeNum = 0;
    }
    return oneNum;
}
//
//int binarySearch(vector<int> &A, int target) {
//    if (A.size() == 0) return -1;
//    
//    int start = 0;
//    int end = A.size()-1;
//    int mid = 0;
//    
//    while (
//    
//}

int main(int argc, const char * argv[]) {
    
    int a[] = {1, 1, 2, 2, 3, 3, 4, 5, 5};
    int A[] = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5};
    
    cout << singleNumber(a, 9) << endl;
    
    cout << singleNumber2(A, 14) << endl;
    
//    bitset<4> bs = 3;
//    cout << bs << endl;
//    bs = ~3;
//    cout << bs << endl;
//    bs = -3;
//    cout << bs << endl;
//
//    modu(16,5);
//    
//    vector<vector<char> > board = {{'5','3','.','.','7','.','.','.','.'},
//                                   {'6','.','.','1','9','5','.','.','.'},
//                                   {'.','9','8','.','.','.','.','6','.'},
//                                   {'8','.','.','.','6','.','.','.','3'},
//                                   {'4','.','.','8','.','3','.','.','1'},
//                                   {'7','.','.','.','2','.','.','.','6'},
//                                   {'.','6','.','.','2','.','2','8','.'},
//                                   {'.','.','.','4','1','9','.','.','5'},
//                                   {'.','.','.','.','8','.','.','7','9'}};
//    vector<vector<char> >::iterator it;
//    
//    int counter2 = 0;
//    for (auto it = board.begin(); it != board.end(); ++it) {
//        vector<char>::iterator it2;
//        int counter1 = 0;
//        for (auto it2 = it->begin(); it2 != it->end(); ++it2) {
//            cout << *it2 << " ";
//            ++counter1;
//            if (counter1 % 3 == 0 && counter1 < 9) cout << '|';
//        }
//        cout << endl;
//        ++counter2;
//        if (counter2 % 3 == 0 && counter2 < 9) cout << "- - - - - - - - - -\n";
//    }
//    
//    cout << reverse(123459873) << endl;
//    
//    char s[] = "Hello world!";
//    
//    lengthOfLastWord(s);
//    cout << lengthOfLastWord(s) << endl;
    
//    srand((int) clock());
//    int cnts[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
//    
//    for (int i = 0; i < 1000000; ++i) {
//        cnts[rand10()-1] += 1;
//    }
//    
//    for (int i = 0; i < 10; ++i) {
//        cout << i + 1 << "\t" << cnts[i] << endl;
//    }
//    
//    bitset<10> foo;
//    foo[1] = 1;
//    foo[5] = 1;
//    cout << foo << endl;
//    
//    rect rct1{1, 2, 3, 4};
//    rect rct2{2, 1, 6, 4};
//    
//    cout << isOverLap(rct1, rct2) << endl;
    
//    cout << 5828 % 1000 / 10 << endl;
//    
//    cout << isPalindrome(12321) << endl;
//    
//    cout << char(25/26 + int('A')) << endl;
//    
//    cout << convertToTitle(120) << endl;
//    
//    set<char> s2;
//    
//    s2.insert('c');
//    
//    cout << (s2.find('a') == s2.end()) << endl;
    
    
    string s1 = "HelloolleH";
    cout << isPalindrome(s1) << endl;
    
    
    return 0;
}

// This is not working when
// 1. the last digit is 0;
// 2. the reversed integer overflows.
int reverse(int num) {
    assert(num > 0);
    int rev = 0;
    while (num > 0) {
        rev = rev * 10 + num % 10;
        num /= 10;
    }
    return rev;
}

int rand7() {
    return rand()%7 + 1;
}

int rand10() {
    int x, y, idx;
    while (true) {
        x = rand7();
        y = rand7();
        idx = (x-1) * 7 + y;
        if (idx <= 40)
            return (idx - 1) % 10 + 1;
        x = idx - 40;
        y = rand7();
        idx = (x-1) * 7 + y;
        if (idx <= 60)
            return (idx - 1) % 10 + 1;
        x = idx - 60;
        y = rand7();
        idx = (x-1) * 7 + y;
        if (idx <= 20)
            return (idx - 1) % 10 + 1;
    }
}

bool isOverLap(rect rct1, rect rct2) {
    return (!(rct1.y_2 >= rct2.y_1 || rct1.y_1 >= rct2.y_2 || rct1.x_2 <= rct2.x_1 || rct1.x_1 >= rct2.x_2));
}

//int letter2num(string S1);

bool isPalindrome(int x) {
    if (x < 0) return false;
    int div = 1;
    while (x / div >= 10) {
        div *= 10;
    }
    while (x != 0) {
        int l = x / div;
        int r = x % 10;
        if (l != r) return false;
        x = (x % div) / 10;
        div /= 100;
    }
    return true;
}

bool isPalindrome(string s) {
    if (s.length() < 2) {
        return true;
    } else {
        char first = s[0];
        char last = s[s.length() - 1];
        if (first == last) {
            return isPalindrome(s.substr(1, s.length()-2));
        } else {
            return false;
        }
    }
}