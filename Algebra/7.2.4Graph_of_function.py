from manim import *

class gaf(MovingCameraScene):
    def construct(self):  

        info_text = Tex(r"\huge$y = \frac{7}{x+4}$")
        self.play(FadeIn(info_text))
        self.wait(1.5)
        self.play(FadeOut(info_text))

        table_1 = Table([["X","-3","-2","-1","0","1","2","3"], ["Y","7","3,5","7/3","1,75","1,4","7/6","1"]]).scale(0.7)
        self.play(Write(table_1), run_time=3)
        self.wait(1)
        self.play(Unwrite(table_1), run_time=3)
        
        number_plane_scaled = Axes(
            x_range=[-8, 8, 1],  
            y_range=[0, 8, 1]   
        )
        self.play(Create(number_plane_scaled), run_time=5)
        self.wait(1)

        dot_1 = Dot(number_plane_scaled.coords_to_point(-3, 7))
        dot_2 = Dot(number_plane_scaled.coords_to_point(-2, -3.5))
        dot_3 = Dot(number_plane_scaled.coords_to_point(-1, 2.3))
        dot_4 = Dot(number_plane_scaled.coords_to_point(0, 1.75))
        dot_5 = Dot(number_plane_scaled.coords_to_point(1, 1.4))
        dot_6 = Dot(number_plane_scaled.coords_to_point(2, 1.17))
        dot_7 = Dot(number_plane_scaled.coords_to_point(3, 1))
        group = VGroup(dot_1, dot_2, dot_3, dot_4, dot_5, dot_6, dot_7)
        
        self.play(Create(group), run_time=2)
        self.wait(1)