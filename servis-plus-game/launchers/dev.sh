#!/bin/bash

# Set Node.js and npm paths
export NODE_PATH="/home/adil/.config/nvm/versions/node/v22.11.0/bin"
export PATH="$NODE_PATH:$PATH"

# Build the backend
echo "Building the backend..."
cd backend || { echo "Backend directory not found!"; exit 1; }
"$NODE_PATH/npm" install && "$NODE_PATH/npm" run build || { echo "Backend build failed!"; exit 1; }
cd ..

# Build the frontend
echo "Building the frontend..."
cd frontend || { echo "Frontend directory not found!"; exit 1; }
"$NODE_PATH/npm" install && "$NODE_PATH/npm" run build || { echo "Frontend build failed!"; exit 1; }
cd ..

# Copy the .env file to dockerfiles directory
cp .env dockerfiles

# Bring down the existing illusium_dev environment
sudo docker-compose -p illusium_dev -f dockerfiles/docker-compose-dev.yml down -v

# Build the illusium_dev images
sudo docker-compose -p illusium_dev -f dockerfiles/docker-compose-dev.yml build

# Bring up the illusium_dev environment
sudo docker-compose -p illusium_dev -f dockerfiles/docker-compose-dev.yml up
