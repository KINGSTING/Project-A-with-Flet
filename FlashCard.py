import flet as ft


class Flashcard(ft.Container):
    def __init__(self, question, answer):
        super().__init__()
        self.question = question
        self.answer = answer
        self.showing_answer = False

        # Initial display is the question
        self.text = ft.Text(value=self.question)

        # Container to display the text
        self.content = self.text

        # Make the flashcard clickable
        self.on_click = self.flip

    def flip(self, e):
        # Toggle between question and answer
        self.showing_answer = not self.showing_answer
        self.text.value = self.answer if self.showing_answer else self.question
        self.update()


def main(page: ft.Page):
    page.title = "Flashcard App"

    # Create a column to hold the flashcards
    column = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    # List of flashcards
    flashcards = [
        Flashcard("What is the capital of France?", "Paris"),
        Flashcard("What is 2 + 2?", "4"),
        Flashcard("What is the boiling point of water?", "100°C")
    ]

    # Add flashcards to the column
    for card in flashcards:
        column.controls.append(card)

    # Add the column to the page
    page.add(column)


ft.app(target=main)
