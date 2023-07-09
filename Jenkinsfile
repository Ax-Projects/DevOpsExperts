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
    registryCredential = 'dockerhub-login' // Make sure to have DockerHub credentials available in the Jenkins Server Credentials Manager
    dockerimage = ''
  }
  stages {
    stage('pull repo') {
      steps {
        git branch: 'jenking-pipeline', url: 'https://github.com/Ax-Projects/DevOpsExperts.git'
      }
    }
    stage('set-docker-imagetag') {
      steps {
        // powershell(script: '"IMAGE_TAG=${BUILD_NUMBER}" | Add-Content -Path ./.env', returnStdout: true, returnStatus: true)
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
        // powershell(script: '.venv\\Scripts\\Activate.ps1', returnStdout: true, returnStatus: true)
        // powershell(script: 'pip install -r requirements.txt', returnStdout: true, returnStatus: true)
        // powershell(script: 'python rest_api.py', returnStdout: true, returnStatus: true)
        bat(script: 'start /min python rest_api.py', returnStatus: true, returnStdout: true)
      }
    }

    stage('clean-DB') {
      steps {
        bat(script: 'python clean_db.py', returnStatus: true, returnStdout: true)
      }
    }

    stage('run-backend-test') {
      steps {
        bat 'python backend_testing.py'
      }
    }
    stage('stop-DC-db') {
      steps {
        powershell(script: 'docker-compose down 2>$nul', returnStdout: true, returnStatus: true)
      }
    }
    stage('stop-restapi') {
      steps {
        bat 'python clean_environment.py'
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

    // stage('clean-DB-docker') {
    //   steps {
    //     script {
    //       dockerImage.inside {
    //         sh 'python clean_db.py'
    //       }
    //     }
    //   }
    // }

    stage('clean-DB-test-again') {
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
        powershell 'Remove-Item -Recurse -Force .venv'
      }
    }
    stage('docker push') {
      steps {
        script {
          docker.withRegistry( '', registryCredential ) {
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
  }
}