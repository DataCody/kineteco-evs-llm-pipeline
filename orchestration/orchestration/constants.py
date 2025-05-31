import os
from pathlib import Path

from dagster_dbt import DbtCliResource

dbt_silver_project_dir = Path(__file__).joinpath("..", "..", "..", "transformation", "silver").resolve()
dbt_gold_project_dir = Path(__file__).joinpath("..", "..", "..", "transformation", "gold").resolve()
dbt_silver = DbtCliResource(project_dir=os.fspath(dbt_silver_project_dir))
dbt_gold = DbtCliResource(project_dir=os.fspath(dbt_gold_project_dir))

# If DAGSTER_DBT_PARSE_PROJECT_ON_LOAD is set, a manifest will be created at run time.
# Otherwise, we expect a manifest to be present in the project's target directory.
if os.getenv("DAGSTER_DBT_PARSE_PROJECT_ON_LOAD"):
    dbt_silver_manifest_path = (
        dbt_silver.cli(
            ["--quiet", "parse"],
            target_path=Path("target"),
        )
        .wait()
        .target_path.joinpath("manifest.json")
    )
    dbt_gold_manifest_path = (
        dbt_gold.cli(
            ["--quiet", "parse"],
            target_path=Path("target"),
        )
        .wait()
        .target_path.joinpath("manifest.json")
    )
else:
    dbt_silver_manifest_path = dbt_silver_project_dir.joinpath("target", "manifest.json")
    dbt_gold_manifest_path = dbt_gold_project_dir.joinpath("target", "manifest.json")