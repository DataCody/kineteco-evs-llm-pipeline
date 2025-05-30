

  create or replace view "lakehouse"."gold"."vehicle_health_analysis"
  
  as 

SELECT
    VehicleID,
    Model,
    ManufacturingYear,
    Alerts,
    MaintenanceHistory
FROM "catalog"."silver"."vehicle_health_logs" AT branch main