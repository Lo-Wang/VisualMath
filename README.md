

![logo](https://cdn.discordapp.com/attachments/1150438545748656179/1180099686149935184/Intro_fro_rdmd_1.png?ex=65f428fa&is=65e1b3fa&hm=12bee6f007c3063600959119103fa1b3c526b54edc789c8efebe1aa85eeed335&)

![Static Badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
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
- [Введение](#введение)
- [Сайт](#сайт)
- [Дизайн](#дизайн)
- [Анимации](#анимации)
- [Интерактивная область](#интерактивная-область)
- [Взаимодействие](#взаимодействие)


# Введение

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

> [!NOTE]
> Для создания анимаций используется библиотека Manim Community v0.17.3, ознакомится с ней
> можно на [сайте](https://www.manim.community/) или в [репозитории проекта](https://github.com/manimCommunity/manim).

# Интерактивная область

Интерактивная область реализуется с помощью canvas, html, css и js.

Файлы интерактивных областей находятся вместе с остальными ресурсными файлами в директории [static](https://github.com/Lo-Wang/VisualMath/tree/main/geometry/static/geometry), а именно в [js](https://github.com/Lo-Wang/VisualMath/tree/main/geometry/static/geometry/js)  (приведен пример с папкой "geometry")

```
Путь - VisualMath/tree/main/geometry/static/geometry/js
```
# Взаимодействие

> [!WARNING]
> Раздел может содержать неточности, требуется дополнительная проверка

В данный момент существует наглядная схема разработки продукта VisualMath. 

![logo](https://cdn.discordapp.com/attachments/1150438545748656179/1183813463051612271/C_.png?ex=65f87133&is=65e5fc33&hm=b699687c74cf18ad979ae4a74c26c36ba7511e1038d99f8319f219524d92f8b4&)

1) Вытянуть актуальную версию ветки ```release```
2) Пушить в свою ветку, выполнить стэш изменений из ветки в ветку ```release```
3) Ветка ```backend``` подтягивает изменения из ветки ```release```
4) Сохранить изменения в ветке ```backend``` и запушить.  
5) После тестирования все изменения из ветки ```release``` запушить в ветку ```main```

  




