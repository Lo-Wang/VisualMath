from manim import *

class bgi(Scene):
    def construct(self):

        intro_text = Text("Обозначения").scale(1.5)
        dot = Dot(LEFT, 0.12, color=WHITE, z_index=1).move_to(np.array([-1, -1, 0]))
        dot_1 = Dot(LEFT, 0.12, color=WHITE, z_index=1).move_to(np.array([1, 1, 0]))
        dot_2 = Dot(LEFT, 0.12, color=WHITE, z_index=1).move_to(np.array([2, -1, 0]))
        label = always_redraw(lambda: MathTex("A").next_to(dot, UP))
        label_1 = always_redraw(lambda: MathTex("B").next_to(dot_1, UP))
        label_11 = always_redraw(lambda: MathTex(r"\beta").next_to(dot, UP))
        label_2 = always_redraw(lambda: MathTex("C").next_to(dot_2, 0.6 * UP + 0.2 * RIGHT))
        line = Line(LEFT + DOWN, RIGHT + UP)
        line_1 = Line(LEFT + DOWN, 2* RIGHT + DOWN)
        line_2 = Line(2* RIGHT + DOWN, RIGHT + UP)
        angle = Angle(line_1, line, radius=0.8)
        angle_info = always_redraw(lambda: Tex(r"$\alpha$").next_to(angle, 0.7 * RIGHT))
        sin = FunctionGraph(lambda x: np.sin(x), x_range=[-6.5, 6.5]).set_stroke(YELLOW, 3)
        sin_text = Text("sin(x)").move_to(np.array([-1.5, 1.5 , 0]))
        cos = FunctionGraph(lambda x: np.cos(x), x_range=[-6.5, 6.5]).set_stroke(RED, 3)
        cos_text = Text("cos(x)").move_to(np.array([-1.5, 1.5 , 0]))
        info_text = Text("A - это точка").move_to(np.array([0, -2, 0]))
        info_text_1 = Tex(r"$\beta$ - луч").move_to(np.array([0, -2, 0]))
        info_text_2 = Text("AB - отрезок").move_to(np.array([0, -2, 0]))
        info_text_3 = Tex(r"$\angle$ BAC - угол \\ $\angle$$\alpha$ - тоже обозначение угла").move_to(np.array([0, -2, 0]))
        info_text_4 = Tex(r"$\triangle$ ABC - треугольник").move_to(np.array([0, -2, 0]))

        self.wait(0.5)
        self.play(Write(intro_text))
        self.wait(0.5)
        self.play(FadeOut(intro_text))

        self.play(FadeIn(dot, label), run_time = 1)
        self.wait(0.5)
        self.play(Write(info_text), run_time = 1.5)

        self.wait(0.5)
        self.play(Create(line))
        self.play(ReplacementTransform(info_text, info_text_1), FadeOut(label), FadeIn(label_11))
        self.wait()
        self.play(FadeOut(label_11), FadeIn(dot_1), FadeIn(label))
        self.wait()

        self.play(FadeIn(label_1), ReplacementTransform(info_text_1, info_text_2))
        self.wait(2)
        self.play(Create(line_1), Create(dot_2),Create(label_2), Create(angle))
        self.play(ReplacementTransform(info_text_2, info_text_3), FadeIn(angle_info))
        self.wait(2)

        self.play(ReplacementTransform(info_text_3, info_text_4), Create(line_2))
        self.wait(4)
        self.play(FadeOut(dot, dot_1, dot_2, label, label_1, label_2, line, line_1, line_2, angle, angle_info, info_text_4, shift=DOWN))
        self.wait()
        



