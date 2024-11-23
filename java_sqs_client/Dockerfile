# Stage 1: Build the application
FROM maven:3.8.8-eclipse-temurin-17 as builder
WORKDIR /app
COPY . .
RUN mvn clean package

# Stage 2: Create the runtime image
FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=builder /app/target/imagegenerator-0.0.1-SNAPSHOT.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
