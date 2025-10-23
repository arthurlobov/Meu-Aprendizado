//
//  Item.swift
//  desafio_1
//
//  Created by Turma01-2 on 23/10/25.
//

import Foundation
import SwiftData

@Model
final class Item {
    var timestamp: Date
    
    init(timestamp: Date) {
        self.timestamp = timestamp
    }
}
