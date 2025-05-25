.phony: all clean lint format test test.cover.directory

test:
	@echo "Make: Running tests..."
	python -m pytest $(DIRECTORY)

test.cover.directory:
	@echo "Make: Running tests with coverage..."
	@echo ${DIRECTORY}
	python -m pytest --cov=$(DIRECTORY) --cov-report=term-missing --cov-branch --cov-report=html --cov-config=.coveragerc $(DIRECTORY)

test.file:
	@echo "Make: Running tests with coverage..."
	@echo ${TARGET_FILE} ${TEST_FILE}
	python -m pytest --cov=$(TARGET_FILE) $(TEST_FILE)

test.cover.file:
	@echo "Make: Running tests with coverage..."
	@echo ${TARGET_FILE} ${TEST_FILE}
	python -m pytest --cov=$(TARGET_FILE) --cov-report=term-missing --cov-branch --cov-report=html $(TEST_FILE) --cov-fail-under=100 --ignore=/**/__init__.py

test.activity.1:
	@echo "Make: Running activity tests..."
	@make test.cover.directory DIRECTORY=src/activity_1

test.activity.2:
	@echo "Make: Running activity tests..."
	@make test.cover.directory DIRECTORY=src/activity_2

test.activity.3:
	@echo "Make: Running activity tests..."
	@make test.cover.directory DIRECTORY=src/activity_3
	
test.activity.4.original:
	@echo "Make: Running activity tests..."
	@make test.file TEST_FILE=src/activity_4 TARGET_FILE=src/activity_4/original

test.activity.4.mutant:
	@echo "Make: Running activity tests..."
	@echo ${MUTANT_NUMBER}
	@make test.file TARGET_FILE=src/activity_4/mutants

test.activity.5.build:
	@echo "Make: Running activity tests..."
	@docker build -t activity_5 src/activity_5

test.activity.5: test.activity.5.build
	@docker run -it activity_5
