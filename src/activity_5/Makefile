TARGET_DIR := target
JAR_NAME := eadproject-1.0-SNAPSHOT.war

.PHONY: build run test

build:
	@mvn clean install
	@mvn package

run:
	@mvn tomcat7:run

test:
	@mvn test
