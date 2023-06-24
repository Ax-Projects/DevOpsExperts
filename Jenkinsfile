pipeline {
  agent {
    node {
      label 'laptop'
    }
  }
  environment {
    registry = 'amsiman/devopsproject'
    registryCredential = 'dockerhub-login'
    dockerimage = ''
  }
  stages {
    // add stage to start mysql container
    stage('pull repo') {
      steps {
        git branch: 'jenking-pipeline', url: 'https://github.com/Ax-Projects/DevOpsExperts.git'
      }
    }
    stage('start-db') {
      steps {
        powershell(script: 'docker-compose up -d mysql', returnStdout: true, returnStatus: true)
      }
    }
    stage('start-backend') {
      steps {
        powershell(script: 'python rest_api.py', returnStdout: true, returnStatus: true)
      }
    }

    stage('clean-DB') {
      steps {
        bat(script: 'start /min python clean_db.py', returnStatus: true, returnStdout: true)
      }
    }

    stage('run-backend-test') {
      steps {
        bat 'python backend_testing.py'
      }
    }

    stage('stop-restapi') {
      steps {
        bat 'python clean_environment.py'
      }
    }
    stage('build and push image') {
      steps {
        script {
          dockerImage = docker.build("$registry:$BUILD_NUMBER")
          docker.withRegistry('', registryCredential) {
            dockerImage.push() // push image to hub
            }
          }
        }
      post {
        always {
          bat "docker rmi $registry:$BUILD_NUMBER" // delete the local image at the end
        }
      }
    }
    stage('start-docker-compose'){
      steps {
        bat 'docker-compose up -d'
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
  }
}