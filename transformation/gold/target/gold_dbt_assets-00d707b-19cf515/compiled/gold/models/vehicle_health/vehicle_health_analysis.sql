

SELECT
    VehicleID,
    Model,
    ManufacturingYear,
    Alerts,
    MaintenanceHistory
FROM "catalog"."silver"."vehicle_health_logs" AT branch main