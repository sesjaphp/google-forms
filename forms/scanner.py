from forms.models import Question


def scan_form(page) -> list[Question]:
    questions = []

    blocks = page.locator('[role="listitem"]')

    for i in range(blocks.count()):
        block = blocks.nth(i)

        radios = block.locator('[role="radio"]')

        if radios.count() == 0:
            continue

        title = f"Question {len(questions) + 1}"

        heading = block.locator('[role="heading"]').first
        if heading.count():
            title = heading.inner_text().strip()

        options = []

        for j in range(radios.count()):
            radio = radios.nth(j)

            label = (
                radio.get_attribute("aria-label")
                or radio.get_attribute("data-value")
                or f"Option {j+1}"
            )

            options.append(label)

        questions.append(
            Question(
                title=title,
                qtype="radio",
                options=options,
                locator=block,
            )
        )

    return questions
