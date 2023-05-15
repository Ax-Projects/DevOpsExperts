pipeline {
  agent {
    node {
      label 'laptop'
    }

  }
  stages {
    stage('start-backend') {
      parallel {
        stage('start-backend') {
          steps {
            bat(script: 'start /min python rest_api.py', returnStdout: true, returnStatus: true)
          }
        }

        stage('start-front') {
          environment {
            python = 'C:\\Users\\Orr-Dev\\Documents\\DevOpsExperts\\.venv\\Scripts\\python.exe'
          }
          steps {
            bat(script: 'start python web_app.py', returnStdout: true, returnStatus: true)
          }
        }

      }
    }

    stage('clean-DB') {
      steps {
        bat 'python clean_db.py'
      }
    }

    stage('run-backend-test') {
      steps {
        bat 'python backend_testing.py'
      }
    }

    stage('run-frontend-test') {
      steps {
        bat 'python frontend_testing.py'
      }
    }

    stage('run-combined-tests') {
      steps {
        bat 'python combined_testing.py'
      }
    }

    stage('stop-servers') {
      steps {
        bat 'python clean_environment.py'
      }
    }

  }
  environment {
    python = 'C:\\Users\\Orr-Dev\\Documents\\DevOpsExperts\\.venv\\Scripts\\python.exe'
  }
}