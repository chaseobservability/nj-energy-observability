SHELL := /bin/bash

# Example:
#   make install
#   make run PERIOD=2026Q1 START=2026-01-01T00:00:00 END=2026-04-01T00:00:00
PERIOD ?= 2026Q1
START  ?= 2026-01-01T00:00:00
END    ?= 2026-04-01T00:00:00

.PHONY: venv install pull compute render run clean

venv:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -U pip

install: venv
	. .venv/bin/activate && pip install -r requirements.txt

pull:
	. .venv/bin/activate && python -m src.pull_dataminer --period $(PERIOD) --start $(START) --end $(END)
	. .venv/bin/activate && python -m src.pull_imm --period $(PERIOD) --start $(START) --end $(END)

compute:
	. .venv/bin/activate && python -m src.compute_zone_scorecard --period $(PERIOD)
	. .venv/bin/activate && python -m src.compute_statewide_rollup --period $(PERIOD)

render:
	. .venv/bin/activate && python -m src.render_onepager --period $(PERIOD)

run: pull compute render
	@echo "Done. Outputs in out/$(PERIOD)/"

clean:
	rm -rf out stage raw
