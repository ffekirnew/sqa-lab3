.phony: all clean lint format test test_coverage

test:
	@echo "Make: Running tests..."
	python -m pytest $(FOLDER)

test.coverage:
	@echo "Make: Running tests with coverage..."
	@echo ${FOLDER}
	python -m pytest --cov=src --cov-report=term-missing --cov-branch --cov-report=html --cov-config=.coveragerc $(FOLDER)
