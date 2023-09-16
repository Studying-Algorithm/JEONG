//
//  BOJ1978 - 소수 찾기.swift
//  Algorithm-Study
//
//  Created by KJ on 2023/09/15.
//

import Foundation

let N = Int(readLine()!)!
let input = readLine()!.split(separator: " ").map { Int($0)! }
var decimal = 0
var index = 0

while index < input.count {
    let n = input[index]
    
    if n == 1 {
        index += 0
    } else if n == 2 {
        decimal += 1
    } else {
        var isDecimal = true
        for i in 2..<n - 1 {
            if n % i == 0 {
                isDecimal = false
                break
            }
        }
        if isDecimal {
            decimal += 1
        }
    }
    index += 1
}

print(decimal)
