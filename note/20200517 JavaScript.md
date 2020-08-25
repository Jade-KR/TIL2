# 2020/05/17 Javascript Tip

### ScrollY 사용법

> [MDN: Window.scrollY](https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollY)ㄴ
>
> [MDN: Determining the dimensions of elements](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model/Determining_the_dimensions_of_elements)

```javascript
const navbar = document.querySelector('#navbar')
const navbarHeight = navbar.getBoundingClientRect().height;
document.addEventListener('scroll', () => {
  if (window.scrollY > navbarHeight) {
    navbar.classList.add('navbar--dark');
  } else {
    navbar.classList.remove('navbar--dark');
  }
})
```



### Scroll Into View

> [Element.scrollIntoView](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView)

``` javascript
const navbarMenu = document.querySelector('.navbar__menu');
navbarMenu.addEventListener('click', (event) => {
  const target = event.target;
  const link = target.dataset.link;
  if (link == null) {
    return;
  }
  const scrollTo = document.querySelector(link);
  scrollTo.scrollIntoView();
})
```



- display: none 일 때 에니메이션이 적용 안된다.
- Pointer-event: none; - 클릭이 안되게 함.





### Filtering

- html 버튼 태그들에 data-filter="" 값을 주고, 아이템들에 data-type="" 값을 준다.
- 