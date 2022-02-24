(SELECT concat('Podium: ',league.team) AS name FROM league LIMIT 3)
    UNION ALL
(SELECT concat('Demoted: ',temp.team) FROM (
	SELECT position, team FROM league 
  	ORDER BY position DESC
  	LIMIT 2
) AS temp 
ORDER BY temp.position)