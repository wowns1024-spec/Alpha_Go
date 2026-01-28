### 📘 Coding Test Study 

본 저장소는 **부울경 1반 코딩테스트 스터디**를 위한 저장소입니다.  
**개인 브랜치**에서 작업 후, 매주 **Pull Request(PR)** 를 통해 제출하는 방식으로 진행합니다.
**제발 본인 이름으로된 폴더와 브랜치만 사용해주세요**

---

## 1️⃣ 폴더 구조 (고정)
모든 코드는 아래와 같이 **이름 > 주차 > 문제** 순서의 폴더 구조를 따릅니다.

```text
(root)/
├─ yunjeong/           <-- 본인 이름(영어)
│  ├─ Week1/           <-- 주차
│  │  ├─ 1000_A+B.py
│  │  └─ 42840_모의고사.py
│  └─ Week2/
├─ jaejoon/
│  └─ Week1/
├─ miri/
│  └─ Week1/
└─ README.md
```

## 2️⃣ 파일 및 커밋 규칙
📄 파일명 규칙
문제번호_문제이름.확장자

예시: 1000_A+B.py, 42840_모의고사.java

✅ 커밋 메시지 규칙
주차_문제이름_본인이름

예시: Week1_A+B_yunjeong

예시: Week1_모의고사_miri

## 3️⃣ Git 작업 프로세스
🚀 Step 1. 브랜치 생성 및 이동
작업 전 항상 master를 최신화하고, 본인 이름의 브랜치에서 작업을 시작합니다.
```
# master 최신화
git switch master
git pull origin master


# 본인 브랜치로 이동 (없다면 -c 옵션으로 생성)
git switch -c 본인이름  # 예: git switch -c yunjeong
```

📝 Step 2. 코드 작성 및 커밋  
본인 폴더(이름/WeekN/)에 문제를 풀고 규칙에 맞춰 커밋합니다.
```
git add .
git commit -m "Week1_A+B_yunjeong"
```
📤 Step 3. Push 및 PR 보내기  
본인 브랜치에 코드를 올린 후, GitHub 페이지에서 Pull Request를 생성합니다.

```
git push origin 본인이름

PR 제목 규칙: [ 사이트명 - 주차 ] 작성자명
예시: [BOJ - Week1] yunjeong
예시: [PG - Week2] miri
```
📄 Step 4. 노션에 표시  
[노션으로 이동](https://www.notion.so/2f4ab8281e0481e99fb7db6464ab51bc?source=copy_link)

✅ Step 5. 1주일에 한번 merge(master에 합치기)

```
git switch master       // 마스터로 이동
git pull origin master  // 마스터 최신화
git merge (내브랜치 이름)

git push origin master // 하기전에 생각할 것 (깃허브에 업로드)
```
* 중요한점 내 폴더만 무조건 수정할 것 


###  **사이트 약어**  
```
백준 - BOJ  
프로그래머스 - PRO  
leetcode - LEET  
```

## 4️⃣ 스터디 운영 규칙
PR 마감: 매주 정해진 시간까지 PR을 생성해야 합니다.  
코드 리뷰: 스터디원은 서로의 PR에 최소 1개 이상의 코멘트(리뷰)를 남깁니다.  
Merge: 리뷰가 완료되면 스터디장 또는 본인이 master 브랜치로 병합합니다.  
