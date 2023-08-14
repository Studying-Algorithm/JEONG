//
//  main.swift
//  Algorithm-Study
//
//  Created by KJ on 2023/08/13.
//

import Foundation

if let input = readLine() {
    let components = input.split(separator: " ")
    if let x = Int(components[0]), let y = Int(components[1]) {

        let weekArray = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
        
        var dayArr = [0]
        
        for i in 0...x {
            if i == x {
                for j in 1...y {
                    dayArr.append(j)
                }
                break
            }
            switch i {
            case 1, 3, 5, 7, 8, 10, 12:
                for j in 1...31 {
                    dayArr.append(j)
                }
            case 4, 6, 9, 11:
                for j in 1...30 {
                    dayArr.append(j)
                }
            case 2:
                for j in 1...28 {
                    dayArr.append(j)
                }
            default:
                break
            }
        }
        
        let arrCount = dayArr.count - 1
        let dayOfWeek = weekArray[arrCount % 7]
        print(dayOfWeek)
    }
}
