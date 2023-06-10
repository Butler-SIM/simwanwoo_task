# simwanwoo_task
오케이포스 지원자 심완우 사전 과제입니다

- Django runserver 실행 방법 및 접속 URL
  
  [requirements.txt](requirements.txt)파일 인스톨 후
  
  터미널에서 python manage.py runserver 입력 후 
  http://127.0.0.1:8000/ 접속


- Docker run (또는 docker-compose up) 실행 방법 및 접속 URL

    터미널에서 docker compose up --build 입력 후

    http://127.0.0.1:1337/ 접속
    
    파이썬3.8-alpine 이미지 또는 nginx1.22-alpine 이미지가 없어 실행이 안되는 경우 
    
    아래 명령어를 입력하여 이미지를 받아 주시고 다시 실행해주세요

    docker pull python:3.8-alpine3.16 

    docker pull nginx:1.22-alpine

- 사정이 생겨 더이상 과제를 진행 할 수 없을 것 같아 급하게
제출하느라 dokcer실행시 static파일 관련 설정을 하지 못하였습니다 api테스트에는 문제 없으니 참고 바랍니다
    







- **API 테스트 방법** 또는 **Postman Export 결과 ( Postman Export 파일 또는 Postman URL )**

    TestCode는 DRF APITestCase를 사용하여 작성하였습니다
    
    테스트코드 실행 방법

    터미널에서 python manage.py test 입력

    Postman Export File 
    [OKPose_Task.postman_collection.json](OKPose_Task.postman_collection.json) <- 프로젝트내 첨부 하였습니다. Postman에서 import해서 사용하시면 됩니다.



이상입니다.

감사합니다
    
    
    