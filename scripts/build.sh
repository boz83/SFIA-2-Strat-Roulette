export DATABASE_URI="${DATABASE_URI}"
export TEST_DB_URI="${TEST_DB_URI}"
docker-compose down --rmi all
docker-compose build
docker login -u "${DOCKER_USERNAME}" -p "${DOCKER_PASSWORD}"
docker-compose push