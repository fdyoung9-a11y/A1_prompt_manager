# 프롬프트 데이터 저장
prompts = [
    {
        "title": "자기소개 작성",
        "content": "면접용 자기소개를 작성해줘.",
        "category": "면접",
        "favorite": False
    },
    {
        "title": "블로그 글쓰기",
        "content": "AI 기술 트렌드에 대한 블로그 글을 써줘.",
        "category": "글쓰기",
        "favorite": False
    },
    {
        "title": "영어 번역",
        "content": "이 문장을 자연스러운 영어로 번역해줘.",
        "category": "번역",
        "favorite": False
    }
]


def show_menu():
    print("\n=== A1 프롬프트 관리 프로그램 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 프롬프트 삭제")
    print("4. 카테고리별 조회")
    print("5. 즐겨찾기 추가/해제")
    print("6. 즐겨찾기 목록 보기")
    print("7. 종료")


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

    prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(prompt)
    print("프롬프트가 추가되었습니다.")


def show_prompt_list():
    print("\n[프롬프트 목록]")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        favorite_mark = "★" if prompt["favorite"] else ""
        print(f"{i}. {favorite_mark} 제목: {prompt['title']}")
        print(f"   내용: {prompt['content']}")
        print(f"   카테고리: {prompt['category']}")
        print("-" * 30)


def delete_prompt():
    print("\n[프롬프트 삭제]")

    if not prompts:
        print("삭제할 프롬프트가 없습니다.")
        return

    show_prompt_list()

    try:
        number = int(input("삭제할 프롬프트 번호를 입력하세요: "))
        if 1 <= number <= len(prompts):
            deleted = prompts.pop(number - 1)
            print(f"'{deleted['title']}' 프롬프트가 삭제되었습니다.")
        else:
            print("올바른 번호를 입력하세요.")
    except ValueError:
        print("숫자를 입력하세요.")


def show_prompts_by_category():
    print("\n[카테고리별 조회]")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    category = input("조회할 카테고리를 입력하세요: ").strip()
    if category == "":
        print("카테고리를 입력하세요.")
        return

    found = False
    for i, prompt in enumerate(prompts, start=1):
        if prompt["category"] == category:
            favorite_mark = "★" if prompt["favorite"] else ""
            print(f"{i}. {favorite_mark} 제목: {prompt['title']}")
            print(f"   내용: {prompt['content']}")
            print(f"   카테고리: {prompt['category']}")
            print("-" * 30)
            found = True

    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")


def toggle_favorite():
    print("\n[즐겨찾기 추가/해제]")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_prompt_list()

    try:
        number = int(input("즐겨찾기 설정/해제할 프롬프트 번호를 입력하세요: "))
        if 1 <= number <= len(prompts):
            prompts[number - 1]["favorite"] = not prompts[number - 1]["favorite"]

            if prompts[number - 1]["favorite"]:
                print("즐겨찾기에 추가되었습니다.")
            else:
                print("즐겨찾기에서 해제되었습니다.")
        else:
            print("올바른 번호를 입력하세요.")
    except ValueError:
        print("숫자를 입력하세요.")


def show_favorites():
    print("\n[즐겨찾기 목록]")

    favorite_prompts = [prompt for prompt in prompts if prompt["favorite"]]

    if not favorite_prompts:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(favorite_prompts, start=1):
        print(f"{i}. ★ 제목: {prompt['title']}")
        print(f"   내용: {prompt['content']}")
        print(f"   카테고리: {prompt['category']}")
        print("-" * 30)


def main():
    while True:
        show_menu()
        choice = input("메뉴 번호를 선택하세요: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_prompt_list()
        elif choice == "3":
            delete_prompt()
        elif choice == "4":
            show_prompts_by_category()
        elif choice == "5":
            toggle_favorite()
        elif choice == "6":
            show_favorites()
        elif choice == "7":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1~7 중에서 선택하세요.")


main()