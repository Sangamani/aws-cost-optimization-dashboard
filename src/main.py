from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.scanner import get_instances
from src.recommendations import generate_recommendations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message": "AI AWS Cost Detective Running"
    }

@app.get("/instances")
def instances():

    try:
        data = get_instances()
        return data

    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/recommendations")
def recommendations():

    try:

        instances = get_instances()

        results = []

        for instance in instances:

            recommendations = generate_recommendations(instance)

            results.append({
                "instance": instance,
                "recommendations": recommendations
            })

        return results

    except Exception as e:

        return {
            "error": str(e)
        }
        