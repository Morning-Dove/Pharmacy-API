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

@app.put("/patients/{fname}")
async def update_patient(first_name: str, updated_patient: Patient) -> Patient:
    for i, patient in enumerate(patients):
        if first_name ==  patient.first_name:
            patient[i] = updated_patient
            return updated_patient
        raise KeyError("Patient not found")

@app.delete("/patients/{first_name}")
async def delete_patient(first_name: str) -> str:
    for i, patient in enumerate(patients):
        if first_name == patient.first_name:
            patients.pop(i)
            return "Patient deleted"
        raise KeyError("Patient not found")

