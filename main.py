# 프롬프트 관리 프로그램

# 프롬프트 관리 프로그램

prompts = []

while True:
    print("\n=== 프롬프트 관리 프로그램 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 종료")

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        prompt = input("저장할 프롬프트를 입력하세요: ")
        if prompt.strip() == "":
            print("빈 프롬프트는 저장할 수 없습니다.")
        else:
            prompts.append(prompt)
            print("프롬프트가 저장되었습니다.")

    elif choice == "2":
        print("\n저장된 프롬프트 목록")
        if len(prompts) == 0:
            print("아직 저장된 프롬프트가 없습니다.")
        else:
            for i, prompt in enumerate(prompts, start=1):
                print(f"{i}. {prompt}")

    elif choice == "3":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 선택입니다. 다시 입력하세요.")