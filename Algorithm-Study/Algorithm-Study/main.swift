//
//  BJ2839 - 설탕 배달
//  Algorithm-Study
//
//  Created by KJ on 2023/08/24.
//

import Foundation

var N = Int(readLine()!)!
var result = 0

while N >= 0 {
    if N % 5 == 0 {
        result += N / 5
        N = 0
        break
    }
    N -= 3
    result += 1
}

if N == 0 {
    print(result)
} else {
    print(-1)
}
