from ui.widgets.slideshow_page import SlideshowPage


class WeaknessesPage(SlideshowPage):

    def __init__(self):

        slides = [
            {
                "image": "assets/images/memes/python.jpg",
                "title": "Python",
                "text":
                    "Python isn't my strongest language yet.\n The fundamentals transfer well, and I'm learning quickly. "
            },
            {
                "image": "assets/images/memes/adhd.jpg",
                "title": "ADHD",
                "text":
                    "I work best with clear priorities and structure.\n Once I have that, I become incredibly productive. "
            },
            {
                "image": "assets/images/memes/imposter.jpg",
                "title": "Imposter Syndrome",
                "text":
                    "Being self taught means I'm aware there are things\nI haven't learned yet and that there are gaps in my knowledge.\n Instead of pretending otherwise, I ask questions and fill the gaps. "
            },
            {
                "image": "assets/images/memes/helpful.jpg",
                "title": "Sometimes Too Helpful",
                "text":
                    "I can spend too long helping someone because I genuinely enjoy solving problems. "
            }
        ]

        super().__init__(
            slides
        )