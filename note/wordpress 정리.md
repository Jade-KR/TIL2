# WordPress

워드프레스 필요 요소 

1. php
2. Apache
3. MySQL



###워드프레스 설치

1. Wordpress.org 에서 다운받은 파일들을 public 디렉터리에 넣어준다

2. config.php 에서 db 정보들을 입력한다.

3. 설치



### 테마 설정

- wp_content 디렉터리에 index.php, style.css, screenshot.png, single.php, page.php 파일 생성

Style.css

```css
/* 
  Theme Name: Prac
  Author: Jade
  Version: 1.0
*/
```

- 활성화



index.php

```php
<?php 
  while (have_posts()) {
    the_post(); ?>
      <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
      <?php the_content(); ?>
      <hr>
	<?php
};
?>
```



single.php

```php
<?php 
  while (have_posts()) {
    the_post(); ?>
      <h2><?php the_title(); ?></h2>
      <?php the_content(); ?>
      <hr>
	<?php
};
?>
```



page.php

```php
<?php 
  while (have_posts()) {
    the_post(); ?>
      <h2><?php the_title(); ?></h2>
      <?php the_content(); ?>
      <hr>
	<?php
};
?>
```





 

### 글 관리

- 글을 작성 한다
- php 코드 수정하여 화면 노출
- have_posts() 글이 있는지 확인
- the_title() 제목
- The_content() 내용

```php
<?php 
  while (have_posts()) {
    the_post(); ?>
      <h2><?php the_title(); ?></h2>
      <?php the_content(); ?>
      <hr>
	<?php 
}
?>
```



## Header & Footer

Theme 디렉터리에 header.php, Footer.php를 만든다

header와 footer를 적용하고 싶은 곳에서 get_header(); get_footer(); 작성하여 호출한다



### header에 css, javascript 적용하기

```php
function prac_files() {
  wp_enqueue_script('nickname', 'url', 'dependency check (NULL)', 'version num', true('body태그 닫기 전에 load하고 싶은지'));
  wp_enqueue_style('prac_main_styles', get_stylesheet_uri()); // main.css
}

add_action('wp_enqueue_scripts', 'prac_files');
```



header.php

Head 태그에 wp_head(); php 코드 넣는다

Body 태그와 html 태그를 닫지 않는다. Footer (적용하기위해)

```php+HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <?php wp_head();?>
</head>
<body>
 
```



Functions.php 파일을 만든다 (자바스크립트와 css 를 적용할 수 있다)

```php
function prac_files() {
  wp_enqueue_style('prac_main_styles', get_stylesheet_uri());
}

add_action('wp_enqueue_scripts', 'prac_files');
```



Footer.php

wp_footer(); 를 body태그 닫기 전에 넣는 것은

자바스크립트를 마지막에 실행시키기 위해 넣는다.

```php+HTML
<p>greeting from footer</p>

<?php wp_footer();?>
</body>
</html>
```



### 이미지 폴더 url 접근하기

**get_theme_file_uri('/url')**

<?php get_theme_file_uri('/url') ?> - 워드프레스가 theme까지의 경로를 자동으로 잡아준다



## Avoiding CSS & JS Caching During Development

### Caching 이란?

> Cache에 데이터를 미리 복사해 놓으면 계산이나 접근 시간 없이 더 빠른 속도로 데이터에 접근할 수 있다. 결국 Cache란 반복적으로 데이터를 불러오는 경우에, 지속적으로 DBMS 혹은 서버에 요청하는 것이 아니라 Memory에 데이터를 저장하였다가 불러다 쓰는 것을 의미한다.



이런 기능 때문에 개발단계에서 즉시 변화를 봐야 할 때 못보는 경우가 생긴다. (css, javascript)

그래서 wordpress에서 caching을 중지 하여 개발한다

**function.php 에서 version을 microtime()으로 사용한다.**

```php
function prac_files() {
  wp_enqueue_script('nickname', 'url', 'dependency check (NULL)', microtime()  , true('body태그 닫기 전에 load하고 싶은지'));
  wp_enqueue_style('prac_main_styles', get_stylesheet_uri()); // main.css
}

add_action('wp_enqueue_scripts', 'prac_files');
```





## Interior page.php template

page.php

```php
<?php get_header();
  while (have_posts()) {
    the_post(); ?>
      //필요한 내용 넣기
	<?php get_footer();
};
?>
```



## 자동으로 타이틀 넣기

functions.php

```php
 <?php
function prac_files() {
  wp_enqueue_script('main-prac-js', get_theme_file_uri('/js/scripts-bundled.js'), NULL, '1.0', true);
  wp_enqueue_style('custom-google-fonts', '//fonts.googleapis.com/css?family=Roboto+Condensed:300,300i,400,400i,700,700i|Roboto:100,300,400,400i,700,700i');
  wp_enqueue_style('font-awesome', '//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css');
  wp_enqueue_style('prac_main_styles', get_stylesheet_uri());
}

add_action('wp_enqueue_scripts', 'prac_files');

function prac_features() {
  add_theme_support('title-tag');
}

add_action('after_setup_theme', 'prac_features');
?>
```



## 링크 넣기

```php
<?php echo site_url() ?>
```

> root url로 세팅해주는 코드 (로컬이든 배포를 하든 편하게 사용가능)



## Parent & Children Pages

wordpress 에서 child page 생성

부모 페이지로 가는 버튼을 children 페이지에서만 보여주려면?

```php
wp_get_post_parent_id(get_the_ID()); 
```

> 위 코드는 부모 페이지의 id 값을 return 하고 부모가 없으면 0을 return 한다.

 

Get_the_title(); - 현재 페이지의 id 값을 리턴

Get_permalink(); - 고유의 Url 리턴

 

## 부모페이지에서 자식 페이지 링크 만들기

wp_list_pages(); - 페이지 리스트를 전부 불러온다 (연관배열이다)

```php
if ($theParent) {
  $findChildrenOf = $theParent;
} else {
  $findChildrenOf = get_the_ID();
}
wp_list_pages(array(
	'title_li' => NULL,
  'child_of' => $findChildrenOf
));
```



자식이 있는지 체크

```php
$testArray = get_pages(array(
	'child_of' => get_the_ID()
));
```

 



###associative array란?

> 변수와 인덱스와 value 값이 서로 연관되어 있게 만들어진 배열 



### 페이지 순서를 정하려면?

```php
 if ($theParent) {
  $findChildrenOf = $theParent;
} else {
  $findChildrenOf = get_the_ID();
}
wp_list_pages(array(
	'title_li' => NULL,
  'child_of' => $findChildrenOf,
  'sort_column' => 'menu_order'
));
```

> 'sort_column' => 'menu_order' 를 추가하고 페이지를 만들 때 Order을 설정한다 



## 헤더 html 세팅

Html 언어 설정

```php+HTML
<html <?php languague_attributes();?>>
  ...
</html>
```

디바이스별 사이즈 설정 - 헤더에 meta 태그 추가 후 CSS에서 반응형으로 만들어야함

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

어떤 종류의 숫자, 글들을 사용할지 설정

```php+HTML
<meta charset="<?php bloginfo('charset');?>">
```

클래스를 자동 생성

> 자바스크립트, CSS에서 유용하게 사용가능

```php+HTML
<body <?php body_class(); ?>>
  ...
</body>
```



## 동적인 네비게이션 메뉴 

### 관리자 페이지에 메뉴 추가하기

add_action('after_setup_theme') 객체의 register_nav_menu(); 사용하여 메뉴를 추가한다

```php+HTML
<?php
function prac_files() {
  wp_enqueue_script('main-prac-js', get_theme_file_uri('/js/scripts-bundled.js'), NULL, microtime(), true);
  wp_enqueue_style('custom-google-fonts', '//fonts.googleapis.com/css?family=Roboto+Condensed:300,300i,400,400i,700,700i|Roboto:100,300,400,400i,700,700i');
  wp_enqueue_style('font-awesome', '//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css');
  wp_enqueue_style('prac_main_styles', get_stylesheet_uri(), NULL, microtime());
}

add_action('wp_enqueue_scripts', 'prac_files');

function prac_features() {
  register_nav_menu('headerMenuLocation', 'Header Menu Location')
  add_theme_support('title-tag');
}

add_action('after_setup_theme', 'prac_features');
?>
```

> headerMenuLocation 은 나중에 호출할 때 필요한 key값
>
> Header Menu Location 은 관리자 페이지에 체크박스로 나온다
>
> 관리자페이지에서 메뉴들을 선택 후 넣고싶은 곳에 체크박스 체크하고 생성

관리자 페이지에서 메뉴를 등록 후 nav 태그에

```php+HTML
<?php 
wp_nav_menu(array(
  'theme_location' => 'headerMenuLocation'
));
?>
```



### 커스텀 메뉴 만들기

ACF 플러그인 다운

 

```php+HTML
<ul>
              <li <?php if (is_page('about-us') or wp_get_post_parent_id(get_the_ID(0) == 14 )) echo 'class="current-menu-item"' ?>><a href="<?php echo site_url('/about-us');?>">About Us</a></li>
              <li><a href="#">Programs</a></li>
              <li><a href="#">Events</a></li>
              <li><a href="#">Campuses</a></li>
              <li><a href="#">Blog</a></li>
            </ul>
```



## Blog Building

Front-page.php 파일 만들기

index.php 코드 모두 front-page.php 에 복사





### Pagination

```php+HTML
<?php get_header(); ?>

<div class="page-banner">
  <div class="page-banner__bg-image" style="background-image: url(<?php echo get_theme_file_uri('/images/ocean.jpg'); ?>);"></div>
  <div class="page-banner__content container container--narrow">
    <h1 class="page-banner__title">Welcome to our blog!</h1>
    <div class="page-banner__intro">
      <p>Keep up with our latest news!</p>
    </div>
  </div>  
</div>

<div class="container container--narrow page-section">
  <?php
    while (have_posts()) {
      the_post(); ?>
      <div class="post-item">
        <h2 class="headline headline--medium headline--post-tile"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
        <div class="metabox">
          <p>Posted by <?php the_author_posts_link(); ?> on <?php the_time('n.j.y');?> in <?php echo get_the_category_list(', ')?></p>
        </div>
        <div class="generic-content">
          <?php the_excerpt(); ?>
          <p><a class="btn btn--blue" href="<?php the_permalink();?>">Continue reading &raquo;</a></p>
        </div>
      </div>
    <?php }
  // 여기 시작
  echo paginate_links();
  ?>
</div>

<?php get_footer(); ?>
```



##Archive.php

> 설명이 필요하다

- archive.php 파일 생성
- Index.php 복사 붙여넣기



1. 카테고리인지, 작성자 인지 판단하여 글쓰기 가능
   - Is_category();, is_author();, single_cat_title(), the_author();  



```php+HTML
<?php get_header(); ?>

<div class="page-banner">
  <div class="page-banner__bg-image" style="background-image: url(<?php echo get_theme_file_uri('/images/ocean.jpg'); ?>);"></div>
  <div class="page-banner__content container container--narrow">
    <h1 class="page-banner__title"><?php if (is_category()) {
      single_cat_title();
      };
      if (is_author()) {
        echo "Posts by ";the_author();
      }
      ?></h1>
    <div class="page-banner__intro">
      <p>Keep up with our latest news!</p>
    </div>
  </div>  
</div>

<div class="container container--narrow page-section">
  <?php
    while (have_posts()) {
      the_post(); ?>
      <div class="post-item">
        <h2 class="headline headline--medium headline--post-tile"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
        <div class="metabox">
          <p>Posted by <?php the_author_posts_link(); ?> on <?php the_time('n.j.y');?> in <?php echo get_the_category_list(', ')?></p>
        </div>
        <div class="generic-content">
          <?php the_excerpt(); ?>
          <p><a class="btn btn--blue" href="<?php the_permalink();?>">Continue reading &raquo;</a></p>
        </div>
      </div>
    <?php }
    echo paginate_links();
  ?>
</div>

<?php get_footer(); ?>
```



위 코드처럼 if 절로 다 나눠서 적는 것은 힘들다 그래서 아래와 같이 작성하면 자동으로 생성해준다

```php
the_archive_title();
the_archive_description();
```





## Custom Queries

>  url에 default 값을 활용 할 수 없으면 각각의 custom query를 만들어서 사용해야한다.
>
> Custom Query를 작성할때는 항상 변수를 만들어야한다

**Front-page.php**

 ```php
<?php
  $homepagePosts = new WP_Query(array(
  	'posts_per_page' => 2
  ));
  
  while ($homepagePosts->have_posts()) {
    $homepagePosts->the_post(); ?>
      <li><?php the_title();?></li>
      <?php }
?>
 ```



- wp_trim_words(get_the_content(), 18); - 18단어를 가져옴

- Wp_reset_postdata(); - wordpress 데이터를 원래 상태로 돌려놓음

  > custom query를 사용하고 while문을 나오고 사용하는 습관을 들여야한다.



 ## Automation

> 코드가 바뀔때마다 자동으로 새로고침을 해준다.

gulp 를 사용한다

```
sudo npm install gulp-cli -g

```

https://github.com/LearnWebCode/vagrant-lamp 

위 링크에서 4가지 파일을 public에 넣는다

```
sudo npm install
```

setting.js 에서 theme 경로와 url을 바꿔준다

```
gulp watch
```

종료는 command + c



### CSS 자동 refresh 시키기

> WordPress는 CSS 폴더에 있는 것을 인식하지 못한다

style.css 의 주석으로 달아놓은 아래 코드를 css/style.css 파일 상단에 넣는다

```css
/* 
  Theme Name: Prac
  Author: Jade
  Version: 1.0
*/
```



## Custom post type

function.php

```php
function prac_post_types() {
  register_post_type('event', array(
  	'public' => true,
    'labels' => array(
    	'name' => 'Events'
    ),
    'menu_icon' => 'dashicons-calendar'
  ));
}

add_action('init', 'prac_post_types');
```



위처럼 하면 admin 페이지에서 event 관리를 할 수 있다

**그러나 Theme에만 의존해야 하기 때문에 문제가 있다**



Custom post type을 가장 잘 관리하는 방법은 Must Use Plugins을 사용하는 것



### Must Use Plugins

> 독립적인 폴더를 가지고 있어서 비활성화시키기 어렵다



Wp-content 디렉터리에 mu-plugins 폴더를 생성하고 안에 post-type 을 저장할 php파일을 생성

**Prac-post-types.php**

```php
function prac_post_types() {
  register_post_type('event', array(
    'has_archive' => true,
  	'public' => true,
    'labels' => array(
    	'name' => 'Events'
    ),
    'menu_icon' => 'dashicons-calendar'
  ));
}

add_action('init', 'prac_post_types');
```

 

이렇게 하면 관리자가 Theme을 변경하거나 모든 플러그인을 비활성화 시키더라도 post-type 을 관리할 수 있다



### 관리자 페이지 post-type 커스텀 하는 방법

Prac-post-types.php

```php
<?php
function prac_post_types() {
  register_post_type('event', array(
  	'public' => true,
    'labels' => array(
      'name' => 'Events',
      'add_new_item' => 'Add New Event',
      'edit_item' => 'Edit Event',
      'all_items' => 'All Events',
      'singular_name' => 'Event'
    ),
    'menu_icon' => 'dashicons-calendar'
  ));
}

add_action('init', 'prac_post_types');
```

> register_post_type 구글에서 검색하면 원하는 부분을 커스텀 할 수 있다.



## Custom Post Type 보여주기

**Front-page.php**

```php+HTML
<?php get_header();?>
<div class="page-banner">
      <div class="page-banner__bg-image" style="background-image: url(<?php echo get_theme_file_uri('/images/library-hero.jpg');?>);"></div>
      <div class="page-banner__content container t-center c-white">
        <h1 class="headline headline--large">Welcome!</h1>
        <h2 class="headline headline--medium">We think you&rsquo;ll like it here.</h2>
        <h3 class="headline headline--small">Why don&rsquo;t you check out the <strong>major</strong> you&rsquo;re interested in?</h3>
        <a href="#" class="btn btn--large btn--blue">Find Your Major</a>
      </div>
    </div>

    <div class="full-width-split group">
      <div class="full-width-split__one">
        <div class="full-width-split__inner">
          <h2 class="headline headline--small-plus t-center">Upcoming Events</h2>
				  
          <?php
            $homepageEvents = new WP_Query(array(
            	'posts_per_page' => 2,
              'post_type' => 'event'
            ));
          
          	while($homepageEvents->have_posts()) {
              $homepageEvents->the_post(); ?>
          		<div class="event-summary">
            <a class="event-summary__date t-center" href="#">
              <span class="event-summary__month">Mar</span>
              <span class="event-summary__day">25</span>
            </a>
            <div class="event-summary__content">
              <h5 class="event-summary__title headline headline--tiny"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h5>
              <p><?php echo wp_trim_words(get_the_content(), 18);?> <a href="<?php the_permalink(); ?>" class="nu gray">Learn more</a></p>
            </div>
          </div>
            <?php }
          ?>

          
        	.....
```

**이렇게 변경하여 링크를 타고 들어가면 없는 페이지라고 나오는데**

**admin 페이지에서 해결할 수 있다.**

**Settings -> Permalinks -> Save Change**

> 이전에 event를 생성했는데 아직 워드프레스는 event를 모르기 때문에 변경사항을 저장해줘야한다.



### Event Posts 에만 따로 single 파일을 적용하고 싶으면?

> 워드프레스는 single-(post type name)을 확인한다
>
> 그래서 event의 디테일페이지는 single-event.php 의 코드를 받음



**Single-event.php**

```php+HTML
<?php get_header();
  while (have_posts()) {
    the_post(); ?>
    <div class="page-banner">
    <div class="page-banner__bg-image" style="background-image: url(<?php echo get_theme_file_uri('/images/ocean.jpg'); ?>);"></div>
    <div class="page-banner__content container container--narrow">
      <h1 class="page-banner__title"><?php the_title();?></h1>
      <div class="page-banner__intro">
        <p>Don't forget to replace me later</p>
      </div>
    </div>  
  </div>
  <div class="container container--narrow page-section">
  <div class="metabox metabox--position-up metabox--with-home-link">
      <p><a class="metabox__blog-home-link" href="<?php echo site_url('/blog');?>">
      <i class="fa fa-home" aria-hidden="true"></i> Events Home</a>
      <span class="metabox__main"><?php the_title(); ?></span></p>
    </div>

    <div class="generic-content"><?php the_content();?></div>
  </div>
	<?php 
};
get_footer();
?>
```



Archive-event.php

```php+HTML
<?php get_header(); ?>

<div class="page-banner">
  <div class="page-banner__bg-image" style="background-image: url(<?php echo get_theme_file_uri('/images/ocean.jpg'); ?>);"></div>
  <div class="page-banner__content container container--narrow">
    <h1 class="page-banner__title">All Events</h1>
    <div class="page-banner__intro">
      <p>See what is going on in our world.</p>
    </div>
  </div>  
</div>

<div class="container container--narrow page-section">
  <?php
    while (have_posts()) {
      the_post(); ?>
      <div class="event-summary">
            <a class="event-summary__date t-center" href="#">
              <span class="event-summary__month">Mar</span>
              <span class="event-summary__day">25</span>
            </a>
            <div class="event-summary__content">
              <h5 class="event-summary__title headline headline--tiny"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h5>
              <p><?php echo wp_trim_words(get_the_content(), 18);?> <a href="<?php the_permalink(); ?>" class="nu gray">Learn more</a></p>
            </div>
          </div>
    <?php }
    echo paginate_links();
  ?>
</div>

<?php get_footer(); ?>
```



get_post_type_archive_link('event') - event의 url을 가져옴



## Custom Field

 Mu-plugins

```php
<?php
function prac_post_types() {
  register_post_type('event', array(
    'supports' => array('title', 'editor', 'excerpt', 'custom-fields'),
    'has_archive' => true,
  	'public' => true,
    'labels' => array(
      'name' => 'Events',
      'add_new_item' => 'Add New Event',
      'edit_item' => 'Edit Event',
      'all_items' => 'All Events',
      'singular_name' => 'Event'
    ),
    'menu_icon' => 'dashicons-calendar'
  ));
}

add_action('init', 'prac_post_types');
```



그럼 Custom Fields 박스가 나타난다.

하지만 field 명을 하나하나 다 기억해야해서 너무 힘들다..

그래서 Plugins을 활용한다 (밑에 둘 중 하나 선택)

- Advanced Custom Fields (ACF) - 이게 좀 더 낫다
- CMB2 (Custom Metaboxes 2)



플러그인을 설치하면 위에서 정의한 custom-fields 를 안적어도 된다

활성화하면 custom fields 메뉴가 생긴다



### 날짜 field가 생겼는데 이것을 어떻게 화면에 노출할까?

the_field(필드 명)

> 필드명은 admin 페이지에서 확인 가능하다

**원하는 형태의 날짜 가져오기**

```php
$eventDate = new DateTime(get_field('event_date')); // 아무것도 입력하지 않으면 현재 날짜를 기준으로함
echo $eventDate->format('M');
```



## Custom Query

```php
<?php
            $homepageEvents = new WP_Query(array(
            	'posts_per_page' => 2,
              'post_type' => 'event',
              'orderby' => 'post_date'
            ));
```

Posts_per_page => -1 은 모든 페이지를 보여줌

Orderby => 'title',

'order' => 'ASC'

orderby => 'rand'



다가올 가장 최근 이벤트 정렬하기

```php
<?php
            $homepageEvents = new WP_Query(array(
            	'posts_per_page' => -1,
              'post_type' => 'event',
              'meta_key' => 'event_date',
              'orderby' => 'meta_value_num',
              'order' => 'ASC'
            ));
```



과거의 이벤트를 보여주지 않으려면

```php
<?php
  					$today = date('Ymd')
            $homepageEvents = new WP_Query(array(
            	'posts_per_page' => -1, 'post_type' => 'event',
              'meta_key' => 'event_date',
              'orderby' => 'meta_value_num',
              'order' => 'ASC',
              'meta_query' => array(
              	array(
                	'key' => 'event_date',
                  'compare' => '>=',
                  'value' => $today,
                  'type' => 'numeric'
                )
              )
            ));
```

>  



## Edit Default Queries

> 새로운 커스텀 쿼리를 만드는 것
>
> default 값인 url의 event를 파괴하지 않아도 된다



functions.php

```php
function prac_adjust_queries($query) {
  if (!is_admin() && is_post_type_archive('event') AND $query->is_main_query()) {
    $today = date('Ymd');
    $query->set('meta_key', 'event_date');
    $query->set('orderby', 'meta_value_num');
    $query->set('order', 'ASC');
    $query->set('meta_query', array(
      array(
        'key' => 'event_date',
        'compare' => '>=',
        'value' => $today,
        'type' => 'numeric'
      )
      ));
  }
}
add_action('pre_get_posts', 'prac_adjust_queries');
```

> $query->set('posts_per_page', '1'); 는 admin이 아닐때와 post_type_archive가 'event' 일때 작동한다.
>
> default query를 조작하기위해서



## Past Event Page

1. admin 페이지에서 Past Events 페이지를 만든다.
2. slug를 확인 후 Theme 디렉터리에서 page-past-events.php 파일을 만든다
3. Archive-event.php 내용을 복사하여 page-past-events.php 에 붙여넣기 한다

```php+HTML
<?php get_header(); ?>

<div class="page-banner">
  <div class="page-banner__bg-image" style="background-image: url(<?php echo get_theme_file_uri('/images/ocean.jpg'); ?>);"></div>
  <div class="page-banner__content container container--narrow">
    <h1 class="page-banner__title">Past Events</h1>
    <div class="page-banner__intro">
      <p>A recap our past events</p>
    </div>
  </div>  
</div>

<div class="container container--narrow page-section">
  <?php
    
    $today = date('Ymd');
    $pastEvents = new WP_Query(array(
            'post_type' => 'event',
            'meta_key' => 'event_date',
            'orderby' => 'meta_value_num',
            'order' => 'ASC',
            'meta_query' => array(
              array(
                'key' => 'event_date',
                'compare' => '<',
                'value' => $today,
                'type' => 'numeric'
              )
            )
          ));
    while ($pastEvents->have_posts()) {
      $pastEvents->the_post(); ?>
      <div class="event-summary">
      <a class="event-summary__date t-center" href="#">
              <span class="event-summary__month">
                <?php
                  $eventDate = new DateTime(get_field('event_date'));
                  echo $eventDate->format('M');
                ?>
              </span>
              <span class="event-summary__day"><?php echo $eventDate->format('d');?></span>
            </a>
            <div class="event-summary__content">
              <h5 class="event-summary__title headline headline--tiny"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h5>
              <p><?php echo wp_trim_words(get_the_content(), 18);?> <a href="<?php the_permalink(); ?>" class="nu gray">Learn more</a></p>
            </div>
          </div>
    <?php }
    echo paginate_links();
  ?>
</div>

<?php get_footer(); ?>
```



### 페이지네이션 추가

echo paginate_links(); 가 코드 아래에 있더라도 작동하지 않는다..

> 워드프레스가 만든 default query 에서만 작동함..

**해결법은?**

```php
 echo paginate_links(array(
 	'total' => $pastEvents->max_num_pages
 ));
```

페이지는 생겨났지만 이동하더라도 새로운 내용을 보여주지 않는다.

**해결법은?**

> query에서 페이지를 받는 방법은
>
> get_query_var('paged', 1) - paged 는 페이지 넘버를 받고, 1은 default로 지정

```php
$today = date('Ymd');
    $pastEvents = new WP_Query(array(
      			'paged' => get_query_var('paged', 1),
            'post_type' => 'event',
            'meta_key' => 'event_date',
            'orderby' => 'meta_value_num',
            'order' => 'ASC',
            'meta_query' => array(
              array(
                'key' => 'event_date',
                'compare' => '<',
                'value' => $today,
                'type' => 'numeric'
              )
            )
          ));
```



### Past events 확인하는 링크 만들기

```php+HTML
<p>
  Looking for a recap of past evets? <a href="<?php echo site_url('/past-events')?>">Check out our past events archive.</a>
</p>
```



## Creating "Program" post type

functions.php

```php
// Program post type
  register_post_type('program', array(
    'supports' => array('title', 'editor'),
    'rewrite' => array('slug' => 'programs'),
    'has_archive' => true,
    'public' => true,
    'labels' => array(
      'name' => 'Programs',
      'add_new_item' => 'Add New Program',
      'edit_item' => 'Edit Program',
      'all_items' => 'All Programs',
      'singular_name' => 'Program'
    ),
    'menu_icon' => 'dashicons-awards'
  ));
}
add_action('init', 'prac_post_types');
```

새 글을 쓰고 페이지를 확인해보면 없는 페이지라고 나온다

admin 페이지 세팅 -> 고유주소 (permalink) -> 저장

위와 같이 하여 워드프레스가 다시 빌드하도록 만들어줘야함



### program 디테일 페이지 만들기

**single-program.php 생성**

원래 있던 single.php 의 코드를 복사하여 붙여넣기

세부 내용 수정



archive-program.php 파일 생성

Archive-event.php 코드 복사하여 붙여넣기

세부 내용 수정



**내용 조작하기**

Functions.php

```php
function prac_adjust_queries($query) {
  if (!is_admin() && is_post_type_archive('program') AND $query->is_main_query()) {
    $query->set('orderby', 'title');
    $query->set('order', 'ASC');
    $query->set('posts_per_page', -1);
  }
  
  if (!is_admin() && is_post_type_archive('event') AND $query->is_main_query()) {
    $today = date('Ymd');
    $query->set('meta_key', 'event_date');
    $query->set('orderby', 'meta_value_num');
    $query->set('order', 'ASC');
    $query->set('meta_query', array(
      array(
        'key' => 'event_date',
        'compare' => '>=',
        'value' => $today,
        'type' => 'numeric'
      )
      ));
  }
}
add_action('pre_get_posts', 'prac_adjust_queries');

?>
```



### Custom Field 만들고 event와 program 관계 만들기

admin 페이지에서 custom Field 새로 만들기로 type을 relationship으로 선택

post type은 program으로, location에서 post type is equal to event



**이렇게 만들었으면 어떻게 사용을 해야할까?**

Single-event.php 파일에서 하단에 코드를 추가한다

> relatedPrograms가 무엇을 들고있는지 알고싶으면
>
> Print_r($relatedPrograms); 를 사용하면 다 나온다

```php+HTML
<?php
	
  $relatedPrograms = get_field('related_programs');

	if ($relatedPrograms) {
    echo '<hr class="section-break">';
	echo '<h2 class="headline headline--medium">Related Program(s)</h2>';
	echo '<ul class="link-list min-list">';
	foreach($relatedPrograms as $program) {?>
<li><a href="<?php echo get_the_permalink($program); ?>"><?php echo get_the_title($program); ?></a></li>
  <?php }
  echo '</ul>';
  ?>
  }
```



프로그램페이지에서 관련된 이벤트 보여주기

single.program.php

```php+HTML
<?php get_header();
  while (have_posts()) {
    the_post(); ?>
    <div class="page-banner">
    <div class="page-banner__bg-image" style="background-image: url(<?php echo get_theme_file_uri('/images/ocean.jpg'); ?>);"></div>
    <div class="page-banner__content container container--narrow">
      <h1 class="page-banner__title"><?php the_title();?></h1>
      <div class="page-banner__intro">
        <p>Don't forget to replace me later</p>
      </div>
    </div>  
  </div>

  <div class="container container--narrow page-section">
  <div class="metabox metabox--position-up metabox--with-home-link">
      <p><a class="metabox__blog-home-link" href="<?php echo get_post_type_archive_link('program');?>">
      <i class="fa fa-home" aria-hidden="true"></i> All Programs</a>
      <span class="metabox__main"><?php the_title(); ?></span></p>
    </div>

    <div class="generic-content"><?php the_content();?></div>

    <?php
            $today = date('Ymd');
            $homepageEvents = new WP_Query(array(
              'posts_per_page' => 2,
              'post_type' => 'event',
              'meta_key' => 'event_date',
              'orderby' => 'meta_value_num',
              'order' => 'ASC',
              'meta_query' => array(
              	array(
                	'key' => 'event_date',
                  'compare' => '>=',
                  'value' => $today,
                  'type' => 'numeric'
                ),
                // 새로운 필터를 추가한다.
                // 이 배열이 related_programs이면
                // contain하고
                // 현재 program post의 id값
                array(
                  'key' => 'related_programs', // serialize
                  'compare' => 'LIKE',
                  'value' => '"' . get_the_ID(). '"' // "12" 같이 쌍따움표를 포함해야한다
                )
              )
            ));
          
          	while($homepageEvents->have_posts()) {
              $homepageEvents->the_post(); ?>
          		<div class="event-summary">
            <a class="event-summary__date t-center" href="#">
              <span class="event-summary__month">
                <?php
                  $eventDate = new DateTime(get_field('event_date'));
                  echo $eventDate->format('M');
                ?>
              </span>
              <span class="event-summary__day"><?php echo $eventDate->format('d');?></span>
            </a>
            <div class="event-summary__content">
              <h5 class="event-summary__title headline headline--tiny"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h5>
              <p><?php echo wp_trim_words(get_the_content(), 18);?> <a href="<?php the_permalink(); ?>" class="nu gray">Learn more</a></p>
            </div>
          </div>
            <?php }
          ?>
  </div>
	<?php 
};
get_footer();
?>
```







## Professors Post Type

 single-professor.php

```php+HTML
<?php get_header();
  while (have_posts()) {
    the_post(); ?>
    <div class="page-banner">
    <div class="page-banner__bg-image" style="background-image: url(<?php echo get_theme_file_uri('/images/ocean.jpg'); ?>);"></div>
    <div class="page-banner__content container container--narrow">
      <h1 class="page-banner__title"><?php the_title();?></h1>
      <div class="page-banner__intro">
        <p>Don't forget to replace me later</p>
      </div>
    </div>  
  </div>

  <div class="container container--narrow page-section">
  <div class="metabox metabox--position-up metabox--with-home-link">
      <p><a class="metabox__blog-home-link" href="<?php echo get_post_type_archive_link('program');?>">
      <i class="fa fa-home" aria-hidden="true"></i> All Programs</a>
      <span class="metabox__main"><?php the_title(); ?></span></p>
    </div>

    <div class="generic-content"><?php the_content();?></div>

    <?php 

$relatedProfessors = new WP_Query(array(
  'posts_per_page' => -1,
  'post_type' => 'professor',
  'orderby' => 'title',
  'order' => 'ASC',
  'meta_query' => array(
    array(
      'key' => 'related_programs',
      'compare' => 'LIKE',
      'value' => '"'.get_the_ID().'"'
    )
  )
));

if ($relatedProfessors->have_posts()) {
  echo '<hr class="section-break">';
echo '<h2 class="headline headline--medium">' . get_the_title() .' Professors</h2>';

while($relatedProfessors->have_posts()) {
  $relatedProfessors->the_post(); ?>
  <li><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></li>
<?php }
}

wp_reset_postdata();

            $today = date('Ymd');
            $homepageEvents = new WP_Query(array(
              'posts_per_page' => 2,
              'post_type' => 'event',
              'meta_key' => 'event_date',
              'orderby' => 'meta_value_num',
              'order' => 'ASC',
              'meta_query' => array(
              	array(
                	'key' => 'event_date',
                  'compare' => '>=',
                  'value' => $today,
                  'type' => 'numeric'
                ),
                array(
                  'key' => 'related_programs',
                  'compare' => 'LIKE',
                  'value' => '"'.get_the_ID().'"'
                )
              )
            ));

            if ($homepageEvents->have_posts()) {
              echo '<hr class="section-break">';
            echo '<h2 class="headline headline--medium">Upcoming '. get_the_title() .' Events</h2>';
          
          	while($homepageEvents->have_posts()) {
              $homepageEvents->the_post(); ?>
          		<div class="event-summary">
            <a class="event-summary__date t-center" href="#">
              <span class="event-summary__month">
                <?php
                  $eventDate = new DateTime(get_field('event_date'));
                  echo $eventDate->format('M');
                ?>
              </span>
              <span class="event-summary__day"><?php echo $eventDate->format('d');?></span>
            </a>
            <div class="event-summary__content">
              <h5 class="event-summary__title headline headline--tiny"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h5>
              <p><?php echo wp_trim_words(get_the_content(), 18);?> <a href="<?php the_permalink(); ?>" class="nu gray">Learn more</a></p>
            </div>
          </div>
            <?php }
            }
          ?>
  </div>
	<?php 
};
get_footer();
?>
```



## Featured Image

이미지를 업로드 하기 위한 세팅

functions.php

```php
function prac_features() {
  add_theme_support('title-tag');
  add_theme_support('post-thumbnails');
}

add_action('after_setup_theme', 'prac_features');

```



Mu-plugin

Prac-post-types.php (thumbnail 추가)

```php
register_post_type('professor', array(
    'supports' => array('title', 'editor', 'thumbnail'),
    'public' => true,
    'labels' => array(
      'name' => 'Professors',
      'add_new_item' => 'Add New Professor',
      'edit_item' => 'Edit Professor',
      'all_items' => 'All Professors',
      'singular_name' => 'Professor'
    ),
    'menu_icon' => 'dashicons-welcome-learn-more'
  ));
}
```

 

이미지 등록



single.professor.php 에 가서 이미지 추가하기

```php+HTML
<div class="generic-content"><?php the_post_thumbnail(); the_content();?></div>
```

보기좋게 만들기

```php+HTML
<div class="generic-content">
      <div class="row group">
        <div class="one-third">
          <?php the_post_thumbnail();?>
        </div>
        <div class="two-third">
          <?php the_content(); ?>
        </div>
      </div>
    </div>
```

- The_post_thumbnail_url()



이미지 사이즈 조절하기

wp-content => upload => 여러 크기의 이미지가 저장되어 있다 (워드프레스가 자동을 생성함)



functions.php

```php
function prac_features() {
  add_theme_support('title-tag');
  add_theme_support('post-thumbnails');
  add_image_size('professorLandscape', 400, 260, true);
  // 속성 ('닉네임', '넓이', '높이', 자르기 여부)
  add_image_size('professorPortrait', 480, 650, true);
}

add_action('after_setup_theme', 'prac_features');


```



### 플러그인 사용

regenerate thumbnails 설치 - 활성화

Tools - regen, Thumbnails



###어떻게 화면에 보여줄까?

single.professor.php

```php+HTML
<div class="generic-content">
      <div class="row group">
        <div class="one-third">
          <?php the_post_thumbnail('professorPortrait');?>
        </div>
        <div class="two-third">
          <?php the_content(); ?>
        </div>
      </div>
    </div>
```



워드프레스는 이미지를 잘라낼때 중앙을 위주로 잘라낸다

### 잘라내는 것을 조절 하는 방법은?

플러그인을 활용하자..



## 유저가 이미지를 업로드 할 수 있게 하는 방법

 Custom Field 추가

Single-professor.php

```php+HTML
<div class="page-banner">
    <div class="page-banner__bg-image" style="background-image: url(<?php 
    $pageBannerImage = get_field('page_banner_background_image'); echo $pageBannerImage['url']
    ?>);"></div>
    <div class="page-banner__content container container--narrow">
      <h1 class="page-banner__title"><?php the_title();?></h1>
      <div class="page-banner__intro">
        <p><?php the_field('page_banner_subtitle')?></p>
      </div>
    </div>  
  </div>
```

커스텀한 사이즈 이미지로 보기

```php+html
<div class="page-banner">
    <div class="page-banner__bg-image" style="background-image: url(<?php 
    $pageBannerImage = get_field('page_banner_background_image'); echo $pageBannerImage['sizes']['pageBanner']
    ?>);"></div>
    <div class="page-banner__content container container--narrow">
      <h1 class="page-banner__title"><?php the_title();?></h1>
      <div class="page-banner__intro">
        <p><?php the_field('page_banner_subtitle')?></p>
      </div>
    </div>  
  </div>
```



## 반복되는 코드 줄이기

 functions.php

```php
 //반복되는 코드를 복사 하여 함수 만들기
 <?php

function pageBanner($args) {
  
   if (!$args['title']) {
     $args['title'] = get_the_title();
   }
   
   if (!$args['subtitle']) {
     $args['subtitle'] = get_field('page_banner_subtitle');
   }
  ?>
  <div class="page-banner">
    <div class="page-banner__bg-image" style="background-image: url(<?php 
    $pageBannerImage = get_field('page_banner_background_image'); echo $pageBannerImage['size']['pageBanner']
    ?>);"></div>
    <div class="page-banner__content container container--narrow">
      <h1 class="page-banner__title"><?php echo $args['title']?></h1>
      <div class="page-banner__intro">
        <p><?php echo $args['subtitle']?></p>
      </div>
    </div>  
  </div>

<?php
}
```

> title이 없으면 default 값으로 get_the_title()을 사용하고

page.php

```php+HTML

```

