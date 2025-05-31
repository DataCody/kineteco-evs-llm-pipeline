from dagster import Definitions
from .assets import silver_dbt_assets, gold_dbt_assets
from .constants import dbt_silver, dbt_gold
from .schedules import schedules

defs = Definitions(
    assets=[silver_dbt_assets, gold_dbt_assets],
    schedules=schedules,
    resources={
        "dbt_silver": dbt_silver,
        "dbt_gold": dbt_gold,
    },
)