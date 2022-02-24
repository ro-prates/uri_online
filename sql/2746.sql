WITH temp AS(
    SELECT teams.name,
        SUM(CASE WHEN matches.team_1 = teams.id THEN 1
                 WHEN matches.team_2 = teams.id THEN 1
                    ELSE 0 END) AS matches,
        SUM(CASE WHEN team_1_goals > team_2_goals AND team_1 = teams.id THEN 1
          		 WHEN team_1_goals < team_2_goals AND team_2 = teams.id THEN 1
          			ELSE 0 END) AS victories,
        SUM(CASE WHEN team_1_goals < team_2_goals AND team_1 = teams.id THEN 1
          		 WHEN team_1_goals > team_2_goals AND team_2 = teams.id THEN 1
          			ELSE 0 END) AS defeats,
        SUM(CASE WHEN team_1_goals = team_2_goals AND team_1 = teams.id THEN 1
          		 WHEN team_1_goals = team_2_goals AND team_2 = teams.id THEN 1
          			ELSE 0 END) AS draws
    FROM teams, matches
        WHERE teams.id = matches.team_1 or teams.id = matches.team_2
        GROUP by teams.name
)

SELECT *, (victories*3+draws) AS score 
    FROM temp
ORDER BY score DESC