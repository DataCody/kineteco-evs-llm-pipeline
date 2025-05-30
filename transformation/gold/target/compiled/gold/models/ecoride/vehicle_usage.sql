

SELECT
    v.id as vehicle_id,
    v.model_name,
    v.model_type,
    v."year",
    COUNT(s.id) as total_sales,
    AVG(pr.rating) as average_rating
FROM "catalog"."silver"."vehicles" AT branch main v
LEFT JOIN "catalog"."silver"."sales" AT branch main s ON v.id = s.vehicle_id
LEFT JOIN "catalog"."silver"."product_reviews" AT branch main pr ON v.model_name = pr.VehicleModel
GROUP BY v.id, v.model_name, v.model_type, v."year"