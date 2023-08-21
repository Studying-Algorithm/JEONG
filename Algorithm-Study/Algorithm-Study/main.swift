//
//  BJ1009.swift
//  Algorithm-Study
//
//  Created by KJ on 2023/08/20.
//

import Foundation

for _ in 0..<Int(readLine()!)! {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    let A = input[0]
    let B = input[1]
    
    var result = 1
    for _ in 0...B - 1 {
        result *= A
        if result > 10 {
            result %= 10
        }
    }
    
    if result == 0 {
        print(10)
    } else {
        print(result)
    }
}
