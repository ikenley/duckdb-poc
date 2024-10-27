.PHONY: run clean

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	touch $(VENV)/bin/activate

venv: clean
	@echo "Creating a new virtual environment..."
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	touch $(VENV)/bin/activate
	@echo "Virtual environment rejuvenated."

run: $(VENV)/bin/activate
	$(PYTHON) -m duckdb_poc.main

clean:
	rm -rf __pycache__
	rm -rf $(VENV)