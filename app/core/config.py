from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.example",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Postgres
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379

    # MinIO / S3
    minio_root_user: str
    minio_root_password: str
    minio_host: str = "localhost"
    minio_port: int = 9000
    minio_bucket_name: str = "gaayo"

    #Auth
    secret_key: str
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 7

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
    
    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}"
    
    @property
    def minio_url(self) -> str:
        return f"http://{self.minio_host}:{self.minio_port}"
    
settings = Settings()