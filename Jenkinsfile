pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'durgarao365/student-course-management'
        DOCKER_CREDENTIALS_ID = 'dockerhub'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git credentialsId: 'c7c69042-6a15-4b94-aee6-681cb44007d3', url: 'https://github.com/Durgarao-gunja365/student-course-management.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', dockerhub) {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    sh 'docker rm -f student-course-app || true'
                    sh 'docker run -d --name student-course-app -p 8000:8000 $DOCKER_IMAGE'
                }
            }
        }
    }
}
