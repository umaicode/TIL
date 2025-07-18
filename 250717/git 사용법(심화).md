commit 메시지 수정하기

명령어 : git commit --amend

vim에디터에서 수정하고
esc -> :q! : 저장하지 않고 강제 종료
esc -> :wq! : 강제 저장하고 종료

====================================

git revert : 특정 commit을 없었던 일로 만들기

a.txt 만들고 commit
b.txt 만들고 commit
c.txt 만들고 commit

git log -> 해시값 전체 복사(ctrl + shift + c), 붙여넣기(shift + insert)

명령어 :
git revert 해시값 : 이 특정 커밋을 없었던 일로 만든다.
vim 에디터 -> esc -> :wq

==========================================

git reset : 특정 commit으로 되돌리기

git reflog : 이전 과거 commit 기록들을 모두 볼 수 있음

명령어 : git reset --hard HEAD@{번호}

=========================================

staging area 있는 작업을 working directory로 옮기기
(git add 취소하기)

<git 2.23 버전 이전>

1. commit이 없는 경우
git rm --cached 파일명
2. 이전에 했던 commit이 있는경우(권장 방법)
git restore --staged 파일명