from forms.models import Question

async def scan_form(page) -> list[Question]:
    questions = []
    blocks = await page.locator('[role="listitem"]').all()

    for block in blocks:
        radios = await block.locator('[role="radio"]').all()
        if not radios:
            continue

        title = "Question"
        heading = block.locator('[role="heading"]').first
        if await heading.count():
            title = await heading.inner_text()

        options = []
        for radio in radios:
            label = (
                await radio.get_attribute("aria-label")
                or await radio.get_attribute("data-value")
                or "Option"
            )
            options.append(label.strip())

        questions.append(
            Question(
                title=title.strip(),
                qtype="radio",
                options=options
            )
        )

    return questions
