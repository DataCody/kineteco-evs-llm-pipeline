

SELECT
    id,
    first_name,
    -- Assuming email is important and retained
    email,
    city,
    "state",
    country
FROM "catalog"."bronze"."ecoride"."customers"