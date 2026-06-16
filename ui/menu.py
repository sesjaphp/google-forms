def collect_answers(questions):
    answers = {}

    for q in questions:
        if q.qtype != "radio":
            continue

        print(f"\n{q.title}")

        for i, opt in enumerate(q.options):
            print(f"  [{i}] {opt}")

        while True:
            try:
                idx = int(input("Select option: "))
                if 0 <= idx < len(q.options):
                    answers[q.title] = q.options[idx]
                    break
            except ValueError:
                pass

    return answers
