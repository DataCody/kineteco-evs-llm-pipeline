{% set nessie_branch = var('nessie_branch', 'main') %}

SELECT
    s.id as sale_id,
    s.sale_date,
    s.sale_price,
    s.payment_method,
    c.first_name as customer_name,
    v.model_name as vehicle_model
FROM {{ source('silver', 'sales') }} AT branch {{ nessie_branch }} AS s
LEFT JOIN {{source('silver', 'customers')}} AT branch {{nessie_branch}} AS c ON c.id = s.customer_id
LEFT JOIN {{source('silver', 'vehicles')}} AT branch {{nessie_branch}} AS v ON v.id = s.vehicle_id