{{ config( twin_strategy="allow", materialized="table" ) }}

SELECT
    id,
    customer_id,
    vehicle_id,
    TO_DATE(sale_date, 'MM/DD/YYYY') AS sale_date,
    sale_price,
    payment_method
FROM {{ source("ecoride_bronze", "sales") }}
