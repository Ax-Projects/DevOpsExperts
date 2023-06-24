pipeline {
  agent {
    node {
      label 'laptop'
    }
  }
  stages {
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

    stage('stop-servers') {
      steps {
        bat 'python clean_environment.py'
      }
    }
  }
}