  - jekyll(지킬)이라는 static 웹페이지 서비스를 이용하여 md파일만 작성해서 github에 commit하는 것만으로 쉽게 관리할 수 있다. jekyll에서 이미 만들어 놓은 theme을 가져와 사용하는것이다.  아니면 html, css, java script로 다 작성해줘야하는데 생각만해도 머리가 아프다. html 익숙하지도 않고 css 등등 공수가 넘 많이 든다. 그리고 무엇보다 글쓸때 메타 글들이 더 많아져서 편집이 어렵다. 기술블로그 수준에선 markdown으로 만 사용해도 괜찮을것 같다.

  - [Jekyll themes 마켓](http://jekyllthemes.org/)에서 마음에드는것 다운로드

  - 압축풀어서 .git 폴더 제외하고 내용물 복사해서 Github에 push

  - 현재 다운 받은 theme이 어떻게 레이아웃등을 지원하는지 이해하고 수정하여 사용하면된다.

  - jekyll rtd theme을 받아서 사용하고 있는데 폴더단위로 레이아웃이 관리되고 폴더 마다 README.md가 있어야한다. README.md 내용의 첫 헤더가 이름으로 싸이드바 레이이아웃에 표시된다. 폴더 이름은 무시되기 때문에 문서작성의 혼동을 줄이기위해 같은 이름으로 하자. 레이아웃에서 컨텐츠의 순서는 --- sort: 1 --- 이런식으로 넣어주면 폴더의 순서가 정렬된다. README.md가 위치한 곳에 진짜 기록하고 싶은 md 파일드을 작성하기 시작할텐데 이 컨텐츠들 또한 같은 방법으로 순서를 정렬할수있다. --- sort: 1 --- 이 README.md와 중복되어서 사용되지만 별도로 관리된다. 즉, README.md는 폴더 구조만 관여되고 나머지 md파일들끼리 순서가 정렬된다.

  - Jekyll 디렉토리 구조
    - _includes
      - footer, header 등 html flagment
    - _layout
      - page 생성시 페이지 앞부분에 선언하여 선택하는 layout (jsp의 tile같은 느낌)

    - _posts

: markdown(.md) 등 블로그 글들이 저장되는 디렉토리

_sass

: css모음 (scss)


  - Github page를 이용해서 site를 생성하는 방법 [링크](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

 - 메뉴에서 settings를 선택 싸이드바에서 Pages를 선택하면 여러가지 설정을 할 수 있다.

  -  Branch 항목에서 Source에서 생성을 선택하고 어느 브랜치의 어느 폴더에서 빌드할지 선택 할 수있다.
  
  - 싸이트에 Jekyll을 연결하는 가이드 [링크](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll)가 있다.

  - Jekyll를 이용해서 로컬에서 테스트를 가이드해주는 [링크](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)를 소개해준다.

  - **참고한 싸이트**
    - Jekyll Github page 연동 [싸이트](https://github.com/gjchoi/gjchoi.github.io/blob/master/_posts/2016-02-18-Github-page%EB%A1%9C-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0.md)

    - [github page에서 Mermaid를 사용하여 diagram 그리기](https://frhyme.github.io/mermaid/Embedding_mermaid_in_github_page/)





