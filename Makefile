all: run

run:
	python src/gen.py

adder:
	python src/adder.py

setup: src/requirements.txt
	pip install -r src/requirements.txt

clean:
	@ rm -rf output/testes/*.pdf 
	@ rm -rf output/resolucoes/*.pdf 

.phony: run clean setup