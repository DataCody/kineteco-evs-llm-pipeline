

  create or replace view "lakehouse"."gold"."customer_lifetime_value"
  
  as 

SELECT
    c.id as customer_id,
    c.first_name,
    c.email,
    SUM(s.sale_price) as total_spent,
    COUNT(s.id) as total_transactions,
    AVG(s.sale_price) as average_transaction_value
FROM "catalog"."silver"."customers" AT branch main c
LEFT JOIN "catalog"."silver"."sales" AT branch main s ON c.id = s.customer_id
GROUP BY c.id, c.first_name, c.email