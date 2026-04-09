from typing import TypedDict


class PredictionResponse(TypedDict):
    case_id: str
    failure_probability: float
    root_cause_hint: str
