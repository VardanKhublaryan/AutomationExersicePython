pipeline {
    agent any

    environment {
        // Define the path to Python (update this to your Python installation path)
        PYTHON = "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        VENV_DIR = "${WORKSPACE}\\venv"
    }

    stages {
//         stage('Checkout') {
//             steps {
//                 echo 'Checking out the code...'
//                 git 'https://github.com/VardanKhublaryan/AutomationExersice/'
//             }
//         }
//
//         stage('Set Up Virtual Environment') {
//             steps {
//                 echo 'Setting up a Python virtual environment...'
//                 bat """
//                     "${PYTHON}" -m venv "${VENV_DIR}"
//                     call "${VENV_DIR}\\Scripts\\activate"
//                     python -m pip install --upgrade pip
//                 """
//             }
//         }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat """
                    call "${VENV_DIR}\\Scripts\\activate"
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat """
                    call "${VENV_DIR}\\Scripts\\activate"
                    pytest --junitxml=test-results.xml --html=report.html
                """
            }
        }

        stage('Publish Test Results') {
            steps {
                echo 'Publishing test results...'
                junit 'test-results.xml'
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'HTML Test Report'
                ])
            }
        }
    }

    post {
//         always {
//             echo 'Cleaning up...'
//             bat "rmdir /s /q ${VENV_DIR}"  // Clean up the virtual environment
//         }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}