
  
    

  create table "catalog"."silver"."product_reviews"
   
  
  
  
  

  

  as (
    

WITH formatted_reviews AS (
    SELECT
        CustomerID,
        CAST("Date" as DATE) as ReviewDate,
        Rating,
        ReviewID,
        TRIM(ReviewText) as ReviewText, -- Removes leading and trailing spaces
        VehicleModel
    FROM "catalog"."bronze"."ecoride"."product_reviews"
)

SELECT
    CustomerID,
    ReviewDate,
    Rating,
    ReviewID,
    ReviewText,
    VehicleModel
FROM formatted_reviews
  )
  