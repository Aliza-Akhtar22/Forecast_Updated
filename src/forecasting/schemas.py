from pydantic import BaseModel
from typing import List

class ForecastRequest(BaseModel):
    model_type: str  # "prophet", "random_forest", or "xgboost"
    table_name: str
    period: int
    ds_column: str
    y_column: str
    regressors: List[str]
    growth_rates: List[float]

class EvaluationRequest(BaseModel):
    table_name: str
    period: int
    ds_column: str
    y_column: str
    regressors: List[str]
    growth_rates: List[float]
