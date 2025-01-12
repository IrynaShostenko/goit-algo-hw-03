import turtle


# Функція для малювання лінії Коха
def draw_koch_snowflake(t, order, level):
    if level == 0:
        t.forward(order)
    else:
        order /= 3.0
        draw_koch_snowflake(t, order, level - 1)  # Перша частина
        t.left(60)
        draw_koch_snowflake(t, order, level - 1)  # Верхній сегмент
        t.right(120)
        draw_koch_snowflake(t, order, level - 1)  # Нижній сегмент
        t.left(60)
        draw_koch_snowflake(t, order, level - 1)  # Остання частина


# Функція для створення фракталу «сніжинка Коха»
def koch_snowflake(order, level):
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.title("Сніжинка Коха")

    # Налаштування черепахи
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-order // 2, order // 3)
    t.pendown()

    # Малювання сніжинки
    for _ in range(3):
        draw_koch_snowflake(t, order, level)
        t.right(120)

    # Завершення програми
    t.hideturtle()
    screen.mainloop()


# Головна функція
def main():
    try:
        level = int(input("Введіть рівень рекурсії (рекомендується 0-5): "))
        if level < 0:
            print("Рівень рекурсії не може бути від'ємним!")
            return

        order = int(
            input("Введіть довжину сторони фракталу (рекомендується 300-600): ")
        )
        if order <= 0:
            print("Довжина сторони повинна бути додатною!")
            return

        koch_snowflake(order, level)

    except ValueError:
        print(
            "Будь ласка, введіть числові значення для рівня рекурсії та довжини сторони."
        )


if __name__ == "__main__":
    main()