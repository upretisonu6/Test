pipeline {
    agent any

    environment {
        IMAGE_NAME = 'your-dockerhub-username/nginx'
        IMAGE_TAG = 'latest'
        REGISTRY_CREDENTIALS_ID = 'dockerhub-credentials' 
        KUBECONFIG_CREDENTIALS_ID = 'kubeconfig-secret' # kubeconfig
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build /path of docker file  -t $IMAGE_NAME:$IMAGE_TAG .' # the code and docker file in same dir
                }
            }
        }

        

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: env.REGISTRY_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME:$IMAGE_TAG
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: env.KUBECONFIG_CREDENTIALS_ID, variable: 'KUBECONFIG')]) {
                    sh """
                        export KUBECONFIG=$KUBECONFIG
                        kubectl set image statefulset/nginx-statefulset nginx=$IMAGE_NAME:$IMAGE_TAG --namespace=default
                        kubectl rollout status statefulset/nginx-statefulset --namespace=default
                    """
                }
            }
        }
    }

    post {
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
    }
}
