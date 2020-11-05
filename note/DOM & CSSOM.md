# DOM

HTML 태그들이 브라우저가 이해할 수 있는 노드라는 오브젝트로 변환이 된다.



### 구조

EventTarget

- Node
  - Document, Element, Text
    - HTMLElement
      - HTMLInputElement, HTMLDivElement



브라우저가 웹페이지 (HTML) 파일을 읽어서

한 줄 한 줄씩 읽으면서 DOM 트리로 변환하게 된다

브라우저가 이해할 수 있도록 자신들만의 오브젝트 트리로 만들어 가는것



window

- DOM, BOM, JavaScript



# CSSOM

> CSS Object Model



### CSS style은 브라우저가 어떻게 이해할까?

DOM과 CSS 의 요소들을 모두 병합해서 CSSOM을 만들어낸 후 합하여

사용자에게 보여질 부분만 Render Tree를 만들어 사용자에게 보여준다.

