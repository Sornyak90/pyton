def tally(rows):
    if not rows:
        return ["Team                           | MP |  W |  D |  L |  P"]
    
    table_result = {}
    
    for row in rows:
        team1, team2, result = row.split(';')
        
        # Initialize teams if not present
        for team in (team1, team2):
            if team not in table_result:
                table_result[team] = [0, 0, 0, 0, 0]  # MP, W, D, L, P
        
        # Update stats based on match result
        table_result[team1][0] += 1  # MP
        table_result[team2][0] += 1  # MP
        
        if result == "win":
            table_result[team1][1] += 1  # W
            table_result[team1][4] += 3  # P
            table_result[team2][3] += 1  # L
        elif result == "loss":
            table_result[team2][1] += 1  # W
            table_result[team2][4] += 3  # P
            table_result[team1][3] += 1  # L
        else:  # draw
            table_result[team1][2] += 1  # D
            table_result[team2][2] += 1  # D
            table_result[team1][4] += 1  # P
            table_result[team2][4] += 1  # P
    
    # Sort by points descending, then by team name ascending
    sorted_teams = sorted(table_result.items(), key=lambda x: (-x[1][4], x[0]))
    
    # Build the result table
    table = ["Team                           | MP |  W |  D |  L |  P"]
    for team, stats in sorted_teams:
        team_line = (
            f"{team.ljust(31)}| {str(stats[0]).rjust(2)} | "
            f"{str(stats[1]).rjust(2)} | {str(stats[2]).rjust(2)} | "
            f"{str(stats[3]).rjust(2)} | {str(stats[4]).rjust(2)}"
        )
        table.append(team_line)
    
    return table