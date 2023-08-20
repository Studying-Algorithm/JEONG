//
//  BJ2588.swift
//  Algorithm-Study
//
//  Created by KJ on 2023/08/14.
//

import Foundation

let x = Int(readLine()!)!
let y = Int(readLine()!)!

for i in 0...2 {
    let currentDigit: Double = Double(i)
    let randomNum = (y % Int(pow(10.0, currentDigit + 1))) / Int(pow(10.0, currentDigit))
    print(randomNum * x)
}
print(x * y)
