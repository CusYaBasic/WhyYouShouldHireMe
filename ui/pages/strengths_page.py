from ui.widgets.slideshow_page import SlideshowPage


class StrengthsPage(SlideshowPage):

    def __init__(self):

        slides = [
            {
                "image": "assets/images/strengths/problem_solving.png",
                "title": "Self Taught",
                "text":
                    "I'm entirely self taught. Nobody forced me to learn. \nI simply enjoyed it enough to keep going. "

            },

            {
                "image": "assets/images/strengths/learning.png",
                "title": "Mindset",
                "text":
                    "Programming isn't just knowing syntax.\nIt's breaking problems down until they become easy. "

            },

            {
                "image": "assets/images/strengths/independent.png",
                "title": "Adaptable",
                "text":
                    "PHP, JavaScript, SQL, C#, C++, Python\nI've picked up multiple languages and frameworks because the underlying problem-solving skills transfer. "
            },

            {
                "image": "assets/images/strengths/teamwork.png",
                "title": "Curious",
                "text":
                    "I ask 'why?' more than 'how?' "
            },

            {
                "image": "assets/images/strengths/creativity.png",
                "title": "Team Player",
                "text":
                    "I enjoy helping others almost as much as solving problems myself. "
            },

            {
                "image": "assets/images/strengths/creativity.png",
                "title": "Always Building",
                "text":
                    "I've been building projects for years because I enjoy creating things; not because someone told me to. "
            }
        ]

        super().__init__(
            slides
        )