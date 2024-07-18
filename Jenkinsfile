pipeline {
    agent none
    stages {
        stage('Build and Test Feature Branch') {
            when {
                branch 'feature/*'
            }
            agent {
                kubernetes {
                    label 'feature-agent'
                    defaultContainer 'jnlp'
                    yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    jenkins: feature-agent
spec:
  containers:
  - name: python
    image: shayshmaiser/piano-app:5.8
    command:
    - cat
    tty: true
  - name: mongodb
    image: mongo:latest
    command:
    - cat
    tty: true
  - name: docker
    image: docker:latest
    command:
    - cat
    tty: true
    volumeMounts:
    - name: docker-sock
      mountPath: /var/run/docker.sock
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
"""
                }
            }
            stages {
                stage('Checkout') {
                    steps {
                        checkout scm
                    }
                }
                stage('Build') {
                    steps {
                        script {
                            def dockerfilePath = './Dockerfile'
                            def image = docker.build("shayshmaiser/piano-app:${env.BRANCH_NAME}-${env.BUILD_NUMBER}", "-f ${dockerfilePath} .")
                            sh 'docker push shayshmaiser/piano-app:${env.BRANCH_NAME}-${env.BUILD_NUMBER}'
                        }
                    }
                }
                stage('Test') {
                    steps {
                        sh 'pytest tests'
                    }
                }
            }
            post {
                success {
                    script {
                        echo 'Feature branch passed tests, merging into main'
                        withCredentials([usernamePassword(credentialsId: 'github-credentials', usernameVariable: 'GITHUB_USER', passwordVariable: 'GITHUB_TOKEN')]) {
                            sh """
                                git config --global user.email "you@example.com" // Update with your email
                                git config --global user.name "Your Name" // Update with your name
                                git checkout main
                                git pull origin main
                                git merge --no-ff ${env.BRANCH_NAME}
                                git push https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/your-repo.git main // Update with your repo
                            """
                        }
                    }
                }
                failure {
                    error('Feature branch tests failed, stopping the pipeline.')
                }
            }
        }
        stage('Build and Test Main Branch') {
            when {
                branch 'main'
            }
            agent {
                kubernetes {
                    label 'main-agent'
                    defaultContainer 'jnlp'
                    yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    jenkins: main-agent
spec:
  containers:
  - name: python
    image: python:latest
    command:
    - cat
    tty: true
  - name: mongodb
    image: mongo:latest
    command:
    - cat
    tty: true
  - name: docker
    image: docker:latest
    command:
    - cat
    tty: true
    volumeMounts:
    - name: docker-sock
      mountPath: /var/run/docker.sock
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
"""
                }
            }
            stages {
                stage('Checkout') {
                    steps {
                        checkout scm
                    }
                }
                stage('Build') {
                    steps {
                        script {
                            def dockerfilePath = 'path/to/main/Dockerfile' // Update this path
                            def image = docker.build("your-dockerhub-username/your-app:${env.BUILD_NUMBER}", "-f ${dockerfilePath} .")
                            sh 'docker push your-dockerhub-username/your-app:${env.BUILD_NUMBER}'
                        }
                    }
                }
                stage('Test') {
                    steps {
                        sh 'pytest tests'
                    }
                }
            }
            post {
                success {
                    echo 'Main branch passed tests'
                }
                failure {
                    error('Main branch tests failed, stopping the pipeline.')
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}