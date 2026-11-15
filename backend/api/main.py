"""S2PiP integrated modular-monolith API scaffold.

No customer operations are exposed until authentication, authorization, tenant
isolation, persistence and audit middleware are implemented and tested.
"""
from fastapi import FastAPI
from backend.modules.pg.router import router as pg_router
from backend.modules.pi.router import router as pi_router

app = FastAPI(
    title="S2PiP API",
    version="0.3.2",
    description="Integrated PG + PI API scaffold with extraction-ready module boundaries.",
)


@app.get("/health", tags=["Platform"])
def platform_health() -> dict:
    return {"platform": "s2pip", "status": "scaffold_ready", "version": "0.3.2"}


@app.get("/api/v1/platform/modules", tags=["Platform"])
def modules() -> dict:
    return {"deployment_mode": "integrated", "modules": ["pg", "pi"]}


app.include_router(pg_router)
app.include_router(pi_router)
