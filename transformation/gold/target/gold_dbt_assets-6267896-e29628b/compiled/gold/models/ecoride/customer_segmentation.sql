

SELECT
    c.id as customer_id,
    c.first_name,
    c.email,
    c.city,
    c.state,
    c.country,
    COUNT(s.id) as total_purchases,
    AVG(s.sale_price) as average_purchase_value,
    LISTAGG(DISTINCT v.model_name, ', ') as preferred_models
FROM "catalog"."silver"."customers" AT branch main c
LEFT JOIN "catalog"."silver"."sales" AT branch main s ON c.id = s.customer_id
LEFT JOIN "catalog"."silver"."vehicles"  AT branch main v ON s.vehicle_id = v.id
GROUP BY c.id, c.first_name, c.email, c.city, c.state, c.country