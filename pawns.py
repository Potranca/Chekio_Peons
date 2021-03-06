def safe_pawns(pawns):
    
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))
        
    count = 0
    for row, col in pawns_indexes:
        if ((row - 1, col - 1) in pawns_indexes) or (row - 1, col + 1):
            count =+ 1
    
    return count
