from ui.widgets.slideshow_page import SlideshowPage


class PreviousWorkPage(SlideshowPage):

    def __init__(self):

        slides = [
            {
                "image": "assets/images/work/unreal.png",
                "title": "Unreal Engine Development",
                "text":
                    "I have experience developing gameplay systems using Unreal Engine "
                    "with both Blueprints and C++. I have created mechanics, UI systems, "
                    "plugins and gameplay frameworks."
            },
            {
                "image": "assets/images/work/humanity_remains.png",
                "title": "Humanity Remains",
                "text":
                    "An extraction-style zombie survival game developed using Unreal Engine. "
                    "I worked on gameplay systems, player mechanics, networking concepts "
                    "and overall game architecture."
            },
            {
                "image": "assets/images/work/lostlands.png",
                "title": "Lost Lands",
                "text":
                    "A 2D sandbox MMORPG project inspired by classic online RPGs. "
                    "Built with MonoGame, focusing on systems such as inventory, "
                    "skills, economy and multiplayer architecture."
            },
            {
                "image": "assets/images/work/lensify.png",
                "title": "Lensify",
                "text":
                    "A streaming-focused application integrating AR technology into "
                    "OBS workflows. Designed to make virtual avatars and effects "
                    "accessible for content creators."
            },
            {
                "image": "assets/images/work/developer_tools.png",
                "title": "Developer Tools",
                "text":
                    "I enjoy building tools that improve workflows, including custom "
                    "editors, inventory systems, automation tools and applications "
                    "to solve real development problems."
            }
        ]

        super().__init__(
            slides
        )