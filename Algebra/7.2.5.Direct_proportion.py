from manim import *
# На правку
# Необходимо добавить  текстовое описание с объяснениями для школьников
class gaf(MovingCameraScene):
    def construct(self):  
        
        text1 = Text("Прямая пропорциональность", font_size=28)
        text2 = Text("k - коэффициент пропорциональности", font_size=28)
        v_group = VGroup(text1, text2)
        v_group.arrange(DOWN, buff=0.5)
        v_group.set_height(2)

        self.play(FadeIn(v_group))
        self.wait(1.5)
        self.play(FadeOut(v_group))
       

        number_plane_scaled = Axes(
            x_range=[-4, 4, 1], 
            y_range=[-4, 4, 1]  
        )
        self.play(Create(number_plane_scaled), run_time=5)
        self.wait(1)

        dot_1 = Dot(number_plane_scaled.coords_to_point(-2, -2))
        dot_2 = Dot(number_plane_scaled.coords_to_point(-1, -1))
        dot_3 = Dot(number_plane_scaled.coords_to_point(0, 0))
        dot_4 = Dot(number_plane_scaled.coords_to_point(1, 1))
        dot_5 = Dot(number_plane_scaled.coords_to_point(2, 2))

        group = VGroup(dot_1, dot_2, dot_3, dot_4, dot_5)
        line = Line(dot_1, dot_5)
        self.play(Create(group), Create(line), run_time=2)
        self.wait(1)
        
        legend = MathTex("y=kx, k>0")
        legend.next_to(line, direction=UP + RIGHT)
        self.play(Write(legend))
        self.wait(1)

        dot_11 = Dot(number_plane_scaled.coords_to_point(-2, 2), color=RED)
        dot_12 = Dot(number_plane_scaled.coords_to_point(-1, 1), color=RED)
        dot_13 = Dot(number_plane_scaled.coords_to_point(0, 0), color=RED)
        dot_14 = Dot(number_plane_scaled.coords_to_point(1, -1), color=RED)
        dot_15 = Dot(number_plane_scaled.coords_to_point(2, -2), color=RED)
        group1 = VGroup(dot_11, dot_12, dot_13, dot_14, dot_15)
        line1 = Line(dot_11, dot_15, color=RED)
        self.play(Create(group1), Create(line1), run_time=2)
        self.wait(1)
        
        legend1 = MathTex("y=kx, k<0", color = RED)
        legend1.next_to(line1, direction=DOWN + RIGHT)
        self.play(Write(legend1))
        self.wait(1)

       