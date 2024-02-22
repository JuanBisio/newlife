source .venv/bin/activate
pip install --upgrade pip 
pip install -r requirements.txt
rm -rf public 
reflex init 
reflex export --frontend-only
#API_URL=https://lethalsupplements-production.up.railway.app 
unzip frontend.zip -d public 
rm -f frontend.zip
desactivate