

![logo](https://media.discordapp.net/attachments/1150438545748656179/1180099686149935184/Intro_fro_rdmd_1.png?ex=657c307a&is=6569bb7a&hm=bfe6c184eac1607b341401bf3225f8e20294962764fa28d48eed3b5b9d721812&=&format=webp&quality=lossless&width=1202&height=676)

![Static Badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue&labelColor=FFD43B)
![Static Badge](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![Static Badge](https://img.shields.io/badge/LaTeX-47A141?style=for-the-badge&logo=LaTeX&logoColor=white)
![Static Badge](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Static Badge](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Static Badge](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Static Badge](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)
![Static Badge](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Static Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Static Badge](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
---
# Оглавление
- [Оглавление](#оглавление)
- [Быстрый Старт](#быстрый-старт)
- [Сайт](#сайт)
- [Дизайн](#дизайн)
- [Анимации](#анимации)
- [Интерактивная область](#интерактивная-область)


# Быстрый Старт

Проект создан для помощи в понимании математике: визуализация теорем, наглядного решения задач и интерактивной области для самостоятельного взаимодействия с геометрическими объектами.

В данный момент наша команда реализует программу по алгебре и геометрии для 7-9 класса.

Далее возможно расширение по математике вплоть до отдельных разделов высшей математике, а так же добавление новых предметов, например, физики и химии.


# Сайт

Сайт разбит на мини-приложения т.к джанго подразумевает разбиение на приложения.

На данный момент три приложения - [algebra](https://github.com/Lo-Wang/VisualMath/tree/main/algebra), [geometry](https://github.com/Lo-Wang/VisualMath/tree/main/geometry), [main](https://github.com/Lo-Wang/VisualMath/tree/main/main).
```
Путь Algebra - VisualMath/tree/main/algebra
Путь Geometry - VisualMath/tree/main/geometry
Путь maim - VisualMath/tree/main/main
```

В файле main находятся: главная страница и оглавления по темам.(index/html - homepage, maintenance - оглавление)

В алгебре и геометрии в папках (В данном случае в геометрии)[templates](https://github.com/Lo-Wang/VisualMath/tree/main/geometry/templates/geometry) находится текстовое описание для каждой темы в формате html. Все темы разбиты на папки для каждого класса.
```
Путь - VisualMath/tree/main/geometry/templates/geometry
```

Во всех трех приложениях содержится директория [static](https://github.com/Lo-Wang/VisualMath/tree/main/geometry/static/geometry), в которых содержится ресурсные и скриптовые файлы. 

За маршрутизацию отвечает [urls](https://github.com/Lo-Wang/VisualMath/blob/main/main/urls.py) и [views](https://github.com/Lo-Wang/VisualMath/blob/main/main/views.py)

# Дизайн

Дизайн разрабатывается в [Figma](https://www.figma.com/file/XITlXS5GmXhYGvXZsqTEn2/VisualMath?type=design&node-id=0%3A1&mode=design&t=8S8QdvUn5JNWRMVN-1).

Слева, в выпадающем меню слева есть Pages:
- Pre-made Templates - все макеты
- Typography - Все шрифты и стили шрифтов
- Colors - Цветовая палитра проекта
- Components - шаблоны для макетов


# Анимации

Код анимации хранится в данной папке [Project_Animation](https://github.com/Lo-Wang/VisualMath/tree/main/Project_animation) и разделены на две группы: [Algebra](https://github.com/Lo-Wang/VisualMath/tree/main/Project_animation/Algebra) и [Geometry](https://github.com/Lo-Wang/VisualMath/tree/main/Project_animation/Geometry). 

```
Путь - VisualMath/tree/main/Project_animation
```

Структура файлов с кодом рассмотрим на примере: 
```
7.2.2.First_Sign_Equality_Triangles.py
```
Здесь, 7 - класс , 2 - раздел , 2 - тема, First_Sign_Equality_Triangles - название темы.

[Внутри файла](https://github.com/Lo-Wang/VisualMath/blob/main/Project_animation/Geometry/7.2.2.First_Sign_Equality_Triangles.py) - название класса складывается из первых букв названия файла, это удобно использовать для команды рендера сцены:
```
manim -pqh First_Sign_Equality_Triangles.py fset
```
---
Если вам нужны файлы готовых анимаций вы их можете найти [здесь](https://github.com/Lo-Wang/VisualMath/tree/main/Project_animation/media/videos).

```
Путь - VisualMath/tree/main/Project_animation/media/videos
```
Название файла .mp4 соответствует названию класса из файлов .py.

# Интерактивная область

Интерактивная область реализуется с помощью canvas, html, css и js.

Раздел все ещё в разработке...

  




