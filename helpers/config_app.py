from fastapi import FastAPI
from helpers.health import health_router
from handlers.fetch_data import fetchdatarouter

all_routers = [health_router, fetchdatarouter]

def create_app() :
    app = FastAPI(title = "Share Market Automation Application")
    for router in all_routers :
        app.include_router(router)
    return app
