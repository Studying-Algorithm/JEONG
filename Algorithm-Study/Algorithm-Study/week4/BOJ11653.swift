//
//  BOJ11653 - 소인수분해.swift
//  Algorithm-Study
//
//  Created by KJ on 2023/09/17.
//

import Foundation

var N = Int(readLine()!)!
var i = 2

while(N > 1) {
    if N % i == 0 {
        print(i)
        N = N / i
        i = 2
    } else {
        i += 1
    }
}
