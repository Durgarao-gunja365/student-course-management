pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'durgarao365/student-course-management'

         DJANGO_SUPERUSER_USERNAME = 'admin'
        DJANGO_SUPERUSER_EMAIL = 'admin@example.com'
        DJANGO_SUPERUSER_PASSWORD = 'admin123'

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
                   // Free up port 8000 if it's already in use
                    sh 'docker ps -q --filter "publish=8000" | xargs -r docker stop || true'
                    sh 'docker ps -aq --filter "publish=8000" | xargs -r docker rm || true'

                    // Take down old containers and start new ones
                    sh 'docker-compose down || true'
                    sh 'docker-compose up -d --build'
                }
            }
        }
          stage('Run Migrations') {
            steps {
                script {
                    // Run migration inside the web container
                    sh 'docker-compose exec web python manage.py migrate'
                }
            }
        }

        stage('Create Superuser') {
            steps {
                script {
                    // Export environment vars and create superuser
                    sh '''
                        docker-compose exec -e DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME} \
                                             -e DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL} \
                                             -e DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD} \
                            web python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists():
    User.objects.create_superuser('${DJANGO_SUPERUSER_USERNAME}', '${DJANGO_SUPERUSER_EMAIL}', '${DJANGO_SUPERUSER_PASSWORD}')"
                    '''
                }
            }
        }
    }
}
