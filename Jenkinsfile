
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\prath\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" --version'
            }
        }
        
stage('Check Workspace Files') {
    steps {
        bat 'echo Current directory:'
        bat 'cd'
        bat 'dir'
        bat 'dir /s /b requirements.txt'
        bat 'dir /s /b test_app.py'
        bat 'dir /s /b app.py'
    }
}


        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\prath\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install --user -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\prath\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-app .'
            }
        }
    }
}
