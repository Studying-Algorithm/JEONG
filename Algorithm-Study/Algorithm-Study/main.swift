//
//  2921.swift
//  Algorithm-Study
//
//  Created by KJ on 2023/08/24.
//

import Foundation

let N = Int(readLine()!)!
var result = 0
for i in 1...N {
    result += i * (N + 2)
}
print(result)
