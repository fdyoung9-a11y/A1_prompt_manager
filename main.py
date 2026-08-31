import json
import os

DATA_FILE = "prompts.json"
EXPORT_DIR = "exports"


def load_prompts():
    """JSON 파일에서 프롬프트를 불러옵니다."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            print("저장된 파일을 읽는 중 문제가 발생했습니다. 기본 데이터로 시작합니다.")

    # 파일이 없거나 읽기 실패 시 기본 프롬프트 제공
    default_prompts = [
        {
            "title": "영어 문장 교정",
            "content": "이 문장을 자연스럽고 정확한 영어로 고쳐줘.",
            "category": "공부",
            "favorite": False
        },
        {
            "title": "자기소개 작성",
            "content": "면접용 1분 자기소개를 작성해줘.",
            "category": "면접",
            "favorite": True
        },
        {
            "title": "블로그 글 아이디어",
            "content": "AI와 생산성을 주제로 블로그 글 아이디어 5개를 제안해줘.",
            "category": "글쓰기",
            "favorite": False
        }
    ]
    save_prompts(default_prompts)
    return default_prompts


def save_prompts(prompts):
    """프롬프트를 JSON 파일에 저장합니다."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)


def show_menu():
    """메뉴를 출력합니다."""
    print("\n=== A1 프롬프트 관리 프로그램 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 프롬프트 삭제")
    print("4. 카테고리별 조회")
    print("5. 즐겨찾기 추가/해제")
    print("6. 즐겨찾기 프롬프트 목록 조회")
    print("7. 카테고리별 Markdown 내보내기")
    print("8. 종료")


def print_prompt(prompt, index):
    """프롬프트 1개를 보기 좋게 출력합니다."""
    favorite_mark = "★" if prompt["favorite"] else " "
    print(f"\n[{index}] {favorite_mark} {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"내용: {prompt['content']}")


def view_prompts(prompts):
    """전체 프롬프트 목록을 출력합니다."""
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    print("\n=== 전체 프롬프트 목록 ===")
    for i, prompt in enumerate(prompts, 1):
        print_prompt(prompt, i)


def add_prompt(prompts):
    """새 프롬프트를 추가합니다."""
    print("\n=== 프롬프트 추가 ===")
    title = input("제목을 입력하세요: ").strip()
    content = input("내용을 입력하세요: ").strip()
    category = input("카테고리를 입력하세요: ").strip()

    if not title or not content or not category:
        print("제목, 내용, 카테고리는 모두 입력해야 합니다.")
        return

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)
    save_prompts(prompts)
    print("프롬프트가 추가되었습니다.")


def delete_prompt(prompts):
    """번호를 입력받아 프롬프트를 삭제합니다."""
    if not prompts:
        print("삭제할 프롬프트가 없습니다.")
        return

    view_prompts(prompts)

    try:
        index = int(input("\n삭제할 프롬프트 번호를 입력하세요: "))
        if 1 <= index <= len(prompts):
            deleted = prompts.pop(index - 1)
            save_prompts(prompts)
            print(f"'{deleted['title']}' 프롬프트가 삭제되었습니다.")
        else:
            print("올바른 번호를 입력하세요.")
    except ValueError:
        print("숫자를 입력해야 합니다.")


def view_by_category(prompts):
    """카테고리별로 프롬프트를 조회합니다."""
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    category = input("\n조회할 카테고리를 입력하세요: ").strip()

    if not category:
        print("카테고리를 입력해야 합니다.")
        return

    found = [prompt for prompt in prompts if prompt["category"] == category]

    if not found:
        print(f"'{category}' 카테고리의 프롬프트가 없습니다.")
        return

    print(f"\n=== '{category}' 카테고리 프롬프트 목록 ===")
    for i, prompt in enumerate(found, 1):
        print_prompt(prompt, i)


def toggle_favorite(prompts):
    """즐겨찾기 상태를 추가/해제합니다."""
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    view_prompts(prompts)

    try:
        index = int(input("\n즐겨찾기 추가/해제할 프롬프트 번호를 입력하세요: "))
        if 1 <= index <= len(prompts):
            prompts[index - 1]["favorite"] = not prompts[index - 1]["favorite"]
            save_prompts(prompts)

            if prompts[index - 1]["favorite"]:
                print("즐겨찾기에 추가되었습니다.")
            else:
                print("즐겨찾기가 해제되었습니다.")
        else:
            print("올바른 번호를 입력하세요.")
    except ValueError:
        print("숫자를 입력해야 합니다.")


def view_favorites(prompts):
    """즐겨찾기된 프롬프트만 조회합니다."""
    favorites = [prompt for prompt in prompts if prompt["favorite"]]

    if not favorites:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    print("\n=== 즐겨찾기 프롬프트 목록 ===")
    for i, prompt in enumerate(favorites, 1):
        print_prompt(prompt, i)


def safe_filename(name):
    """파일명으로 사용할 수 없거나 불편한 문자를 치환합니다."""
    invalid_chars = '\\/:*?"<>|'
    for char in invalid_chars:
        name = name.replace(char, "_")
    return name.strip()


def export_to_markdown(prompts):
    """카테고리별로 Markdown 파일을 생성합니다."""
    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    os.makedirs(EXPORT_DIR, exist_ok=True)

    categories = {}
    for prompt in prompts:
        category = prompt["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(prompt)

    for category, items in categories.items():
        filename = safe_filename(category) + ".md"
        filepath = os.path.join(EXPORT_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(f"# {category} 프롬프트 모음\n\n")

            for i, prompt in enumerate(items, 1):
                file.write(f"## {i}. {prompt['title']}\n\n")
                file.write(f"**내용**\n\n{prompt['content']}\n\n")
                file.write(f"- 카테고리: {prompt['category']}\n")
                file.write(f"- 즐겨찾기: {'예' if prompt['favorite'] else '아니오'}\n\n")
                file.write("---\n\n")

    print(f"카테고리별 Markdown 파일이 '{EXPORT_DIR}' 폴더에 저장되었습니다.")


def main():
    prompts = load_prompts()

    while True:
        show_menu()
        choice = input("원하는 메뉴 번호를 입력하세요: ").strip()

        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            view_prompts(prompts)
        elif choice == "3":
            delete_prompt(prompts)
        elif choice == "4":
            view_by_category(prompts)
        elif choice == "5":
            toggle_favorite(prompts)
        elif choice == "6":
            view_favorites(prompts)
        elif choice == "7":
            export_to_markdown(prompts)
        elif choice == "8":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1~8 사이의 번호를 입력하세요.")


if __name__ == "__main__":
    main()