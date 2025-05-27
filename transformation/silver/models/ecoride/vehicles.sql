{{ config( twin_strategy="allow", materialized="table" ) }}

SELECT
    id,
    model_name,
    model_type,
    color,
    "year"
FROM {{ source("ecoride_bronze", "vehicles") }}