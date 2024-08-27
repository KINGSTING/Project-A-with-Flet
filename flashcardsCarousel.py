import flet as ft


class Flashcard(ft.Container):
    def __init__(self, question, answer):
        super().__init__()
        self.question = question
        self.answer = answer
        self.showing_answer = False

        # Initial display is the question
        self.text = ft.Text(value=self.question, size=20, text_align=ft.TextAlign.CENTER)

        # Flashcard style
        self.padding = ft.padding.all(20)
        self.alignment = ft.alignment.center
        self.width = 300
        self.height = 200
        self.bgcolor = ft.colors.GREEN
        self.border_radius = 10
        self.content = self.text
        self.on_click = self.flip

    def flip(self, e):
        # Toggle between question and answer
        self.showing_answer = not self.showing_answer
        self.text.value = self.answer if self.showing_answer else self.question
        self.bgcolor = ft.colors.LIGHT_BLUE_100 if self.showing_answer else ft.colors.GREEN
        self.update()


# Global variable to store flashcards
flashcards = []


def show_add_flashcard_form(page: ft.Page):
    page.title = "Add Cards"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Function to handle button click
    def button_click(e):
        print(f"Question: {question_input.value}")
        print(f"Answer: {answer_input.value}")

    # Text fields
    question_input = ft.TextField(label="Question", width=300)
    answer_input = ft.TextField(label="Answer", width=300)

    # Button
    submit_button = ft.ElevatedButton(
        text="Submit",
        on_click=button_click,
        width=100
    )

    # Container with two textfields and a button
    container = ft.Container(
        content=ft.Column(
            controls=[
                question_input,
                answer_input,
                ft.Row(
                    controls=[submit_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        ),
        padding=ft.padding.all(20),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.LIGHT_BLUE_100,
        border_radius=10
    )

    # Add the container to the page
    page.add(container)


def show_flashcards(page: ft.Page):
    def update_flashcard():
        if current_index.current < len(flashcards):
            flashcard = Flashcard(flashcards[current_index.current]["question"],
                                  flashcards[current_index.current]["answer"])
            page.controls.clear()
            page.add(
                flashcard,
                ft.Row([prev_button, next_button], alignment=ft.MainAxisAlignment.CENTER),
            )
            page.update()
        else:
            page.controls.clear()
            page.add(ft.Text("No more flashcards!"))
            page.update()

    def next_flashcard(e):
        if current_index.current < len(flashcards) - 1:
            current_index.current += 1
            update_flashcard()

    def previous_flashcard(e):
        if current_index.current > 0:
            current_index.current -= 1
            update_flashcard()

    current_index = ft.Ref()
    current_index.current = 0

    next_button = ft.ElevatedButton(text="Next", on_click=next_flashcard)
    prev_button = ft.ElevatedButton(text="Previous", on_click=previous_flashcard)

    update_flashcard()


def show_home_page(page: ft.Page):
    def go_to_flashcards(e):
        page.controls.clear()
        show_flashcards(page)

    def open_add_flashcard_form(e):
        show_add_flashcard_form(page)

    page.title = "Home Page"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Home page UI Components
    title = ft.Text("Welcome to the Flashcard App", size=30, text_align=ft.TextAlign.CENTER)

    # Clickable container
    start_container = ft.Container(
        content=ft.Text("Start Flashcards", size=20, text_align=ft.TextAlign.CENTER),
        padding=ft.padding.all(20),
        alignment=ft.alignment.center,
        width=300,
        height=100,
        bgcolor=ft.colors.LIGHT_BLUE_200,
        border_radius=10,
        on_click=go_to_flashcards,
        border=ft.border.all(2, ft.colors.BLUE_600),  # Optional: add a border to make it more button-like
    )

    # Add Flashcard button
    add_flashcard_button = ft.ElevatedButton(text="Add Flashcard", on_click=open_add_flashcard_form)

    # Add components to the page
    page.add(
        title,
        start_container,
        add_flashcard_button
    )


def main(page: ft.Page):
    # Show home page when the app starts
    show_home_page(page)


ft.app(target=main)
