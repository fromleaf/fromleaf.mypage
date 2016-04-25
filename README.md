## 유용한 명령어(?)
_**Make**_
* insertuser - execute **manage.py shell < insert_user_data.py**
* migrate - makemigrations and migrate
* clean - remove migrations folders and excute makemigrations and migrate
* superclean - remove migrations folders and excute makemigrations and migrate. Create Super User

## TODO List
* 페이지 시작할 때, DB Data가져오는 것 때문인지 많이 느리다. Optimization 해야겠다.
* Skill Page - Level 이미지 표시(***oo)
* Studying Page - Django 공부하면서 만들었던 것들 볼 수 있도록 올려놔야겠다.
* Data insert하는 방법 JSON현태로 바꿔볼까? (inser_user_data.py에 구현하면 될 것 같다.)
* insert할 때, 각 attribute 입력할 때, **kwargs로 변경해야겠다. 진작에 이걸로 했었어야 했는데..
* 사용자 정보를 Django에서 제공해주는 기본 기능으로 바꿀 수 있을 것 같은데....
* Member 생성 시에 자동으로 Page 관련된 부분들 생성하도록 해야할 것 같다.
* 예외처리 부분이 많이 빠져있다. 그리고 로그 남기는 기능도 추가해야겠다.
* Unit Test Code도 작성해보자.
