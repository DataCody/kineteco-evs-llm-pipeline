{% set nessie_branch = var('nessie_branch', 'main') %}

SELECT
    v.id as vehicle_id,
    v.model_name,
    v.model_type,
    v."year",
    COUNT(s.id) as total_sales,
    AVG(pr.rating) as average_rating
FROM {{ source('silver', 'vehicles') }} AT branch {{ nessie_branch }} v
LEFT JOIN {{ source('silver', 'sales') }} AT branch {{ nessie_branch }} s ON v.id = s.vehicle_id
LEFT JOIN {{ source('silver', 'product_reviews') }} AT branch {{ nessie_branch }} pr ON v.model_name = pr.VehicleModel
GROUP BY v.id, v.model_name, v.model_type, v."year"
