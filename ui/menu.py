def collect_answers(questions):
    answers = {}
    for q in questions:
        print(f"\n{q.title}")
        for i, opt in enumerate(q.options):
            print(f"  [{i}] {opt}")

        while True:
            try:
                choice = input(f"Select option for '{q.title}' (or press Enter for random): ").strip()
                if not choice:
                    import random
                    answers[q.title] = random.choice(q.options)
                    print(f"  Selected: {answers[q.title]} (Random)")
                    break

                idx = int(choice)
                if 0 <= idx < len(q.options):
                    answers[q.title] = q.options[idx]
                    print(f"  Selected: {answers[q.title]}")
                    break
            except ValueError:
                print("  Invalid input. Please enter a number or press Enter.")
    return answers
