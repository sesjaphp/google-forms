from rich.console import Console
from rich.table import Table

from forms.session import FormSession
from forms.scanner import scan_form
from ui.menu import collect_answers
from forms.filler import fill_form

console = Console()


def display_questions(questions):
    table = Table(title="Detected Questions")

    table.add_column("#")
    table.add_column("Title")
    table.add_column("Options")

    for i, q in enumerate(questions, start=1):
        table.add_row(str(i), q.title, ", ".join(q.options))

    console.print(table)


def run_once(session, url, questions):
    answers = collect_answers(questions)

    print("\nAnswers:")
    for k, v in answers.items():
        print(f"{k} → {v}")

    fill_form(session.page, questions, answers)


def main():
    console.print("[bold cyan]Google Form Bot (Safe Mode)[/bold cyan]")

    url = input("Form URL: ").strip()

    session = FormSession()
    session.start(url)

    questions = scan_form(session.page)

    display_questions(questions)

    while True:
        run_once(session, url, questions)

        again = input("\nSubmit again? (y/n): ").lower()
        if again != "y":
            break

        session.page.goto(url)
        session.page.wait_for_timeout(20)

    session.stop()


if __name__ == "__main__":
    main()
