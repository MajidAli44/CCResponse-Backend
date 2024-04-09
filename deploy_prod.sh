#!/bin/sh

ssh -o StrictHostKeyChecking=no root@$EC2_PUBLIC_IP_ADDRESS << 'ENDSSH'
  cd /home/root/ccresponse-crm
  export $(cat ./.env | xargs)
  docker login -u $DOCKER_CCRESPONSE_USER -p $DOCKER_CCRESPONSE_TOKEN
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_rsa

  ( cd ccresponse-docker && git pull && cd ../ ) || git clone git@gitlab.com:ccresponse/ccresponse-docker.git -b feature/add_redis_worker
  git switch feature/add_redis_worker || true
  cp -r ccresponse-docker/* ./
  chmod +x step-1-prepare-for-letsencrypt.sh step-2-letsencrypt.sh step-3-live.sh
ENDSSH

ssh -o StrictHostKeyChecking=no root@$EC2_PUBLIC_IP_ADDRESS << 'ENDSSH'
  cd /home/root/ccresponse-crm && sudo ./step-1-prepare-for-letsencrypt.sh
ENDSSH

ssh -o StrictHostKeyChecking=no root@$EC2_PUBLIC_IP_ADDRESS << 'ENDSSH'
  cd /home/root/ccresponse-crm && sudo ./step-2-letsencrypt.sh
ENDSSH

ssh -o StrictHostKeyChecking=no root@$EC2_PUBLIC_IP_ADDRESS << 'ENDSSH'
  cd /home/root/ccresponse-crm && sudo ./step-3-live.sh
ENDSSH
