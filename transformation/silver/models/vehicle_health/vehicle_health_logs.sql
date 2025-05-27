{{ config( twin_strategy="allow", materialized="table" ) }}

SELECT
    VehicleID,
    Model,
    ManufacturingYear,
    Alerts,
    MaintenanceHistory
FROM {{ source("vehicle_health_bronze", "logs") }}
