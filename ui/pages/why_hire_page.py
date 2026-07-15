from ui.widgets.slideshow_page import SlideshowPage


class WhyHirePage(SlideshowPage):

    def __init__(self):

        slides = [
            {
                "image": "assets/images/memes/chillguy.jpg",
                "title": "Chill Guy",
                "text":
                "I'm just a chill guy who genuinely enjoys anything involving technology.\nWhether it's fixing PCs, building software, automating boring tasks or making games, I enjoy solving problems."
            },

            {
                "image": "assets/images/memes/loyalty.gif",
                "title": "Loyal",
                "text":
                "I don't enjoy job hopping.\nWhen I join a company, I like to put down roots and become part of the team.\n Small fun fact: shortest time i spent at a company is 3 years"
            },

            {
                "image": "assets/images/memes/worker.gif",
                "title": "Hard Working",
                "text":
                "I'm hungry to learn, eager to improve and genuinely enjoy helping people solve technical problems."
            },

            {
                "image": "assets/images/memes/neversick.jpg",
                "title": "Hardly Ever Sick",
                "text":
                    "Professional sick days: 3 over 15 years\nUnless I'm genuinely ill, I'd rather be working."
            },

            {
                "image": "assets/images/memes/builder.png",
                "title": "Builder",
                "text":
                    "I don't just like using software...\nI like understanding how it works."
            },

            {
                "image": "assets/images/memes/sponge.gif",
                "title": "Sponge",
                "text":
                    "I love learning new technologies.\nThe more obscure, the better."
            },

            {
                "image": "assets/images/memes/tea.gif",
                "title": "Caffeine Powered",
                "text":
                    "99% caffeine.\n1% actual blood."
            },

            {
                "image": "assets/images/memes/duck.png",
                "title": "Debug Duck",
                "text":
                    "If talking to a rubber duck fixes bugs...\nImagine what I can do with an actual team."
            }
        ]


        super().__init__(
            slides
        )