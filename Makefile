all: run

run:
	python3 src/gen.py

sync:
	python3 src/sync.py

setup: requirements.txt
	pip install -r requirements.txt
	python3 src/sync.py

clean:
	@ rm -rf output/testes/*.pdf 
	@ rm -rf output/resolucoes/*.pdf 
	@ rm -rf src/__pycache__

.phony: run clean setup