from ui.widgets.slideshow_page import SlideshowPage


class ProgrammingPrinciplesPage(SlideshowPage):

    def __init__(self):

        slides = [
            {
                "image": "assets/images/programming/modular.png",
                "title": "Modular Design",
                "text":
                    "I prefer building reusable systems that can be extended rather "
                    "than rewriting functionality. Components, inheritance and clean "
                    "interfaces help keep projects maintainable."
            },
            {
                "image": "assets/images/programming/clean_code.png",
                "title": "Clean Code",
                "text":
                    "Code should be easy for other developers to understand. "
                    "I focus on meaningful names, organised structures and avoiding "
                    "unnecessary complexity."
            },
            {
                "image": "assets/images/programming/debugging.png",
                "title": "Problem Solving",
                "text":
                    "When debugging, I approach issues methodically by understanding "
                    "the problem, identifying the cause and testing solutions instead "
                    "of relying on trial and error."
            },
            {
                "image": "assets/images/programming/performance.png",
                "title": "Performance Awareness",
                "text":
                    "I consider performance when designing systems, especially in games "
                    "where optimisation, memory usage and efficient updates can have "
                    "a significant impact."
            },
            {
                "image": "assets/images/programming/testing.png",
                "title": "Testing & Iteration",
                "text":
                    "I believe reliable software comes from testing ideas early, "
                    "iterating based on feedback and continuously improving systems."
            }
        ]

        super().__init__(
            slides
        )