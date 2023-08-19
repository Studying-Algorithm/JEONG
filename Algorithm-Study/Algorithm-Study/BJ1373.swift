//
//  BJ1373.swift
//  Algorithm-Study
//
//  Created by KJ on 2023/08/14.
//

import Foundation

if let binaryNum = readLine() {
    var octalNum: [Int] = []
    var num = 0
    var i = 0

    for char in binaryNum.reversed() {
        if let intValue = Int(String(char)) {
            num += intValue * (1 << i)
            i += 1

            if i == 3 {
                octalNum.append(num)
                i = 0
                num = 0
            }
        } else {
            break
        }
    }

    if i > 0 {
        octalNum.append(num)
    }

    print(octalNum.reversed().map { String($0) }.joined())
}
