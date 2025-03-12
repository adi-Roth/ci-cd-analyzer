# Jenkins Shared Library

This repository is a **Jenkins Shared Library** designed to manage and streamline DevOps pipelines, automate CI/CD processes, and handle various development tasks such as testing, publishing, and monitoring.

## 📁 Repository Structure

### `HowTo/`  
This folder contains documentation and example files to help users understand and implement various Jenkins pipeline configurations.

- **CreateNewClass.md** - Guide for creating a new class in the shared library.
- **JenkinsfileForExample/** - Example Jenkinsfiles:
  - `CI_for_BaseImage.groovy` - Pipeline for deploying base Docker images.
  - `CI_for_Docker.example.groovy` - Example pipeline for Docker CI.

### `jobs/`  
Contains Jenkinsfiles used for managing DevOps pipelines (excluding CI/CD).

- **Job_CI_Maker.groovy** - Generates Jenkins jobs for CI.
- **rmsc.groovy** - Custom job configuration.
- **testAdi** - Placeholder for additional Jenkins jobs.

### `resources/lib/class/`  
Library files, YAML configurations, and Docker Compose files for various services.

- **`apitests/`** - Docker Compose files for API testing environments:
  - `docker-compose.apitests.yaml` - Runs API tests.
  - `docker-compose.kafka.yaml` - Runs Kafka and ZooKeeper (1 replica).
  - `docker-compose.mongo.yaml` - Runs a simple MongoDB instance.

- **`JenkinsAPI/`** - Configuration files for generating Jenkins jobs and pipelines:
  - `apitests_env_Docker.json` - API test environment config for Docker CI.
  - `apitests_env_NPM.json` - API test environment config for NPM CI.
  - `config-Docker.xml` - Job configuration for Docker CI pipelines.
  - `config-NPM.xml` - Job configuration for NPM CI pipelines.
  - `docker-compose.integration.Docker.yaml` - Integration service+mock for Docker CI.
  - `docker-compose.integration.NPM.yaml` - Integration service+mock for NPM CI.
  - `jenkinsfile-Docker.groovy` - Jenkinsfile for Docker CI pipelines.
  - `jenkinsfile-NPM.groovy` - Jenkinsfile for NPM CI pipelines.

- **`unitests/`** - Unit test-related resources:
  - `angularDockerfile` - Dockerfile for running Angular unit tests with Chrome Headless.

### `src/lib/Class/`  
Contains Groovy classes for various CI/CD utilities and functions.

- **Apitests.groovy** - Functions for API test stages.
- **DockerTools.groovy** - Utility functions for Docker management.
- **ErrorHandler.groovy** - Error handling class.
- **GitBash.groovy** - Functions for Git commands execution.
- **Lint.groovy** - Linting stage functions.
- **Logging.groovy** - Logging utility functions.
- **NpmPublish.groovy** - Functions for publishing NPM packages.
- **NpmTools.groovy** - NPM utilities.
- **ReportHandler.groovy** - Functions for generating reports.
- **Sonar.groovy** - SonarQube analysis functions.
- **TestTool.groovy** - Utility functions for testing.
- **Tool.groovy** - General utility functions.
- **Unitests.groovy** - Functions for unit test stages.
- **Xray.groovy** - Functions related to Xray security scanning.

#### `src/lib/mongo/`  
Handles MongoDB document processing and operations.

- **BuildDoc.groovy** - Class for building MongoDB documents.
- **MongoHandler.groovy** - MongoDB command handler.
- **ProductDoc.groovy** - Class for handling product documents.
- **Validatable.groovy** - Interface for `isValid()` function in document classes.

### `vars/`  
Global Groovy scripts and pipeline definitions.

- **CI_for_BaseImage.groovy** - Pipeline for deploying base Docker images.
- **CI_for_Docker.groovy** - Pipeline for deploying Docker images (for clients).
- **CI_for_npm.groovy** - Pipeline for deploying NPM packages.
- **Generate_for_ProductDocs.groovy** - Cron job pipeline for extracting product data and importing it into MongoDB.
- **Generate_Job.groovy** - Generates jobs based on `CI_for_<something>` and pushes the template files to relevant repositories.
- **global.groovy** - Global variables for the shared library.
- **stage_cloneWorkspace.groovy** - Function for cloning a workspace in a pipeline stage.
- **stage_publishMongoDoc.groovy** - Function for publishing a document to MongoDB.
- **stage_sonarScan.groovy** - Function for executing a SonarQube scan.

## 📖 Usage

1. **Import the shared library in your Jenkins pipeline:**
   ```groovy
   @Library('your-shared-library-name') _
   ```

2. **Use predefined functions and stages in your Jenkinsfile.**

3. **Modify and extend the library as needed for your pipeline needs.**

## 📌 Contribution

Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a feature branch.
- Commit your changes.
- Open a pull request.

## 🛠️ License

This shared library is provided under an open-source license. See `LICENSE` for details.

---

🚀 **Optimizing Jenkins pipelines for DevOps teams!** 🚀
