pipeline{
  agent any
  environment {


    DATABASE_URI = credentials('DATABASE_URI')
    SECRET_KEY = credentials('SECRET_KEY')

    TEST_DB_URI = credentials('TEST_DB_URI')
    TEST_SECRET_KEY = credentials('TEST_SECRET_KEY')
  }
}