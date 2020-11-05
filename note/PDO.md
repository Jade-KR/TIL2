# PDO

PDO를 사용해 MySQL서버에 접속하는 코드

```php
new PDO('mysql:host=호스트명;dbname=데이터베이스명;charset=utf8', '사용자명', '비밀번호')
```



Try... catch 로 오류가 해결이 안될 때 오류 메세지를 화면에 노출하는 방법

```php
try {
  $pdo = new PDO('mysql:host=localhost;dbname=ijdb;charset=utf8', 'ijdb', '111111');
  $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $output = '데이터베이스 접속 성공';
}
catch (PDOException $e) {
  $output = '데이터베이스 서버에 접속할 수 없습니다.'.$e;
}
```



수십개의 파일을 include하는 대형 웹사이트에서 유용한 에러 메세지 처리

> 상황이 닥쳤을 때 확인하는 용도로 사용하면 좋다

```php
try {
  $pdo = new PDO('mysql:host=localhost;dbname=ijdb;charset=utf8', 'ijdb', '111112');
  $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $output = '데이터베이스 접속 성공';
}
catch (PDOException $e) {
  $output = '데이터베이스 서버에 접속할 수 없습니다.'.
  $e->getMessage().', 위치: '.
  $e->getFile().':'.$e->getLine();
}

include __DIR__.'/../templates/output.html.php'
```



### PDO를 이용한 SQL 쿼리 전송

```php
$pdo->exec($query);
```

> $query 변수에 실행하고자 하는 SQL 쿼리 문자열을 담는다



SELECT 결과 처리를 할때는 query() 메서드를 사용한다.

> exec()와 다르게 PDOStatement 객체를 반환하여 $result에 저장한다

```php
$pdo->query($query);
```



모든 레코드를 확인할 때 반복문을 사용하는데 for문은 레코드의 갯수를 모르기 때문에 while문을 사용한다

```php
while ($row = $result->fetch()) {
  // 로우 처리
}
```



**PDOStatement 객체의 fetch() 메서드는 결과 집합의 로우를 하나씩 배열로 반환하다가 반환할 로우가 없으면 false를 반환한다**

```php
$row = $result->fetch()
```



```php
while ($row = $result->fetch()) {
  $jokes[] = $row['joketext'];
}
```



echo문이나 include 문을 바로 브라우저에 보내지 앟고 버퍼링을 주는 방법

```php
ob_start(); // 출력 버퍼링을 시작하는 함수, 내용을 브라우저로 전달하지 않고 버퍼에 저장시킴
include __DIR__. '/../templates/addjoke.html.php'
$output = ob_get_clean(); // 버퍼의 내용을 반환하고 기존 버퍼를 비운다.
```



**유저로부터 넘겨받은 정보 $_POST['joketext']를 안전하게 INSERT 쿼리에 넣는 방법 (SQL injection Attack 방어)**

```php
$sql = 'INSERT INTO `joke` SET
`joketext` = :joketext
`jokedate` = CURDATE()
';
$stmt = $pdo->prepare($sql);

$stmt->bindValue(':joketext', $_POST['joketext']);
$stmt->execute();
```

> joketext 의 값이 들어갈 자리에 :joketext 라는 자리 표시자를 넣는다
>
> PDO 객체의 prepare()메서드를 호출하고 SQL 쿼리를 인수로 전달
>
> 서버는 prepare()로 전달될 쿼리를 미리 검사하고, joketext 값이 없으므로 아직 실행하지 않는다.
>
> Prepare()메서드는 PDOStatement 객체를 반환하며 $stmt 변수에 담는다.
>
> 쿼리에 빠진 값을 PDOStatement 객체의 bindValue() 메서드로 채워 넣으면 준비된 구문을 실행할 수 있다.
>
> bindValue() 메서드에 전달하는 인수는 자리표시자와 그에 해당하는 값이다.



Redirect 시키기

```php
header('Location: 이동할 URL');
```











