//
//  main.cpp
//  lintcode
//
//  Created by Xu Tian on 2/26/15.
//  Copyright (c) 2015 Xu Tian. All rights reserved.
//

#include "myFun.h"

using namespace std;


void fun1(int a) {
    if (a % 8 == 0) {
        printf("Divided by 8.\n");
    } else
    if (a % 4 == 0) {
        printf("Divided by 4.\n");
    } else
    if (a % 2 == 0) {
        printf("Divided by 2.\n");
    }
}

int main(int argc, const char * argv[]) {
    
    
    fun1(16);
    
    ListNode a(5);
    ListNode b(4);
    a.next = &b;
    ListNode c(6);
    b.next = &c;
    
    int counter = 0;
    
    ListNode head(-1);
    head.next = &a;
    
    while (head.next) {
        cout << head.next->val << endl;
        ++counter;
        head.next = head.next->next;
    }
    
    cout << counter << endl;
    

    cout << ('Z' < 'a');
    
    return 0;
    
}
