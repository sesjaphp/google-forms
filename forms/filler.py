async def fill_form(page, questions, answers):
    for q in questions:
        if q.qtype != "radio":
            continue

        answer = answers.get(q.title)
        if not answer:
            continue

        question_block = page.locator(f'[role="listitem"]:has-text("{q.title}")')
        if await question_block.count():
            radio = question_block.locator(f'[role="radio"][data-value="{answer}"], [role="radio"][aria-label="{answer}"]').first
            if await radio.count():
                await radio.click()

    submit = page.locator('div[role="button"]:has-text("Prześlij"), div[role="button"]:has-text("Submit")').first
    if await submit.count():
        await submit.click()
        await page.wait_for_load_state('networkidle')
