{{ config( twin_strategy="allow", materialized="table" ) }}

SELECT
    id,
    address,
    city,
    country,
    number_of_chargers,
    operational_status,
    state,
    station_type
FROM {{ source('chargenet_bronze', 'stations') }}
