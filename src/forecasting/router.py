from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .schemas import ForecastRequest, EvaluationRequest
from ..shared.dependencies import get_db
from .service import run_forecast, evaluate_models

router = APIRouter()

@router.post("/forecast")
def forecast_endpoint(req: ForecastRequest, db: Session = Depends(get_db)):
    try:
        result_df = run_forecast(
            db=db,
            model_type=req.model_type,
            table_name=req.table_name.lower(),
            ds_col=req.ds_column,
            y_col=req.y_column,
            regressor_cols=req.regressors,
            growth_rates=req.growth_rates,
            period=req.period
        )
        result_df["ds"] = result_df["ds"].astype(str)
        return {"forecast": result_df.to_dict(orient="records")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/forecast/evaluate")
def evaluate_forecast_models(req: EvaluationRequest, db: Session = Depends(get_db)):
    try:
        evaluation_result = evaluate_models(
            db=db,
            table_name=req.table_name.lower(),
            ds_col=req.ds_column,
            y_col=req.y_column,
            regressor_cols=req.regressors,
            growth_rates=req.growth_rates,
            period=req.period
        )
        return evaluation_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
