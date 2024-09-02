from fastapi import FastAPI
from app.routers.user_router import router as user_router
from app.context import app_context

app = FastAPI()

# Include the router
app.include_router(user_router, prefix="/users", tags=["users"])

@app.on_event("startup")
async def startup_event():
    # Any startup logic, e.g., initializing resources
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Call shutdown to close resources
    app_context.shutdown()
