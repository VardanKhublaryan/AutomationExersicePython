pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        VENV_DIR = "${WORKSPACE}\\venv"
        ALLURE_RESULTS_DIR = "${WORKSPACE}\\allure-results"
        ALLURE_REPORT_DIR = "${WORKSPACE}\\allure-report"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git 'https://github.com/VardanKhublaryan/AutomationExersice/'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                echo 'Setting up a Python virtual environment...'
                bat """
                    "${PYTHON}" -m venv "${VENV_DIR}"
                    call "${VENV_DIR}\\Scripts\\activate"
                    python -m pip install --upgrade pip
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat """
                    call "${VENV_DIR}\\Scripts\\activate"
                    pip install -r requirements.txt
                    pip install allure-pytest
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with Allure...'
                bat """
                    call "${VENV_DIR}\\Scripts\\activate"
                    pytest --junitxml=test-results.xml --alluredir="${ALLURE_RESULTS_DIR}" --html=report.html
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo 'Generating Allure report...'
                bat """
                    allure generate "${ALLURE_RESULTS_DIR}" --clean -o "${ALLURE_REPORT_DIR}"
                """
            }
        }

        stage('Publish Test Results') {
            steps {
                echo 'Publishing test results and reports...'
                junit 'test-results.xml'
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'HTML Test Report'
                ])
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${ALLURE_REPORT_DIR}",
                    reportFiles: 'index.html',
                    reportName: 'Allure Report',
                    reportTitles: 'Allure Report'
                ])
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat "rmdir /s /q ${VENV_DIR}"  // Clean up the virtual environment
            bat "rmdir /s /q ${ALLURE_RESULTS_DIR}"
            bat "rmdir /s /q ${ALLURE_REPORT_DIR}"
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
