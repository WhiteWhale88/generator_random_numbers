"""Генератор распределений"""

import numpy as np
import dearpygui.dearpygui as dpg


def create_graffics():
    """Создание графиков"""

    def add_data(name_discrib, numbers):
        """Генерация данных"""
        hist, _ = np.histogram(numbers, count_inter)
        frequency = [h / count_num for h in hist]
        datax, datay = np.array(range(count_inter)), frequency

        dpg.set_value(f"graff_{name_discrib}", [datax, datay])
        dpg.configure_item(f"numbers_{name_discrib}", items=list(np.around(numbers, decimals=5)))

    try:
        count_num = int(dpg.get_value("count_num"))
        count_inter = int(dpg.get_value("count_inter"))
        mean = float(dpg.get_value("mean"))
        sigma = float(dpg.get_value("sigma"))
        lambd = float(dpg.get_value("lambd"))
        alpha = float(dpg.get_value("alpha"))
        beta = float(dpg.get_value("beta"))
    except ValueError as e:
        print(e)
        return

    add_data("norm", np.random.normal(mean, sigma, count_num))
    add_data("exp", np.random.exponential(lambd, count_num))
    add_data("gamma", np.random.gamma(alpha, beta, count_num))


if __name__ == "__main__":
    dpg.create_context()

    with dpg.font_registry():
        with dpg.font(r"fonts\caviar-dreams.ttf", 20) as font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

    with dpg.window(tag="Primary Window"):
        with dpg.group(horizontal=True):
            with dpg.group():
                dpg.add_text("Общие параметры генерации и отображения")
                dpg.add_input_text(
                    default_value=10000,
                    label="Количество чисел",
                    width=100,
                    tag="count_num",
                    decimal=True,
                    callback=create_graffics,
                )
                dpg.add_input_text(
                    default_value=10,
                    label="Количество интервалов",
                    width=100,
                    tag="count_inter",
                    decimal=True,
                    callback=create_graffics,
                )
                dpg.add_text("Параметры нормального распределения")
                dpg.add_input_text(
                    default_value=10,
                    label="Т среднее (среднее значение)",
                    width=100,
                    tag="mean",
                    decimal=True,
                    callback=create_graffics,
                )
                dpg.add_input_text(
                    default_value=3,
                    label="Сигма (стандартное отклонение)",
                    width=100,
                    tag="sigma",
                    decimal=True,
                    callback=create_graffics,
                )
                dpg.add_text("Параметры экспоненциального распределения")
                dpg.add_input_text(
                    default_value=20,
                    label="Лямбда (масштаб)",
                    width=100,
                    tag="lambd",
                    decimal=True,
                    callback=create_graffics,
                )
                dpg.add_text("Параметры гамма-распределения")
                dpg.add_input_text(
                    default_value=10,
                    label="Альфа (форма)",
                    width=100,
                    tag="alpha",
                    decimal=True,
                    callback=create_graffics,
                )
                dpg.add_input_text(
                    default_value=3,
                    label="Бета (масштаб)",
                    width=100,
                    tag="beta",
                    decimal=True,
                    callback=create_graffics,
                )

            with dpg.group():
                dpg.add_text("Сгенерированные числа")
                with dpg.group(horizontal=True):
                    dpg.add_listbox(
                        items=[], tag="numbers_norm", width=200, num_items=10
                    )
                    dpg.add_listbox(
                        items=[], tag="numbers_exp", width=200, num_items=10
                    )
                    dpg.add_listbox(
                        items=[], tag="numbers_gamma", width=200, num_items=10
                    )

        dpg.add_button(label="Сгенерировать", callback=create_graffics)
        dpg.add_text("Графики относительных частот")
        with dpg.group(horizontal=True):
            with dpg.plot(label="Нормальное распределение", width=400, tag="plot_norm"):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="Номер интервала")
                dpg.add_plot_axis(dpg.mvYAxis, label="Частота", tag="y_axis1")
                dpg.add_line_series(
                    [], [], label="", parent="y_axis1", tag="graff_norm"
                )

            with dpg.plot(
                label="Экспоненциальное распределение", width=400, tag="plot_exp"
            ):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="Номер интервала")
                dpg.add_plot_axis(dpg.mvYAxis, label="Частота", tag="y_axis2")
                dpg.add_line_series([], [], label="", parent="y_axis2", tag="graff_exp")

            with dpg.plot(label="Гамма-распределение", width=400, tag="plot_gamma"):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="Номер интервала")
                dpg.add_plot_axis(dpg.mvYAxis, label="Частота", tag="y_axis3")
                dpg.add_line_series(
                    [], [], label="", parent="y_axis3", tag="graff_gamma"
                )

        dpg.bind_font(font)
        create_graffics()

    dpg.create_viewport(title="Generator", width=1300, height=760)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
