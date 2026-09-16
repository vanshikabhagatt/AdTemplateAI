TEMPLATES = {
    "UGC Product Review": {
        "description": (
            "A natural creator-style ad that feels authentic, relatable "
            "and suitable for social media."
        ),
        "best_for": "Building trust, product discovery and everyday use cases.",
        "recommended_actor": "AI Creator",
        "variations": [
            {
                "name": "Relatable Creator Review",
                "description": (
                    "A friendly creator introduces the product through "
                    "a natural, personal-style review."
                ),
                "actor": "AI Creator",
                "tone": "Natural and authentic",
                "hook_style": "Personal experience",
                "visual_style": "Handheld, natural light, creator-style shots",
            },
            {
                "name": "Problem to Product",
                "description": (
                    "The video begins with a relatable problem and introduces "
                    "the product as a possible solution."
                ),
                "actor": "AI Creator",
                "tone": "Conversational",
                "hook_style": "Problem-first",
                "visual_style": "Relatable everyday situation",
            },
            {
                "name": "Fast Social Review",
                "description": (
                    "A quick, energetic review using fast cuts, product "
                    "close-ups and clear benefits."
                ),
                "actor": "AI Creator",
                "tone": "Fun and energetic",
                "hook_style": "Attention-grabbing",
                "visual_style": "Fast cuts, close-ups and captions",
            },
        ],
    },

    "Problem–Solution Ad": {
        "description": (
            "A structured advertisement that presents a problem, introduces "
            "the product and explains the solution."
        ),
        "best_for": "Explaining product value and driving consideration.",
        "recommended_actor": "Professional Presenter",
        "variations": [
            {
                "name": "Everyday Frustration",
                "description": (
                    "Start with a common audience frustration and introduce "
                    "the product as a helpful option."
                ),
                "actor": "AI Creator",
                "tone": "Relatable",
                "hook_style": "Problem-first",
                "visual_style": "Everyday lifestyle scenes",
            },
            {
                "name": "Before and After",
                "description": (
                    "Show the situation before using the product and the "
                    "improved experience afterward."
                ),
                "actor": "Professional Presenter",
                "tone": "Clear and confident",
                "hook_style": "Transformation",
                "visual_style": "Before-and-after visual contrast",
            },
            {
                "name": "Benefit Breakdown",
                "description": (
                    "Explain the product through three clear benefits "
                    "supported by simple visuals."
                ),
                "actor": "Professional Presenter",
                "tone": "Informative",
                "hook_style": "Benefit-led",
                "visual_style": "Clean product shots and text overlays",
            },
        ],
    },

    "Product Demo": {
        "description": (
            "A product-focused video showing how the product looks, works "
            "and fits into the user's routine."
        ),
        "best_for": "Demonstrating features, usage and product experience.",
        "recommended_actor": "Product-only",
        "variations": [
            {
                "name": "Step-by-Step Demo",
                "description": (
                    "Walk through the product in a simple sequence from "
                    "introduction to usage."
                ),
                "actor": "Product-only",
                "tone": "Clear and practical",
                "hook_style": "Demonstration",
                "visual_style": "Close-ups and step-by-step shots",
            },
            {
                "name": "Feature Spotlight",
                "description": (
                    "Focus on the product's most important features using "
                    "clean visuals and short explanations."
                ),
                "actor": "Professional Presenter",
                "tone": "Confident",
                "hook_style": "Feature-led",
                "visual_style": "Product close-ups and detail shots",
            },
            {
                "name": "Daily Routine Demo",
                "description": (
                    "Show how the product can fit naturally into an "
                    "everyday routine."
                ),
                "actor": "AI Creator",
                "tone": "Natural",
                "hook_style": "Routine-based",
                "visual_style": "Lifestyle scenes and natural movement",
            },
        ],
    },

    "Cinematic Product Ad": {
        "description": (
            "A visually polished product advertisement focused on mood, "
            "composition, premium visuals and brand identity."
        ),
        "best_for": "Premium launches, brand awareness and visual storytelling.",
        "recommended_actor": "Product-only",
        "variations": [
            {
                "name": "Premium Product Reveal",
                "description": (
                    "Reveal the product through dramatic lighting, elegant "
                    "movement and a strong hero shot."
                ),
                "actor": "Product-only",
                "tone": "Premium",
                "hook_style": "Visual reveal",
                "visual_style": "Studio lighting and cinematic camera movement",
            },
            {
                "name": "Lifestyle Story",
                "description": (
                    "Place the product inside a carefully designed lifestyle "
                    "scene that reflects the brand mood."
                ),
                "actor": "AI Creator",
                "tone": "Aspirational",
                "hook_style": "Lifestyle opening",
                "visual_style": "Cinematic lifestyle composition",
            },
            {
                "name": "Minimal Brand Film",
                "description": (
                    "Use minimal visuals, elegant pacing and a focused "
                    "product message."
                ),
                "actor": "Product-only",
                "tone": "Minimal and premium",
                "hook_style": "Elegant visual opening",
                "visual_style": "Minimal background and controlled movement",
            },
        ],
    },
}


ACTOR_OPTIONS = [
    "Young creator",
    "Female creator",
    "Male creator",
    "Student creator",
    "Professional presenter",
    "Product model",
    "No on-screen actor"
]


TONE_OPTIONS = [
    "Friendly",
    "Professional",
    "Casual",
    "Energetic",
    "Humorous",
    "Premium",
    "Cinematic",
    "Educational",
    "Relatable",
    "Bold"
]


PLATFORM_OPTIONS = [
    "Instagram Reels",
    "YouTube Shorts",
    "TikTok",
    "Product advertisement",
]


OBJECTIVE_OPTIONS = [
    "Product awareness",
    "Drive sales",
    "Generate leads",
    "Launch a product",
    "Build trust",
]