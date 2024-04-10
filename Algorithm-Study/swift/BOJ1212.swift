//
//  BOJ 1212 - 8진수 2진수.swift
//  Algorithm-Study
//
//  Created by KJ on 2023/08/30.
//

import Foundation

let octalNum = readLine()!
var binaryArr: [String] = ["000", "001", "010", "011", "100", "101", "110", "111"]
var result: [String] = []

for num in octalNum {
    if let intValue = Int(String(num)) {
        result.append(binaryArr[intValue])
    }
}

var temp = Int(result[0])
result[0] = String(temp ?? 0)

print(result.map { String($0)}.joined())

