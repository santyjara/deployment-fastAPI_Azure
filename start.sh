pip install -r modelling/requirements.txt
python modelling/train.py
pip install -r app/requirements.txt
uvicorn app.main:app --reload
