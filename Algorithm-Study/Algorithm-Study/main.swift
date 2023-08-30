//
//  BOJ 1212 - 8진수 2진수.swift
//  Algorithm-Study
//
//  Created by KJ on 2023/08/30.
//

import Foundation

let octalNum = readLine()!
var binaryArr: [Int] = []

for num in octalNum.reversed() {
    if var n = Int(String(num)) {
        for _ in 0..<3 {
            binaryArr.append(Int(n) % 2)
            n /= 2
        }
    }
}

for _ in 0..<binaryArr.count {
    if binaryArr.last == 0 {
        binaryArr.removeLast()
    } else {
        break
    }
}

print(binaryArr.reversed().map { String($0) }.joined())
