# A1 프롬프트 관리 프로그램

## 소개
Python 콘솔 기반 프롬프트 관리 프로그램입니다.  
프롬프트를 추가하고, 목록을 조회하고, 삭제할 수 있으며, 카테고리별 조회와 즐겨찾기 관리 기능도 제공합니다.

## 실행 방법
터미널에서 아래 명령어를 입력합니다.

python main.py

## 기능 목록
- 프롬프트 추가
- 프롬프트 목록 보기
- 프롬프트 삭제
- 즐겨찾기 추가/해제
- 즐겨찾기 프롬프트 목록 조회
- JSON 파일 저장 및 불러오기
- 카테고리별 Markdown 파일 내보내기
- 잘못된 입력 처리
- 종료 기능

## 사용 기술
- Python 3
- Git
- GitHub

## 프로젝트 구조
A1_prompt_manager/
├─ main.py
├─ README.md
├─ .gitignore
├─ prompts.json
└─ exports/
   ├─ 공부.md
   ├─ 면접.md
   └─ 글쓰기.md