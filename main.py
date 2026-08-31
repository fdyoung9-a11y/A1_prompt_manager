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
    print("3. 프롬프트 삭제")
    print("4. 종료")

def add_prompt():
    print("\n[프롬프트 추가]")

    title = input("제목을 입력하세요: ").strip()
    if title == "":
        print("제목은 비워둘 수 없습니다.")
        return

    content = input("내용을 입력하세요: ").strip()
    if content == "":
        print("내용은 비워둘 수 없습니다.")
        return

    category = input("카테고리를 입력하세요: ").strip()
    if category == "":
        print("카테고리는 비워둘 수 없습니다.")
        return

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)
    print("프롬프트가 추가되었습니다.")

def show_prompt_list():
    print("\n[프롬프트 목록]")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        print(f"{i}. {prompt['title']} | {prompt['category']}")

def delete_prompt():
    print("\n[프롬프트 삭제]")

    if not prompts:
        print("삭제할 프롬프트가 없습니다.")
        return

    show_prompt_list()

    choice = input("삭제할 프롬프트 번호를 입력하세요: ").strip()

    if not choice.isdigit():
        print("숫자를 입력해주세요.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(prompts):
        print("올바른 번호를 입력해주세요.")
        return

    deleted = prompts.pop(index)
    print(f"'{deleted['title']}' 프롬프트가 삭제되었습니다.")

while True:
    show_menu()
    choice = input("메뉴를 선택하세요: ").strip()

    if choice == "1":
        add_prompt()
    elif choice == "2":
        show_prompt_list()
    elif choice == "3":
        delete_prompt()
    elif choice == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 입력하세요.")