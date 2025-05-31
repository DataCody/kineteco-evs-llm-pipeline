
  
    

  create table "catalog"."silver"."vehicle_health_logs"
   
  
  
  
  

  

  as (
    

SELECT
    VehicleID,
    Model,
    ManufacturingYear,
    Alerts,
    MaintenanceHistory
FROM "catalog"."bronze"."vehicle_health"."logs"
  )
  