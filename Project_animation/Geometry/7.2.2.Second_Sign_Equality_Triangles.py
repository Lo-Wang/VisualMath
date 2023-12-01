from manim import *

class sset(MovingCameraScene):
    def construct(self):
        intro_text = Text("Второй признак подобия \n       треугольников").scale(1.2)
        info_text = Tex(r"Если сторона и два угола прилежащей к ней одного " +
                          r"треугольника соответственно равны стороне " +
                          r"и двум углам прилежащей к ней другого " +
                          r"треугольника, то такие треугольники равны", tex_to_color_map={"две стороны и угол между ними": ORANGE}).scale(0.8)
        
        info_text_1 = Tex(r"\begin{justify}Докажем что $\triangle$1 = $\triangle$2\end{justify}").move_to(2* DOWN)

        info_text_2 = Tex(r"\begin{justify} Наложим два треугольника так, чтобы вершина $A$ " + 
                          r"\\совместилась с $A_1$, $AB$ с $A_1B_1$, $C$ по одну сторону с $C_1$ \end{justify}").move_to(np.array([0,-2,0])).scale(0.7)
        
        info_text_3 = Tex(r"\begin{justify}Так как $\angle$$A$ = $\angle$$A_1$ и $\angle$$B$ = $\angle$$B_1$" +
                          r"\\ то, $AC$ наложится на $A_1$$C_1$ и $BC$ на $B_1C_1$ \end{justify}").move_to(np.array([0,-2,0])).scale(0.7)
        info_text_3 = Tex(r"\begin{justify}$C$ - общая точка $AC$ и $BC$ $\Rightarrow$ Совмещается точка $C$ и $C_1$\end{justify}").move_to(np.array([0,-2,0])).scale(0.7)
        info_text_4 = Tex(r"\begin{justify}Следовательно, если совместились все вершины и прямые." +
                           r"\\ то, $\triangle$1 = $\triangle$2\end{justify}").move_to(np.array([0,-2,0])).scale(0.7)
        
        triangle = Polygon([-4, -1, 0], [-6, 1, 0], [-3, 3, 0],color = BLUE)
        dot_1 = Dot(4 * LEFT + DOWN)
        dot_2 = Dot(6 * LEFT + UP)
        dot_3 = Dot(3 * LEFT + 3 * UP)
        label_1 = always_redraw(lambda: MathTex("A").next_to(dot_1, LEFT))
        label_2 = always_redraw(lambda: MathTex("C").next_to(dot_2, LEFT))
        label_3 = always_redraw(lambda: MathTex("B").next_to(dot_3, RIGHT))
        line_1 = Line(4 * LEFT + 1 * DOWN, 6 * LEFT + UP, color= BLUE)
        line_2 = Line(4 * LEFT + 1 * DOWN, 3 * LEFT + 3 * UP, color = WHITE)
        line_3 = Line(6 * LEFT + UP, 3 * LEFT + 3 * UP)
        angle = Angle(line_2, line_1, radius=0.7)
        angle_1 = Angle(line_3, line_2, quadrant=(-1, -1), radius=0.7)

        triangle_group = VGroup(triangle, line_1, line_2, line_3, angle, angle_1, dot_1, dot_2, dot_3)


        triangle_1 = Polygon([-4, -1, 0], [-6, 1, 0], [-3, 3, 0], color=ORANGE)
        dot_4 = Dot(4 * LEFT + DOWN)
        dot_5 = Dot(6 * LEFT + UP)
        dot_6 = Dot(3 * LEFT + 3 * UP)
        label_4 = always_redraw(lambda: MathTex("A_1").next_to(dot_4, UP))
        label_5 = always_redraw(lambda: MathTex("C_1").next_to(dot_5, RIGHT))
        label_6 = always_redraw(lambda: MathTex("B_1").next_to(dot_6, DOWN))
        line_4 = Line(4 * LEFT + 1 * DOWN, 6 * LEFT + UP, color = ORANGE)
        line_5 = Line(4 * LEFT + 1 * DOWN, 3 * LEFT + 3 * UP, color = ORANGE)
        line_6 = Line(6 * LEFT + UP, 3 * LEFT + 3 * UP)
        angle_3 = Angle(line_4, line_6, quadrant=(-1,1), radius=0.7)
        angle_4 = Angle(line_6, line_5, quadrant=(-1, -1), radius=0.7)

        triangle_group_1 = VGroup(triangle_1, line_4, line_5, line_6, angle_3, angle_4, dot_4, dot_5, dot_6).move_to(np.array([3,0,0])).rotate(40)

        dot_group_1 = VGroup(dot_1, dot_4)
        dot_group_2 = VGroup(dot_2, dot_6)
        two_angle = VGroup(angle, angle_1)
        two_side = VGroup(line_1, line_3)
        two_side_1 = VGroup(line_2, line_4)
        label_group = VGroup(label_1, label_2, label_3, label_4, label_5, label_6)

        # Заголовок
        self.wait(0.5)
        self.play(FadeIn(intro_text))
        self.play(FadeOut(intro_text))

        # Теория
        self.wait(0.5)
        self.play(FadeIn(info_text))
        self.wait(6)
        self.play(FadeOut(info_text))

        # Треугольник
        self.wait(0.5)
        self.play(FadeIn(triangle_group, triangle_group_1, label_group), run_time=2)

        self.wait()
        
        # Доказательство
        self.wait(0.5)
        self.play(FadeIn(info_text_1))
        self.wait(3)
        self.play(TransformMatchingShapes(info_text_1, info_text_2))
        self.wait(3)
        self.play(Indicate(dot_group_1, scale_factor=1.03),Indicate(dot_group_2, scale_factor=1.03), run_time=3)
        self.wait(3)
        self.play(TransformMatchingShapes(info_text_2, info_text_3))
        self.wait(3)
        self.play(Indicate(two_side, scale_factor=1.03), run_time=3)
        self.wait(0.1)
        self.play(Indicate(two_side_1, scale_factor=1.02), run_time=3)
        self.play(Indicate(dot_group_1, scale_factor=1.02), Indicate(dot_group_2, scale_factor=1.02), run_time=2)
        self.wait(2)
        self.play(TransformMatchingShapes(info_text_3, info_text_4))
        self.play(Indicate(triangle, scale_factor=1.02), Indicate(triangle_1, scale_factor=1.02), run_time=2)
        self.play(FadeOut(label_group))
        self.wait(1)
        self.play(ApplyMethod(triangle_group.shift, 4 * RIGHT + 0.75* DOWN))
        self.play(ApplyMethod(triangle_group.rotate, 20))
        self.play(ApplyMethod(triangle_group_1.shift, -2.8 * RIGHT + 0.7* UP))
        self.play(ApplyMethod(triangle_group_1.rotate, -20))

        self.play(FadeOut(triangle_group, triangle_group_1, info_text_4, shift=DOWN))