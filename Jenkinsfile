pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Jenkins automatically checks out the repo, this is optional
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh 'docker build -t flaskapp:latest .'
                }
            }
        }

        stage('Run with Docker Compose') {
            steps {
                script {
                    echo "Running container using Docker Compose..."
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
