# A script to remove unused Docker containers, images, and volumes.

#!/bin/bash

# Remove stopped containers
docker container prune -f

# Remove dangling images
docker image prune -f

# Remove unused volumes
docker volume prune -f

echo "Docker cleanup completed."
