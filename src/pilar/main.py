from fastapi import FastAPI
from pilar.routers import vowel_count


app = FastAPI(title="PilarAPI")

app.include_router(vowel_count.router)
