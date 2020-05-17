# 20200516 CSS & JavaScript 체계적으로 작성

### CSS setting

```css
/* Global */
:root {
  /* Color */
  --color-white: #ffff;
  --color-light-white: #eeee;
  --color-dark-white: #bdbdbd;
  
  /* Font size */
  --font-large: 48px;
  --font-medium: 28px;
  --font-regular: 18px;
  --font-small: 16px;
  --font-micro: 14px;
  
	/* Font weight */
  --weight-bold: 700;
  --weight-semi-bold: 600;
  --weight-regular: 400;
  
  /* Size */
}

/* Universal tags */
* {
  box-sizing: border-box;
}

/* Typography */
h1 {
  font-size: var(--font-large);
  font-weight: var(--weight-bold);
  color: var(--color-light-white);
  margin: 16px 0;
}

```



- margin 때문에 중앙 정렬이 안되면 margin auto를 사용해라.. ( width:100% margin: 0 이런식으로 할 필요 없음 )
- flex 박스에서 공간을 차지하는 비율을 정할 때 flex-basis를 사용
- 높이를 중앙으로 맞출 때는 상위 태그의 높이만큼 line-height를 주면 된다.
- 이미지 같은 크기를 맞출때는 상위 박스의 넓이와 높이를 맞추고 이미지 의 max_width 와 max_height 을 100%로 맞춤