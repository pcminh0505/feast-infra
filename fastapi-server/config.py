from pydantic import BaseSettings


class Config(BaseSettings):
    db_host: str
    db_port: str
    db_username: str
    db_password: str

    host_url: str

    class Config:
        env_file = ".env"


config = Config()
