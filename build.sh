source .venv/bin/activate
pip install --upgrade pip 
pip install -r requirements.txt
rm -rf public 
reflex init 
API_URL=https://newlife-production.up.railway.app reflex export --frontend-only
unzip frontend.zip -d public 
rm -f frontend.zip
desactivate