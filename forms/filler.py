def fill_form(page, questions, answers):
    print("\nFilling form...\n")

    for q in questions:
        if q.qtype != "radio":
            continue

        answer = answers.get(q.title)

        if not answer:
            continue

        radio = q.locator.locator(
            f'[role="radio"][data-value="{answer}"]'
        )

        if radio.count():
            radio.first.click()

    page.wait_for_timeout(10)

    submit = page.locator(
        'div[role="button"]:has-text("Prześlij"), '
        'div[role="button"]:has-text("Submit")'
    )

    if submit.count():
        submit.first.click()
        print("Submitted.")
    else:
        print("Submit not found.")

    page.wait_for_timeout(10)

    page.go_back()
    page.wait_for_timeout(10)
