from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets
from .constants import dbt_silver, dbt_gold
from .constants import dbt_silver_manifest_path, dbt_gold_manifest_path

@dbt_assets(manifest=dbt_silver_manifest_path)
def silver_dbt_assets(context: AssetExecutionContext):
    yield from dbt_silver.cli(["run"], context=context).stream()

@dbt_assets(manifest=dbt_gold_manifest_path)
def gold_dbt_assets(context: AssetExecutionContext):
    yield from dbt_gold.cli(["run"], context=context).stream()