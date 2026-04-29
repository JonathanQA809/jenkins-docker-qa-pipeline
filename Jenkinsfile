
pipeline {
    agent any

    stages {
        stage('Build Test Image') {
            steps {
                sh 'docker build -t jenkins-docker-qa-pipeline .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm jenkins-docker-qa-pipeline'
            }
        }
    }
}
