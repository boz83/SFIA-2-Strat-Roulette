pipeline{
  agent any
  environment {
    DATABASE_URI = credentials('DATABASE_URI')
    TEST_DB_URI = credentials('TEST_DB_URI')
    DOCKER_USERNAME = credentials('DOCKER_USERNAME')
    DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
  }
  stages {
    stage('Configure'){
      steps{
        sh 'chmod +x ./scripts/*'
        sh './scripts/config.sh'
      }
    }
    stage('Build'){
      steps{
        sh './scripts/build.sh'
      }
    }
    stage('Test'){
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