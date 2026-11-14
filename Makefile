# VENV: virtual environment path (default: .venv)
VENV ?= .venv
# PYTHON: interpreter used by the targets (default: $(VENV)/bin/python)
PYTHON ?= $(VENV)/bin/python
# EXAMPLES: example scripts executed by `make run`
EXAMPLES := $(sort $(wildcard examples/*.py))
# MASPY: MASPY requirement to install. Defaults to the published package.
#   Local:       MASPY="-e ../MASPY"
MASPY ?= maspy-ml

.PHONY: setup install-maspy run run-tellhow run-untellhow help

setup: $(PYTHON) ## Create the venv and install the project dependencies
	uv pip install --python $(PYTHON) --reinstall-package maspy-ml -e .

$(PYTHON):
	uv venv $(VENV) --python 3.12

install-maspy: $(PYTHON) ## Install/replace MASPY (default: published; override with MASPY=...)
	uv pip install --python $(PYTHON) --reinstall-package maspy-ml $(MASPY)

run: ## Run all examples
	@set -e; for example in $(EXAMPLES); do \
		echo "Running $$example"; \
		$(PYTHON) "$$example"; \
	done

run-tellhow: ## Run the tellHow example
	$(PYTHON) examples/tellhow.py

run-untellhow: ## Run the untellHow example
	$(PYTHON) examples/untellhow.py

help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_.-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
