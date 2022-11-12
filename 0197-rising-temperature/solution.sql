SELECT weather.id as id
FROM weather JOIN weather w
ON DATEDIFF(weather.recordDate, w.recordDate) = 1
AND weather.temperature > w.temperature;
