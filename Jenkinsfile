pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'durgarao365/student-course-management'

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
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                    sh 'docker push $DOCKER_IMAGE'
                    sh 'docker logout'
                }
            }
        }


        stage('Deploy Container') {
            steps {
                script {
                    sh 'docker-compose down || true'
            sh 'docker-compose up -d --build'
                }
            }
        }
    }
}
