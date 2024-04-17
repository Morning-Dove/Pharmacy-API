from fastapi import FastAPI

import json
from models import Patient

app = FastAPI()

with open("patients.json", "r") as f:
    patient_list = json.load(f)

patients: list[Patient] = []

for patient in patient_list:
    patients.append(Patient(**patient))


@app.get("/patients/")
async def get_patient() -> list[Patient]:
    return patients

@app.post("/patients/")
async def create_patient(patient: Patient) -> None:
    patients.append(patient)

@app.put("/patients/{first_name}")
async def update_patient(first_name: str, updated_patient: Patient):
    for patient in range(len(patients)):
        if first_name in patients[patient].first_name:
            patients[patient] = updated_patient
            return updated_patient

@app.delete("/patients/{first_name}")
async def delete_patient(first_name: str) -> str:
    for patient in patients:
        if first_name in patient.first_name:
            patients.remove(patient)
            return "Patient deleted"

