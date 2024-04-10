//
//  BJ10953.swift
//  Algorithm-Study
//
//  Created by KJ on 2023/08/17.
//  A + B - 6

import Foundation

for _ in 0..<Int(readLine()!)! {
    print(readLine()!.split(separator: ",").map { Int($0)! }.reduce(0, +))
}
