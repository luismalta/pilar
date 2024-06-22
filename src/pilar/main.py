from fastapi import FastAPI
from pilar.routers import vowel_count, sort


app = FastAPI(title="PilarAPI")

app.include_router(vowel_count.router)
app.include_router(sort.router)
