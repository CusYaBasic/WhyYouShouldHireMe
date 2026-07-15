from ui.widgets.slideshow_page import SlideshowPage

class StrengthsPage(SlideshowPage):

    def __init__(self):

        slides = [
            {
                "image": "assets/images/memes/self_taught.png",
                "title": "Self Taught",
                "text":
                    "I'm entirely self taught. Nobody forced me to learn. \nI simply enjoyed it enough to keep going. "

            },
            {
                "image": "assets/images/memes/mindset.jpg",
                "title": "Mindset",
                "text":
                    "Programming isn't just knowing syntax.\nIt's breaking problems down until they become easy. "

            },
            {
                "image": "assets/images/memes/adaptable.jpg",
                "title": "Adaptable",
                "text":
                    "PHP, JavaScript, SQL, C#, C++, Python\nI've picked up multiple languages and frameworks because the underlying problem-solving skills transfer. "
            },
            {
                "image": "assets/images/memes/curious.jpg",
                "title": "Curious",
                "text":
                    "I ask 'why?' more than 'how?' "
            },
            {
                "image": "assets/images/memes/team.jpg",
                "title": "Team Player",
                "text":
                    "I enjoy helping others almost as much as solving problems myself. "
            },
            {
                "image": "assets/images/memes/always.jpg",
                "title": "Always Building",
                "text":
                    "I've been building projects for years because I enjoy creating things; not because someone told me to. "
            }
        ]

        super().__init__(
            slides
        )