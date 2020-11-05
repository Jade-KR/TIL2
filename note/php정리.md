# PHP 기본

① : 클라이언트가 웹 브라우저를 통해 웹 서버에 원하는 웹 페이지를 요청합니다.

② : 웹 서버는 클라이언트가 요청한 웹 페이지의 로직 및 데이터베이스와의 연동을 위해 PHP 파서(parser)에 이에 대한 처리를 요청합니다.

③ : 이때 PHP 파서는 데이터베이스와의 연동이 필요하면 데이터베이스와 데이터의 처리를 수행합니다.

④ : PHP 파서는 웹 페이지의 로직 및 데이터베이스와의 작업 처리 결과를 웹 서버로 전달합니다.

⑤ : 웹 서버는 전달받은 데이터로 웹 페이지를 완성하여 웹 브라우저로 응답을 전송합니다.

### form

```
form에서 action 속성이 빈값이면 현재 URL로 폼을 전송한다.
```



### php 숙련자들의 작성법

```
문자열은 작은 따움표를 사용한다
파일 내용이 전부 php 코드이면 ?>를 생략한다.
```

### include

```
include '' = 상대경로다. 이 파일이 위치한 디렉터리에서 검색을 함
```

### 구조화 주의점

```
사용자가 웹 브라우저로 직접 접근할 파일만 public 디렉터리에 둔다. (html, css, JavaScript)
include문으로 참조하는 모든 파일은 사용자가 직접 접근할 수 없도록 public 디렉터리 외부에 둔다.
파일을 조직적으로 관리하기 위해 종류에 따라 더로 다른 디렉터리에 저장하는 편이 좋다.
```

### 구조화

Count.php

```php
$output = '';
for ($count = 1; $count <= 10; $count++) {
  $output .= $count . ' ';
}

include __DIR__.'count.html.php';
```

count.html.php

```php+HTML
<body>
  <p>
    <?php echo $output; ?>
  </p>
</body>
```



## 객체 지향 프로그래밍

```php+HTML
<?php
class MyFileObject {
  function isFile() {
    return is_file('data.txt');
  }
}
$file = new MyFileObject();
var_dump($file->isFile());
?>
```



### php 생성자

constructor = 클래스를 기반으로 해서 인스턴스를 만드는 역할을 하는 것

```php+HTML
<?php
class MyFileObject{
  function __construct($fname) {
    $this->filename = $fname;
  }
  function isFile() {
    return is_file($this->filename);
  }
}
$file = new MyFileObject('data.txt');
?>
```



### 캡슐화 - 불필요한 정보를 감추는 것 (접근제어)

```php+HTML
<?php
class MyFileObject{
  private $filename;
  function __construct($fname) {
    $this->filename = $fname;
    if(!file_exists($this->filename)) {
      die('There is no file '.$this->filename);
    }
  }
  function isFile() {
    return is_file($this->filename);
  }
}
$file = new MyFileObject('data.txt');
$file->filename = 'asdfekf.txt';
?>
```



```php
class Person {
  private $name;
  function sayHi() {
    print("Hi, I'm {$this->name}.");
  }
  function setName($_name) {
    $this->ifEmptyDie($_name);
    $this->name = $_name;
  }
  function getNmae() {
    return $this->name;
  }
  private function ifEmptyDie($value) {
    if (empty($_name)) {
      die('I need name');
    }
  }
}
$jade = new Person();
$jade->setName('jade');
$jade->sayHi();
print($jade->getName());
```



### 상속

```php
class Animal {
  function run() {
    print('running...');
  }
  function breathe() {
    print('breathing...');
  }
}
class Human extends Animal {
  function think() {
    print('thinking...');
  }
  function talk() {
    print('talking...');
  }
}
$human = new Human();
$human->run();
$human->think();
```



### Static

> 클래스 소속의 멤버를 만드는 것 (static)
>
> 인스턴스의 멤버를 만드는 것 (static이 없는 것)
>
> 인스턴스에 대한 자기 자신을 원할때는 $this->
>
> 클래스에 대한 자기 자신을 원할 때는 self::

```php
class Person {
  private static $count = 0;
  private $name;
  function __construct($name) {
    $this->name = $name;
    self::$count += 1
  }
  function enter() {
    echo "<h1>Enter ".$this->name." ".self::$count."th<h1>"
  }
  static function getCount() {
    return self::$count;
  }
}
$p1 = new Person('jade');
$p1->enter();
$p2 = new Person('leezche');
$p2->enter();
$p3 = new Person('duru')
```



### Class loading & Namespace

greeting.php

```php
class Hi {
  function __construct() {
    echo 'hi';
  }
}
```

1. 이해하긴 쉽지만 불편함이 조금 있는 방식

```php
require_once 'greeting.php'
```

2. 필요로 하는 파일을 자동으로 require 할 수 있는 방법

```php
function autoloader($path) {
  $path = $path.'.php';
  var_dump("path : {$path}");
  require_once $path;
}
spl_autoload_register('autoloader');
new Hi();
```

### Namespace

```php
namespace greeting\en;
  class Hi {
  function __construct() {
    echo '<h1>h1</h1>';
  }
}
namespace greeting\ko;
class Hi {
  function __construct() {
    echo '<h1>안녕</h1>';
  }
}
new \greeting\en\Hi();
new \greeting\ko\Hi();

use \greeting\en\Hi as HiEn;
use \greeting\ko\Hi as HiKo;
new HiEn();
new HiKo();
```



### 상속 오버라이딩 (부모클래스가 가진 기능을 덮어쓰기 할 때)

```php
class ParentClass {
  function __construct($param) {
    echo "<h1>Parent {$param}</h1>";
  }
  function callMethod($param) {
    echo "<h2>Parent {$param}</h2>";
  }
}
class ChildClass extends ParentClass {
  function __construct($param) {
    parent::__construct($param);
    echo "<h1>Child {$param}<h1>";
  }
  function callMethod($param) {
    parent::callMethod($param);
    echo "<h2>Child {$param}</h2>";
  }
}
```



### 접근제어자(protected)

> 인스턴스를 통해 직접 접근은 금지하면서 상속관계를 통해 연결되어있는
>
> 자식의 메서드를 통해 접근하면 가능하다

```php
class ParentClass {
  public $_public = 'public';
  protected $_protected = 'protected';
  private $_private = 'private';
}
class ChildClass extends ParentClass {
  function callPublic() {
    echo $this->_public;
  }
  function callProtected() {
    echo $this -> _protected;
  }
  function callPrivate() {
    echo $this->_private;
  }
}
$obj = new ChildClass();
echo $obj -> _public;
echo $obj->_private;
$obj->callPublic();
```



### 상속과 final

> 부모가 가진 기능을 자식이 상속받지 못하게 하고 싶을 때

```php
class ParentClass {
  function a() {
    echo 'Parent';
  }
  final function b() {
    echo 'Parent B';
  }
}
class ChildClass extends ParentClass{
  function a() {
    echo 'Child';
  }
  function b() {
    echo 'Child B';
  }
}

$obj = new ChildClass();
```



### Interface

> 아울렛과 플러그
>
> 규격과 표준같은 규제가 있기 때문에 
>
> 규제에 안에서 구현을 자유롭게 하기 위해서 interface 가 존재

```php
interface ContractInterface
{
  public function promiseMethod(array $param):int;
}
class ConcreateClass implements ContractInterface
{
  public function promiseMethod(array $param):int
  {
    return 10;
  }
}
$obj = new ConcreateClass();
$obj->promiseMethod([1,2]);
```

> ConcreateClass 는 ContractInterface에 정의되어 있는 method를 반드시 구현해야한다.



### Abstract

> 상속과 구현을 강제하는 것을 함께 가지는 클래스

```php
abstract class ParentClass
{
  public function a()
  {
    echo 'a';
  }
  public abstract function b();
}
class ChildClass extends ParentClass
{
  public function b()
  {
    
  }
}
```





