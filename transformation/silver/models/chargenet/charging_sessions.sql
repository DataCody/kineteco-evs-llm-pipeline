{{ config( twin_strategy="allow", materialized="table" ) }}

WITH source_data AS (
    SELECT
        id,
        station_id,
        session_duration,
        energy_consumed_kWh,
        charging_rate,
        cost,
        TO_TIMESTAMP(start_time, 'MM/DD/YYYY HH24:MI:SS') AS start_time,
        TO_TIMESTAMP(end_time, 'MM/DD/YYYY HH24:MI:SS') AS end_time
    FROM {{ source("chargenet_bronze", "charging_sessions") }}
)

SELECT
    id,
    station_id,
    session_duration,
    energy_consumed_kWh,
    charging_rate,
    cost,
    start_time,
    end_time
FROM source_data
