<h1 align="center">Welcome to DjangoBlog ๐</h1>
<p>
</p>


## Author

๐ค **ํฉ๊ดํ**

๐ค **Superuser ID**
* admin

๐ค **Superuser password**
* 0000

## โญ๏ธ To get started with project, run the following in a virtual environment:
> venv\Scripts\activate.bat

> pip install -r requirements.txt
> 
> python manage.py makemigrations
> 
> python manage.py migrate

> python manage.py createsuperuser

> python manage.py runserver

## Show your API

    ์์ธํ ๋ช์๋ Swagger๋ฅผ ํตํ์ฌ :8000๋ฒ ํฌํธ์์ ํ์ธ ํ  ์ ์์ต๋๋ค.
    - http://127.0.0.1:8000/

    * Header Token ์ฃผ์์ฌํญ
    Swagger์์ ์ฃผ์ด์ง๋ API UI๋ก ์ฒ๋ฆฌํ  ์ superuser๋ก ์ฒ๋ฆฌํ๊ฒ๋ ๋์ด์์ต๋๋ค.


 * Questions URL
    ## Search
    
    /questions/?search=ํค์๋

    ## Method [GET] : ์ง๋ฌธ์ ๊ดํ ์ ์ฒด ๋ฆฌ์คํธ๋ฅผ Returnํฉ๋๋ค.

    /questions/

    URL Palams:

    Required: None
    
    ## Method [POST] : ์ง๋ฌธ์ ์์ฑํฉ๋๋ค.

    /questions/create/

    URL Palams: 
    * title : string
    * body : string

    Required: Header Token

    - **Request Header:**
    
    Authorization: {token type] {access token]

    ex) Authorization: Token ee7aed09cc4e2abca4411947767bfee28a550dab

    ## Method [GET,PUT, DELETE] : ํน์  ์ง๋ฌธ์ ์์ฒญ, ์์ , ์ญ์ ํฉ๋๋ค.

    /questions/{int:id}/

    URL Palams: 

    * id : int

    Required: None


 * Review URL

    ## Method [GET] : ํน์  ์ง๋ฌธ์ ๋ํ ๋๊ธ์ ๋ฆฌํดํฉ๋๋ค.

    /reviews/{question_id}/

    URL Palams:
    * question_id : int

    Required: None
    
    ## Method [POST] : ์ง๋ฌธ์ ๋ํ ๋๊ธ์ ์์ฑํฉ๋๋ค.

    /reviews/{question_id}/create

    URL Palams: 
    * body: string
    * is_like :true/false

    Required: Header Token

    - **Request Header:**
    
    Authorization: {token type] {access token]

    ex) Authorization: Token ee7aed09cc4e2abca4411947767bfee28a550dab


 * USER URL

    ## Method [GET] : ์ ์ ๋ค์ ๋ชจ๋ ๋ฆฌํดํฉ๋๋ค

    /users/

    URL Palams:

    Required: None
    
    ## Method [POST] : ์ ์  ๋ก๊ทธ์ธ์ ํตํด ํ ํฐ์ ๋ฐ๊ธํฉ๋๋ค.

    /users/signin/

    URL Palams: 
    * username : string
    * password : string

    return: Token

    ## Method [POST] : ์ ์ ๋ฅผ ์์ฑํ๊ณ  ํ ํฐ์ ๋ฐ๊ธํฉ๋๋ค.

    /users/signup/

    URL Palams: 
    * username : string
    * password : string

    return: Token




