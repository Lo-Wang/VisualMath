from manim import *

class Test(Scene):
    def construct(self):

        intro_text = Text("Тест на математическую \n         грамотность").scale(1.2)
        introdaction = Text("У вас будет 15 секунд на прочтение задачи \n        и записи её в математическом виде").scale(0.8)

        quest = Tex(r"Даны отрезки AB и CD, они пересекаются в точке L")
        quest_1 = Tex(r"Точка O находится на отрезке AE")
        quest_2 = Tex(r"В треугольнике JKL, прямая MN проходит через точку J и перпендикулярна стороне KL")

        answer_intro = Tex(r"Ответы").scale(2)

        answer_label = Tex(r"1) AB $\cap$ CD={L}").scale(1.5)
        answer_label_1 = Tex(r"2) O $\in$ AE ").scale(1.5)
        answer_label_2 = Tex(r"3) MN $\bot$ KL").scale(1.5)

        line = Line(4 * LEFT + 3*DOWN, 4 * RIGHT + 3*DOWN)


        self.wait()
        self.play(Write(intro_text))
        self.play(FadeOut(intro_text))
        self.play(Write(introdaction))
        self.wait(5)
        self.play(FadeOut(introdaction))

        self.play(Write(quest), Create(line), run_time=4)
        self.play(ShowPassingFlashWithThinningStrokeWidth(line.copy().set_color(RED), run_time=15, time_width=3))
        self.play(FadeOut(quest, line, shift=DOWN))
        
        self.play(Write(quest_1), Create(line), run_time = 3)
        self.play(ShowPassingFlashWithThinningStrokeWidth(line.copy().set_color(RED), run_time=15, time_width=3))
        self.play(FadeOut(quest_1, line, shift=DOWN))

        self.play(Write(quest_2), Create(line), run_time = 3)
        self.play(ShowPassingFlashWithThinningStrokeWidth(line.copy().set_color(RED), run_time=15, time_width=3))
        self.play(FadeOut(quest_2, line, shift=DOWN))

        self.play(Write(answer_intro))
        self.play(FadeOut(answer_intro))

        self.play(Write(answer_label))
        self.wait(2)
        self.play(FadeOut(answer_label, shift=DOWN))

        self.play( Write(answer_label_1))
        self.wait(2)
        self.play(FadeOut(answer_label_1, shift=DOWN))

        self.play(Write(answer_label_2))
        self.wait(2)
        self.play(FadeOut(answer_label_2, shift=DOWN))