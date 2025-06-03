import os
from superset.app import create_app

# 从环境变量读取 Dremio 连接参数
dremio_user = os.environ["DREMIO_USER"]
dremio_pass = os.environ["DREMIO_PASSWORD"]
dremio_host = os.environ.get("DREMIO_HOST", "dremio")
dremio_port = os.environ.get("DREMIO_PORT", "32010")

sqlalchemy_uri = f"dremio+flight://{dremio_user}:{dremio_pass}@{dremio_host}:{dremio_port}/"

app = create_app()
with app.app_context():
    from superset import db
    from superset.models.core import Database

    # 检查是否已存在
    existing = db.session.query(Database).filter_by(database_name='dremio_local').first()

    if not existing:
        dremio = Database(
            database_name="dremio_local",
            sqlalchemy_uri=f"dremio+flight://{os.getenv('DREMIO_USER')}:{os.getenv('DREMIO_PASSWORD')}@{os.getenv('DREMIO_HOST')}:{os.getenv('DREMIO_PORT')}/",
            extra='{"engine_params": {"connect_args": {"disable_certificate_verification": true}}}',
            expose_in_sqllab=True,
            allow_run_async=True,
        )
        db.session.add(dremio)
        db.session.commit()
        print("✅ Dremio 数据源注册成功")
    else:
        print("ℹ️ Dremio 数据源已存在，跳过注册")