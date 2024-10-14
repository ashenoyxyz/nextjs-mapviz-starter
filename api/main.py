from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import sample

import uvicorn

app = FastAPI()

origins = [
    "http://localhost:3000",  # Frontend running on localhost:3000 (Next.js)
    "http://localhost:8000",  # Backend running on localhost:8000
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow credentials (cookies, headers, etc.)
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers (Authorization, Content-Type, etc.)
)

cities = [
    {"description": "New York, NY", "lat": 40.7128, "lng": -74.0060},
    {"description": "Los Angeles, CA", "lat": 34.0522, "lng": -118.2437},
    {"description": "Chicago, IL", "lat": 41.8781, "lng": -87.6298},
    {"description": "Houston, TX", "lat": 29.7604, "lng": -95.3698},
    {"description": "Phoenix, AZ", "lat": 33.4484, "lng": -112.0740},
    {"description": "Philadelphia, PA", "lat": 39.9526, "lng": -75.1652},
    {"description": "San Antonio, TX", "lat": 29.4241, "lng": -98.4936},
    {"description": "San Diego, CA", "lat": 32.7157, "lng": -117.1611},
    {"description": "Dallas, TX", "lat": 32.7942, "lng": -96.7669},
    {"description": "San Jose, CA", "lat": 37.3382, "lng": -121.8863},
    {"description": "Austin, TX", "lat": 30.2672, "lng": -97.7431},
    {"description": "Fort Worth, TX", "lat": 32.7357, "lng": -97.3356},
    {"description": "Jacksonville, FL", "lat": 30.3321, "lng": -81.6557},
    {"description": "Columbus, OH", "lat": 39.9612, "lng": -83.0007},
    {"description": "Indianapolis, IN", "lat": 39.7684, "lng": -86.1581},
    {"description": "Memphis, TN", "lat": 35.1495, "lng": -90.0489},
    {"description": "Baltimore, MD", "lat": 39.2904, "lng": -76.6105},
    {"description": "Detroit, MI", "lat": 42.3314, "lng": -83.0469},
    {"description": "El Paso, TX", "lat": 31.7778, "lng": -106.4478},
    {"description": "Seattle, WA", "lat": 47.6062, "lng": -122.3321},
    {"description": "Boston, MA", "lat": 42.3601, "lng": -71.0589},
    {"description": "Washington, DC", "lat": 38.8951, "lng": -77.0364},
    {"description": "Nashville, TN", "lat": 36.1627, "lng": -86.7816},
    {"description": "Oklahoma City, OK", "lat": 35.4822, "lng": -97.5349},
    {"description": "Las Vegas, NV", "lat": 36.1699, "lng": -115.1403},
    {"description": "Portland, OR", "lat": 45.5051, "lng": -122.6777},
    {"description": "Louisville, KY", "lat": 38.2527, "lng": -85.7585},
    {"description": "Charlotte, NC", "lat": 35.2271, "lng": -80.8431},
    {"description": "Milwaukee, WI", "lat": 43.0389, "lng": -87.9065},
    {"description": "Albuquerque, NM", "lat": 35.0842, "lng": -106.6475},
    {"description": "Tucson, AZ", "lat": 32.2217, "lng": -110.9757},
    {"description": "Fresno, CA", "lat": 36.7500, "lng": -119.7667},
    {"description": "Sacramento, CA", "lat": 38.5816, "lng": -121.4944},
    {"description": "Kansas City, MO", "lat": 39.0983, "lng": -94.5777},
    {"description": "Raleigh, NC", "lat": 35.7775, "lng": -78.6382},
    {"description": "Long Beach, CA", "lat": 33.7700, "lng": -118.1938},
    {"description": "Omaha, NE", "lat": 41.2586, "lng": -95.9375},
    {"description": "Minneapolis, MN", "lat": 44.9778, "lng": -93.2650},
    {"description": "Miami, FL", "lat": 25.7617, "lng": -80.1918},
    {"description": "St. Louis, MO", "lat": 38.6270, "lng": -90.1994},
    {"description": "Cincinnati, OH", "lat": 39.1001, "lng": -84.5175},
    {"description": "Atlanta, GA", "lat": 33.7490, "lng": -84.3879},
    {"description": "Riverside, CA", "lat": 33.9081, "lng": -117.3949},
    {"description": "Tampa, FL", "lat": 27.9506, "lng": -82.4583},
    {"description": "Oakland, CA", "lat": 37.8044, "lng": -122.2710},
    {"description": "Cleveland, OH", "lat": 41.4784, "lng": -81.6864},
    {"description": "Tucson, AZ", "lat": 32.2217, "lng": -110.9757},
]

@app.get("/")
async def root():
    return {"message": "Mapviz template"}

@app.get("/points")
async def get_points():
    samples = sample(cities, 10)
    return samples

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
