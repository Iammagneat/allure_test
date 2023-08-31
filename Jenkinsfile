pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from the repository
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                // Install Python dependencies from requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Activate virtual environment if needed
                sh 'source venv/bin/activate && pytest'
            }
        }
    }
}
