# AI Website Builder

## Local backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Set OPENAI_API_KEY, then:
uvicorn main:app --reload

## Frontend
Open frontend/index.html.

If the backend is deployed, set its URL in the browser console:
localStorage.setItem("API_BASE","https://YOUR-RENDER-URL")
Then refresh.

## Render
Deploy this repository using render.yaml and add OPENAI_API_KEY as a secret.
