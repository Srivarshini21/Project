from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Import routers (IMPORTANT: use src.routes)
from src.routes import user_routes
from src.routes import product_routes
from src.routes import order_routes
from src.database import init_db

app = FastAPI(title="Cloud Native Inventory System")

# -------------------------
# CORS (important for frontend)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Include Routers
# -------------------------
app.include_router(user_routes.router)
app.include_router(product_routes.router)
app.include_router(order_routes.router)


@app.on_event("startup")
def startup_event():
    init_db()

# -------------------------
# Health Check
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# -------------------------
# Static Frontend (if needed)
# -------------------------
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")