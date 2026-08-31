# 기본 프롬프트 데이터 3개
prompts = [
    {
        "title": "자기소개 생성",
        "content": "신입 개발자 자기소개서를 작성해줘.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "고양이 이미지 프롬프트",
        "content": "우주복을 입은 귀여운 고양이 이미지를 만들어줘.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "공부 계획표 만들기",
        "content": "파이썬 기초를 2주 동안 공부할 수 있는 계획표를 작성해줘.",
        "category": "자동화",
        "favorite": False
    }
]


def show_menu():
    print("\n=== 프롬프트 관리 프로그램 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 종료")


def add_prompt():
    print("\n[프롬프트 추가]")

    title = input("제목을 입력하세요: ").strip()
    if title == "":
        print("빈 제목은 저장할 수 없습니다.")
        return

    content = input("내용을 입력하세요: ").strip()
    if content == "":
        print("빈 내용은 저장할 수 없습니다.")
        return

    category = input("카테고리를 입력하세요: ").strip()
    if category == "":
        print("빈 카테고리는 저장할 수 없습니다.")
        return

    prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(prompt)
    print("프롬프트가 저장되었습니다.")


def show_prompt_list():
    print("\n[저장된 프롬프트 목록]")

    if len(prompts) == 0:
        print("아직 저장된 프롬프트가 없습니다.")
    else:
        for i, prompt in enumerate(prompts, start=1):
            star = "⭐" if prompt["favorite"] else ""
            print(f"{i}. {prompt['title']} | {prompt['category']} {star}")


while True:
    show_menu()
    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        add_prompt()
    elif choice == "2":
        show_prompt_list()
    elif choice == "3":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 입력하세요.")