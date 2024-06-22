from fastapi import FastAPI

from pilar.routers import root, sort, vowel_count

app = FastAPI(title="PilarAPI")

app.include_router(vowel_count.router)
app.include_router(sort.router)
app.include_router(root.router)
