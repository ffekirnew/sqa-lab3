FROM openjdk:17-jdk-slim

WORKDIR /app

RUN apt-get update && \
  apt-get install -y maven && \
  rm -rf /var/lib/apt/lists/*

RUN mkdir -p src/main/java/com/example
RUN mkdir -p src/test/java/com/example

COPY main/java/com/example/Calculator.java src/main/java/com/example/
COPY test/java/com/example/CalculatorTest.java src/test/java/com/example/

COPY pom.xml .

RUN mvn test

CMD ["tail", "-f", "/dev/null"]
