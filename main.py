import asyncio
from rich.console import Console
from forms.session import FormSession
from forms.scanner import scan_form
from ui.menu import collect_answers
from forms.filler import fill_form

console = Console()

async def submit_once(url, questions, answers):
    session = FormSession()
    await session.start(url)
    await fill_form(session.page, questions, answers)
    await session.stop()

async def main():
    console.print("[bold cyan]google spam[/bold cyan]")
    url = input("Form URL: ").strip()

    temp_session = FormSession()
    await temp_session.start(url)
    questions = await scan_form(temp_session.page)
    await temp_session.stop()

    if not questions:
        console.print("[bold red]No questions detected. Exiting.[/bold red]")
        return

    answers = collect_answers(questions)

    count = int(input("\nNumber of submissions: ").strip())
    concurrency = int(input("Concurrency (how many at once): ").strip())

    semaphore = asyncio.Semaphore(concurrency)

    async def sem_submit(i):
        async with semaphore:
            console.print(f"[yellow]Submitting #{i+1}...[/yellow]")
            await submit_once(url, questions, answers)
            console.print(f"[green]Done #{i+1}[/green]")

    tasks = [sem_submit(i) for i in range(count)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
