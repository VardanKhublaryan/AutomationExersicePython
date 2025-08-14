pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        VENV_DIR = "${WORKSPACE}\\venv"
        ALLURE_RESULTS_DIR = "${WORKSPACE}\\allure-results"
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
                echo 'Setting up Python virtual environment...'
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
                    pytest --junitxml=test-results.xml --alluredir="${ALLURE_RESULTS_DIR}"
                """
            }
        }

   stage('Publish Allure Report') {
    steps {
        echo 'Publishing Allure report in Jenkins...'
        allure([
            includeProperties: false,
            results: [[path: "${ALLURE_RESULTS_DIR}"]]
        ])
    }
}


        stage('Publish Test Results') {
            steps {
                echo 'Publishing JUnit test results...'
                junit 'test-results.xml'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up virtual environment...'
            bat "if exist ${VENV_DIR} rmdir /s /q ${VENV_DIR}"
            bat "if exist ${ALLURE_RESULTS_DIR} rmdir /s /q ${ALLURE_RESULTS_DIR}"
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
