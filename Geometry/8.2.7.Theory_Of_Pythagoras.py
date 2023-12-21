from manim import *

class Pythagoras(Scene): 
    def construct(self):
        # Фигуры и лейблы    
        intro_text = Text("Теорема Пифагора").scale(1.5)    
        triangle = Polygon(4 * UP, ORIGIN, 3 * RIGHT)
        triangle.set_stroke(YELLOW, 2.5).set_z_index(1)
        square = VGroup(Square(3), Square(4), Square(5))
        square.set_opacity(0.12) 
        angle = Elbow(width=0.4).set_stroke(YELLOW, 1.5)        
        theorem = MathTex("c^2 = a^2 + b^2")        
        label = MathTex("a", "b", "c")        

        # Расположение 
        square[0].next_to(triangle, DOWN, buff=0)
        square[1].next_to(triangle, LEFT, buff=0)      
        square[2].shift(3.5 * UR).rotate(np.arctan(3 / 4)) 
        theorem.move_to(square[2].get_center()) 
        label[0].next_to(triangle, DOWN, buff=0.15)
        label[1].next_to(triangle, LEFT, buff=0.15)
        label[2].next_to(2 * UP + 1.5 * RIGHT, UR, buff=0.15)  
        picture = VGroup(triangle, square, label, angle, theorem)
        picture.move_to(ORIGIN).scale(0.75)    

        # Анимация
        self.wait(0.5)
        self.play(Write(intro_text))
        self.wait(0.5)
        self.play(FadeOut(intro_text))
        self.play(Create(triangle), run_time=2)  
        self.play(GrowFromCenter(angle))      
        self.play(GrowFromCenter(label))        
        self.play(FadeIn(square[0], shift=UP))
        self.play(FadeIn(square[1], shift=RIGHT))
        self.play(FadeIn(square[2], shift=LEFT + 0.75 * DOWN))
        self.play(Write(theorem), run_time=2)  
        box = SurroundingRectangle(theorem, buff=0.2)
        box.set_stroke(YELLOW, 2)       
        self.play(ShowPassingFlash(box), run_time=2) 
        self.wait(3)