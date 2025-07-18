![git]()

GUI : 그래픽 유저 인터페이스
TUI : 텍스트 (이말은 잘 안씁니다.)

CLI : Command Line Interface

interface : 대상을 제어하는 수단 ( ex) 리모컨) )

========================================

Window OS의 Interface
GUI : Windows Shell
CLI : cmd(명령프롬프트), Power Shell

Linux OS의 Interface
GUI : GNOME
CLI : bash

왜 굳이 bash를 쓸까??
bash가 편해서 ---> Tab키 자동완성

Git을 다룰때 Interface
GUI : Github Desktop, 소스트리
CLI : git bash

결론 : GUI, CLI 둘다 쓸수는 있어야하지만 우리는 CLI를 쓸겁니다.

GUI의 장점 : 그래프 같은 복잡한 분석 보기 편하다
CLI의 장점 : 빠르다(Commit 명령어 3~4초면 끝)

====================================================

리눅스는 항상 HOME 디렉토리에서 시작 : ~
. : 현재 디렉토리
cd ~ : 홈 디렉토리
cd .. : 상위 디렉토리
cd - : 뒤로가기

touch : 파일생성
mkdir : 폴더생성
start : 파일 열기
rm : 파일 삭제
rm -rf : 폴더 삭제
cp : 복사

절대경로
~/Desktop/test/python/

상대경로(현재 티렉토리를 기준)
cd ./python
cd ../python2

=======================================================

python.org ---> python 설치 ---> 3.11.9
인터프리터

extension??
너 IDE 뭐써??
vscode는 IDE일까??
vscode는 텍스트 에디터 : 여기에 extension을 추가해서 마치 IDE처럼 쓴다.

IDE
Python : Pycharm, jupyter notebook
C : Visual Studio
Java : IntelliJ

node.js ---> 런타임
js 백엔드 프레임워크 ---> express.js 

====================================================================

Markdown : 로직 X 
README.md에 활용
: 내가 공부한내용, 프로젝트에 대한 간단한 설명(가독성, 편의성)

============================================================

git init  : git 시작 (로컬 저장소 생성)
rm -rf .git : git 삭제(git 종료)

git add . : staging area에 변경사항 올리기
git status : staging area의 작업 파일 확인

git config --global user.email "이메일주소"
git config --global user.name "이름"
git config --global -l

git commit -m "메시지명" : repository에(staging area의 변경사항을)올리기
git log : repository 작업 파일 확인 (커밋 이력 확인)

===================================================

참고자료 

git commit --amend : vim 에디터가 열린다

수정 후(커서 위치를 확인 후 과감하게 타이핑)

ecs -> :q -> 저장하지 않고 종료
ecs -> :q! -> 저장하지 않고 강제 종료
ecs -> :wq -> 저장하고 종료

===================================================

# git 기본

git : 분산 버전 관리 시스템

git : 로컬저장소 // github : 원격저장소

git init : git 시작

git add . : staging area에 올리기
git status : staging area의 작업 파일 확인

<git commit 전에>
git config --global [user.name](http://user.name/) "이름"
git config --global user.email "이메일"
git config --global -l : user.name과 user.email 확인

git commit -m "메시지명" : repository에 올리기
git log : 커밋 이력을 확인

git remote add origin url : 로컬 저장소와 원격저장소를 연결(origin은 별칭)
git remote -v : remote 목록 확인

git remote rm 별칭 : remote 이력 삭제

git push origin +master : 가장 최근에 commit 되어있던 것을 강제로 push
(origin:별칭, master:branch명, +:강제로 진행)

==================================================

Q) clone과 pull의 차이점이 뭘까??
A) 새로운 환경에서 처음 다운로드 : clone

명령어 : git clone url

Q) clone을 받으면 remote를 할 필요가 있을까?
A) remote를 할 필요가 없다.

Q) clone과 pull의 차이?
A) 한번 clone을 받고 그 이후에는 pull로 진행

명령어 : git pull origin +master

==================================================

자리 옮긴후

1. git clonfig --global -l 확인
[user.name](http://user.name/), user.email 확인
2. 제어판 -> 사용자 계정 -> window 자격 증명 -> github, gitlab 삭제

=================================================

Q) .gitignore 파일은 왜 만들까?
A) 수 백개의 파일을 일일이 git add 하기에는 불편하기 때문에
.gitignore파일을 만들면 편하다

용량이 매우 크거나, 보안상 문제가 있거나, 청구 결제 관련된 파일들을
add 하지 않기 위해 .gitignore파일을 만든다(staging area에 올리지 않기 위해)

방법 : .gitignore 파일 생성 -> add 하지 않을 파일명이나 폴더명 작성하고 저장