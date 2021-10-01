python3 -m venv .venv
source .venv/bin/activate
python modelling/train.py

uvicorn app.main:app --reload