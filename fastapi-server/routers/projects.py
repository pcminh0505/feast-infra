from config import config
from fastapi import APIRouter, Response
from feast import FeatureStore, RepoConfig
from feast.repo_config import RegistryConfig


router = APIRouter(
    prefix="/projects",
    tags=["projects"],
)


@router.get("/registry")
def get_registry_data(id: str):
    repo_config = RepoConfig(
        registry=RegistryConfig(
            registry_type="sql", path=f"postgresql://{config.db_username}:{config.db_password}@{config.db_host}:{config.db_port}/{id}", cache_ttl_seconds=60),
        project=id,
    )

    store = FeatureStore(config=repo_config)
    registry_proto = store.registry.proto()
    return Response(
        content=registry_proto.SerializeToString(),
        media_type="application/octet-stream",
    )