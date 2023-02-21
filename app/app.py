from fastapi import FastAPI
from app.competition.competition_routes import competition_route
from app.entry.entry_routes import entry_route
from app.user.user_routes import user_route

app = FastAPI()

'''
It adds three routes to the application and allows requests to be sent to the application based on the route chosen.
'''

app.include_router(competition_route, tags=['Competition'])
app.include_router(entry_route, tags=['Entry'])
app.include_router(user_route, tags=['Users'])