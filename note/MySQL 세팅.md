# MySQL 세팅

MySQL 워크벤치를 실행

```
MySQL Connections 에 + 버튼 클릭

Conection Name 과 Username, Password를 입력 후 Test Connection 클릭
```

> 사용자 이름과 비밀번호는 소문자로 입력하는 것이 좋다.



**워크벤치의 버전이 일치하지 않을 때 다음과 같은 에러가 뜨기도 한다**

```
There was an error while parsing the DDL retrieved from the server.
```

> 가상 환경에 세팅된 MySQL 워크벤치와 로컬에 설치된 워크벤치의 버전을 일치 시켜주면 해결된다.
>
> 이 문제가 아니라면 vagrant 가 실행되고 있는지 확인, 사용자명과 서버 주소가 정확한지 확인



새로 등록된 커넥션에 들어가 스키마 생성

테이블 탭에서 오른쪽 클릭해서 테이블을 생성할 수 있다.



### MySQL 사용자 계정 생성

> 하나의 웹 서버로 여러 웹사이트를 운영할 때 사이트 마다 계정을 생성하면 권한을 관리하기 편하다.



1. Administration에 Users and Privileges 선택
2. Add Account 클릭

```
Login name은 DB 이름과 일치시키는게 좋다.
Limit to Hosts Matching 은 접속을 제한할 때 사용
```

3. 생성된 사용자를 클릭 후 Add Entry 클릭하여 스키마 선택

```
밑에 체크 박스들을 모두 클릭하여 모든 명령을 실행할 수 있게 한다.
```



**이렇게 생성된 계정은 PHP 스크립트에서 데이터베이스 서버로 접속할 때 사용한다.**





