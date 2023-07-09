pipeline {
  agent {
    node {
      label 'laptop'
    }
  }
  triggers {
    pollSCM 'H/30 * * * *'
  }
  options{
    buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    timestamps()
  }
  environment {
    registry = 'amsiman/devopsproject'
    DOCKER_CERT_PATH = credentials('docker-token') // Make sure to have DockerHub credentials available in the Jenkins Server Credentials Manager
    DOCKER_CREDS = credentials('docker-token')
    dockerImage = ''
  }
  stages {
    stage('pull repo') {
      steps {
        git branch: 'jenking-pipeline', url: 'https://github.com/Ax-Projects/DevOpsExperts.git'
      }
    }
    stage('set-docker-imagetag') {
      steps {
        bat(script: "(echo. & echo IMAGE_TAG=${BUILD_NUMBER}) >> .env", returnStdout: true, returnStatus: true)
      }
    }
    stage('create-venv') {
      steps {
        powershell(script: 'python -m venv .venv', returnStdout: true, returnStatus: true)
      }
    }
    stage('start-db') {
      steps {
        powershell(script: 'docker-compose up -d mysql', returnStdout: true, returnStatus: true)
        // waiting a bit for sql to be available
        powershell 'sleep 10'
      }
    }
    stage('start-backend') {
      steps {
        bat(script: '.venv\\Scripts\\Activate.bat', returnStatus: true, returnStdout: true)
        bat(script: 'pip install -r requirements.txt', returnStatus: true, returnStdout: true)
        bat(script: 'start /min python rest_api.py', returnStatus: true, returnStdout: true)
      }
    }

    stage('init-DB') {
      steps {
        bat(script: 'python clean_db.py', returnStatus: true, returnStdout: true)
      }
    }

    stage('run-backend-test') {
      steps {
        bat 'python backend_testing.py'
      }
    }
    stage('stop-db') {
      steps {
        powershell(script: 'docker-compose down 2>$nul', returnStdout: true, returnStatus: true)
      }
    }
    stage('stop-restapi') {
      steps {
        bat 'python clean_environment.py'
      }
    }

    stage('docker login') {
      steps {
        bat "docker login -u $DOCKER_CREDS_USR -p $DOCKER_CREDS_PSW"
      }
    }

    stage('docker build') {
      steps {
        script {
          dockerImage = docker.build( registry + ":$BUILD_NUMBER")
        }
      }
    }
    
    stage('start-docker-compose'){
      steps {
        bat 'docker-compose up -d'
        powershell 'sleep 20'
      }
    }

    stage('init-setup-docker-DB') {
      steps {
        bat(script: 'python clean_db.py', returnStatus: true, returnStdout: true)
      }
    }

    stage('run-docker-test') {
      steps {
        bat 'python docker_backend_testing.py'
      }
    }

    stage('stop-servers') {
      steps {
        bat 'docker-compose stop restapi'
        bat 'docker-compose down'
      }
    }
    stage('docker push') {
      steps {
        script {
          dockerImage.push() // push image to hub
        }
      }
      post {
        always {
          bat "docker logout" // loging out of docker user for security reasons
          bat "docker rmi $registry:$BUILD_NUMBER" // delete the local image at the end
          powershell 'Remove-Item -Recurse -Force .venv' // removing python venv files
        }
      }
    }
  }
}