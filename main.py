from flet import ElevatedButton, Page, AppBar, Text, TextField, SnackBar, ScrollMode, colors, app
from StringCalculator import SolveMathProblem

def main(page: Page):

    def button_clicked(e):

        problem = tf.value

        if problem == "":
            show_snack_bar("Введите арифметическое выражение")
            page.update()
            return

        try:
            result = SolveMathProblem(problem)
        except ZeroDivisionError:
            show_snack_bar("Деление на ноль!")
            page.update()
            return

        if str(t.value) == "None":
            result_list = problem + "=" + str(result) + "\n"
        else:
            result_list = str(t.value) + problem + "=" + str(result) + "\n"

        t.value = result_list

        page.update()

    def show_snack_bar(msg):
        snack_bar = SnackBar(content=Text(msg), bgcolor=colors.RED)
        page.snack_bar = snack_bar
        snack_bar.open = True

    t = Text(size=20, selectable=True)
    tf = TextField(label="Введите арифметическое выражение")
    b = ElevatedButton(text="ВЫЧИСЛИТЬ", on_click=button_clicked)
    ab = AppBar(title=Text("Калькулятор"), bgcolor=colors.LIME_100)

    page.add(ab, tf, b, t)
    page.scroll = ScrollMode.ADAPTIVE
    page.title = "Строковый Калькулятор"
    page.update()

app(main)
