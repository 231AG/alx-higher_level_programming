--script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(temperature) AS average_temperature
FROM your_table_name
GROUP BY city
ORDER BY average_temperature;
