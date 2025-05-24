.phony: all clean lint format test test_coverage

test:
	@echo "Make: Running tests..."
	python -m pytest $(FOLDER)

test.coverage:
	@echo "Make: Running tests with coverage..."
	@echo ${FOLDER}
	python -m pytest --cov=src --cov-report=term-missing --cov-branch --cov-report=html --cov-config=.coveragerc $(FOLDER)

test.activity.1:
	@echo "Make: Running activity tests..."
	@make test.coverage FOLDER=src/activity_1/
test.activity.2:
	@echo "Make: Running activity tests..."
	@make test.coverage FOLDER=src/activity_2/
test.activity.3:
	@echo "Make: Running activity tests..."
	@make test.coverage FOLDER=src/activity_3/
test.activity.4:
	@echo "Make: Running activity tests..."
	@make test.coverage FOLDER=src/activity_4/
test.activity.5:
	@echo "Make: Running activity tests..."
	@make test.coverage FOLDER=src/activity_5/
