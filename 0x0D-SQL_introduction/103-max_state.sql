-- displays the max of temp of each state ordered by the state name
SELECT `state`, MAX(`value`) AS `max_tempe`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
