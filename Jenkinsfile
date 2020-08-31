pipeline{
  agent any
  environment {
    DATABASE_URI = credentials('DATABASE_URI')
    SECRET_KEY = credentials('SECRET_KEY')

    TEST_DB_URI = credentials('TEST_DB_URI')
    TEST_SECRET_KEY = credentials('TEST_SECRET_KEY')
  }
  stages {
    stage('Configure'){
      steps{
        sh 'chmod +x ./scripts/*'
        sh './scripts/build.sh'
      }
    }
    stage('Test'){
      steps{
        sh './scripts/test.sh'
      }
    }
    stage('Build'){
      steps{
        sh './scripts/test.sh'
      }
    }
    stage('Deploy'){
      steps{
        sh './scripts/deploy.sh'
      }
    }
  }
}