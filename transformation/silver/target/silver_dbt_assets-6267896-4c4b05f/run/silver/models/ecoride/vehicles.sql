
  
    

  create table "catalog"."silver"."vehicles"
   
  
  
  
  

  

  as (
    

SELECT
    id,
    model_name,
    model_type,
    color,
    "year"
FROM "catalog"."bronze"."ecoride"."vehicles"
  )
  