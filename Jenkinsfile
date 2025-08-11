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
                git branch: 'main', url: 'https://github.com/VardanKhublaryan/AutomationExersice/'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                echo 'Checking if virtual environment exists...'
                script {
                    if (!fileExists("${VENV_DIR}\\Scripts\\activate.bat")) {
                        echo 'Virtual environment not found, creating...'
                        bat """
                            "${PYTHON}" -m venv "${VENV_DIR}"
                            call "${VENV_DIR}\\Scripts\\activate"
                            python -m pip install --upgrade pip
                        """
                    } else {
                        echo 'Virtual environment already exists, skipping creation.'
                    }
                }
            }
        }

        stage('Install Dependencies If Needed') {
            steps {
                script {
                    echo 'Installing dependencies only if missing...'
                    bat """
                        call "${VENV_DIR}\\Scripts\\activate"
                        pip install --upgrade pip
                        pip install --upgrade --requirement requirements.txt --no-cache-dir
                        pip show allure-pytest >nul 2>&1 || pip install allure-pytest --no-cache-dir
                    """
                }
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

        stage('Publish Allure Report') {
            steps {
                echo 'Publishing Allure report in Jenkins...'
                allure includeProperties: false, jdk: '', results: [[path: "${ALLURE_RESULTS_DIR}"]]
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
                    reportName: 'Allure Report (Static HTML)',
                    reportTitles: 'Allure Report'
                ])
            }
        }
    }

    post {
        always {
            echo 'Cleaning up test results (keeping venv and dependencies)...'
            bat "if exist ${ALLURE_RESULTS_DIR} rmdir /s /q ${ALLURE_RESULTS_DIR}"
            bat "if exist ${ALLURE_REPORT_DIR} rmdir /s /q ${ALLURE_REPORT_DIR}"
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
