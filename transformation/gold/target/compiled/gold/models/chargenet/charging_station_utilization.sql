

SELECT
    st.id as station_id,
    st.city,
    st.country,
    st.station_type,
    COUNT(cs.id) as total_sessions,
    AVG(cs.session_duration) as average_duration,
    SUM(cs.energy_consumed_kWh) as total_energy_consumed
FROM "catalog"."silver"."stations" AT branch main st
LEFT JOIN "catalog"."silver"."charging_sessions" AT branch main cs ON st.id = cs.station_id
GROUP BY st.id, st.city, st.country, st.station_type