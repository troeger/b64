all: osxbin

osxbin: venv
#	pyinstaller --windowed --onefile --paths ./venv/lib/python3.11/site-packages b64.py
	venv/bin/pyinstaller b64.spec

venv:
	test -d venv || python3 -m venv venv
	venv/bin/pip install -r requirements.txt
