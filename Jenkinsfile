pipeline {
  agent any
  triggers { pollSCM('H/2 * * * *') }   // check Git every 2 minutes

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'YOUR_GITHUB_URL'
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        bat '''
        REM point Docker CLI to Minikube’s Docker daemon
        call minikube docker-env --shell=cmd > docker_env.bat
        call docker_env.bat

        REM build image inside Minikube
        docker build -t mydjangoapp:latest .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat '''
        kubectl apply -f deployment.yaml
        kubectl rollout status deployment/django-deployment
        kubectl apply -f service.yaml
        '''
      }
    }
  }
}
