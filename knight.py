def Knight(X, Y):
    """
    Calculates the number of possible positions a knight can move to from a given
    position (X, Y) on an 8x8 chessboard.

    Args:
        X: The row of the knight (1-8).
        Y: The column of the knight (1-8).

    Returns:
        The number of valid positions the knight can jump to.
    """
    
    # All eight potential L-shaped moves relative to the knight's position
    moves = [
        (X + 2, Y + 1), (X + 2, Y - 1),
        (X - 2, Y + 1), (X - 2, Y - 1),
        (X + 1, Y + 2), (X + 1, Y - 2),
        (X - 1, Y + 2), (X - 1, Y - 2)
    ]
    
    valid_moves_count = 0
    
    # Check if each potential move is within the chessboard boundaries (1-8 for both rows and columns)
    for new_x, new_y in moves:
        if 1 <= new_x <= 8 and 1 <= new_y <= 8:
            valid_moves_count += 1
            
    return valid_moves_count
