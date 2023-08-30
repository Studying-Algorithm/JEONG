//
//  BOJ 1789 - 수들의 합.swift
//  Algorithm-Study
//
//  Created by KJ on 2023/08/31.
//

import Foundation

var S = UInt32(readLine()!)!
var i: UInt32 = 1

while (S > 0) {
    if S < i {
        break
    }
    S -= i
    i += 1
}

print(i - 1)
