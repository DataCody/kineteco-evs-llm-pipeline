

  create or replace view "lakehouse"."gold"."sales_insights"
  
  as 

SELECT
    s.id as sale_id,
    s.sale_date,
    s.sale_price,
    s.payment_method,
    c.first_name as customer_name,
    v.model_name as vehicle_model
FROM "catalog"."silver"."sales" AT branch main AS s
LEFT JOIN "catalog"."silver"."customers" AT branch main AS c ON c.id = s.customer_id
LEFT JOIN "catalog"."silver"."vehicles" AT branch main AS v ON v.id = s.vehicle_id