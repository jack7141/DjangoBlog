<h1 align="center">Welcome to AIFFEL 👋</h1>
<p>
</p>

> AIFFEL Coding Test

## Author

👤 **황광회**

👤 **Superuser ID**
* admin
👤 **Superuser password**
* 0000

## ⭐️ To get started with project, run the following in a virtual environment:
> venv\Scripts\activate.bat

> pip install -r requirements.txt

> python manage.py migrate

> python manage.py createsuperuser

> python manage.py runserver

## Show your API

    자세한 명시는 Swagger를 통하여 :8000번 포트에서 확인 할 수 있습니다.
    - http://127.0.0.1:8000/

    * Header Token 주의사항
    Swagger에서 주어지는 API UI로 처리할 시 superuser로 처리하게끔 되어있습니다.


 * Questions URL

    ## Method [GET] : 질문에 관한 전체 리스트를 Return합니다.

    /questions/

    URL Palams:

    Required: None
    
    ## Method [POST] : 질문을 생성합니다.

    /questions/create/

    URL Palams: 
    * title : string
    * body : string

    Required: Header Token

    - **Request Header:**
    
    Authorization: {token type] {access token]

    ex) Authorization: Token ee7aed09cc4e2abca4411947767bfee28a550dab

    ## Method [GET,PUT, DELETE] : 특정 질문을 요청, 수정, 삭제합니다.

    /questions/{int:id}/

    URL Palams: 

    * id : int

    Required: None


 * Review URL

    ## Method [GET] : 특정 질문에 대한 댓글을 리턴합니다.

    /reviews/{question_id}/

    URL Palams:
    * question_id : int

    Required: None
    
    ## Method [POST] : 질문에 대한 댓글을 생성합니다.

    /reviews/{question_id}/create

    URL Palams: 
    * body: string
    * is_like :true/false

    Required: Header Token

    - **Request Header:**
    
    Authorization: {token type] {access token]

    ex) Authorization: Token ee7aed09cc4e2abca4411947767bfee28a550dab


 * USER URL

    ## Method [GET] : 유저들을 모두 리턴합니다

    /users/

    URL Palams:

    Required: None
    
    ## Method [POST] : 유저 로그인을 통해 토큰을 발급합니다.

    /users/signin/

    URL Palams: 
    * username : string
    * password : string

    return: Token

    ## Method [POST] : 유저를 생성하고 토큰을 발급합니다.

    /users/signup/

    URL Palams: 
    * username : string
    * password : string

    return: Token




