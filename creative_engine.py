# creative_engine.py

from copy import deepcopy
from templates import TEMPLATES


# ---------------------------------------------------------
# Utility Helpers
# ---------------------------------------------------------

def clean_text(value):
    """Convert any value into clean text."""
    return str(value or "").strip()


def lower_text(value):
    """Return lowercase text for matching."""
    return clean_text(value).lower()


def contains_any(value, keywords):
    """Check whether any keyword exists in a text value."""
    text = lower_text(value)
    return any(keyword.lower() in text for keyword in keywords)


# ---------------------------------------------------------
# Template Recommendation Engine
# ---------------------------------------------------------

def score_template(template_name, brief):
    """
    Score a template based on the user's creative brief.

    This is intentionally rule-based and deterministic.
    Later, this can be replaced with an LLM or embedding model.
    """

    platform = lower_text(brief.get("platform"))
    objective = lower_text(brief.get("objective"))
    tone = lower_text(brief.get("tone"))
    product = lower_text(brief.get("product"))
    audience = lower_text(brief.get("audience"))

    score = 0

    if template_name == "UGC Product Review":
        if contains_any(platform, ["instagram reels", "tiktok", "youtube shorts"]):
            score += 4

        if contains_any(objective, ["build trust", "product awareness"]):
            score += 4

        if contains_any(tone, ["friendly", "relatable", "casual", "humorous"]):
            score += 3

        if contains_any(product, ["skincare", "beauty", "fashion", "food", "fitness"]):
            score += 2

        if contains_any(audience, ["student", "young", "gen z", "college"]):
            score += 2

    elif template_name == "Problem–Solution Ad":
        if contains_any(objective, ["drive sales", "generate leads"]):
            score += 5

        if contains_any(platform, ["instagram reels", "tiktok", "youtube shorts"]):
            score += 3

        if contains_any(tone, ["bold", "energetic", "direct", "urgent"]):
            score += 3

        if contains_any(product, ["app", "tool", "software", "service", "course"]):
            score += 2

    elif template_name == "Product Demo":
        if contains_any(objective, ["drive sales", "launch a product"]):
            score += 4

        if contains_any(product, ["app", "software", "device", "gadget", "tool"]):
            score += 5

        if contains_any(platform, ["youtube", "linkedin"]):
            score += 3

        if contains_any(tone, ["professional", "educational", "clear"]):
            score += 3

    elif template_name == "Cinematic Product Ad":
        if contains_any(objective, ["launch a product", "product awareness"]):
            score += 4

        if contains_any(tone, ["premium", "luxury", "cinematic", "aspirational"]):
            score += 5

        if contains_any(platform, ["youtube", "instagram", "website"]):
            score += 2

        if contains_any(product, ["perfume", "watch", "jewellery", "car", "fashion"]):
            score += 4

    return score


def recommend_templates(brief, limit=3):
    """
    Return the best creative templates for a brief.

    Output format:
    [
        {
            "name": "...",
            "description": "...",
            "best_for": "...",
            "recommended_actor": "...",
            "variations": [...]
        }
    ]
    """

    ranked_templates = sorted(
        TEMPLATES.keys(),
        key=lambda name: score_template(name, brief),
        reverse=True
    )

    selected_templates = ranked_templates[:limit]

    recommendations = []

    for template_name in selected_templates:
        template = deepcopy(TEMPLATES[template_name])

        recommendations.append({
            "name": template_name,
            **template
        })

    return recommendations


# ---------------------------------------------------------
# Variation Recommendation Engine
# ---------------------------------------------------------

def score_variation(variation, brief):
    """Score one variation according to the creative brief."""

    tone = lower_text(brief.get("tone"))
    objective = lower_text(brief.get("objective"))
    platform = lower_text(brief.get("platform"))

    variation_tone = lower_text(variation.get("tone"))
    variation_style = lower_text(variation.get("visual_style"))
    variation_hook = lower_text(variation.get("hook_style"))

    score = 0

    if tone and tone in variation_tone:
        score += 4

    if contains_any(tone, ["premium", "luxury"]):
        if contains_any(variation_style, ["cinematic", "premium", "minimal"]):
            score += 4

    if contains_any(tone, ["friendly", "casual", "relatable"]):
        if contains_any(variation_tone, ["friendly", "casual", "relatable"]):
            score += 4

    if contains_any(objective, ["drive sales", "generate leads"]):
        if contains_any(variation_hook, ["problem", "benefit", "result", "offer"]):
            score += 3

    if contains_any(objective, ["build trust"]):
        if contains_any(variation_tone, ["authentic", "relatable", "honest"]):
            score += 4

    if contains_any(platform, ["tiktok", "instagram reels", "youtube shorts"]):
        if contains_any(variation_hook, ["pattern interrupt", "fast", "bold"]):
            score += 2

    return score


def recommend_variations(template_name, brief):
    """
    Return variations for a selected template, ranked by relevance.
    """

    if template_name not in TEMPLATES:
        return []

    variations = deepcopy(TEMPLATES[template_name]["variations"])

    variations.sort(
        key=lambda variation: score_variation(variation, brief),
        reverse=True
    )

    return variations


# ---------------------------------------------------------
# Hook Generation
# ---------------------------------------------------------

def generate_hooks(product, audience, objective, tone, template_name, variation):
    """
    Generate five hooks based on the selected template and variation.
    """

    product = clean_text(product)
    audience = clean_text(audience)
    objective = clean_text(objective)
    tone = clean_text(tone)
    template_name = clean_text(template_name)
    variation = clean_text(variation)

    hooks = [
        f"POV: You finally found a better way to deal with {product}.",
        f"If you're a {audience}, you need to see this before choosing your next solution.",
        f"Most people approach {product} the wrong way. Here's a smarter approach.",
        f"I tried {product} with one simple goal: {objective.lower()}.",
        f"Here's why {product} could be worth adding to your routine."
    ]

    if "UGC" in template_name:
        hooks.extend([
            f"Okay, I did not expect {product} to become part of my daily routine.",
            f"Honest review: here's what I noticed after trying {product}."
        ])

    elif "Problem" in template_name:
        hooks.extend([
            f"Still struggling with this problem? Try this approach.",
            f"Stop wasting time on complicated solutions for this problem."
        ])

    elif "Demo" in template_name:
        hooks.extend([
            f"Let me show you exactly how {product} works.",
            f"Three useful things you can do with {product}."
        ])

    elif "Cinematic" in template_name:
        hooks.extend([
            f"Designed for the moments that matter. Meet {product}.",
            f"More than a product. A better everyday experience."
        ])

    return hooks[:5]


# ---------------------------------------------------------
# Strategy Generation
# ---------------------------------------------------------

def generate_strategy(
    product,
    audience,
    objective,
    tone,
    platform,
    duration,
    template_name,
    variation
):
    """Generate a complete creative strategy."""

    product = clean_text(product)
    audience = clean_text(audience)
    objective = clean_text(objective)
    tone = clean_text(tone)
    platform = clean_text(platform)
    template_name = clean_text(template_name)
    variation = clean_text(variation)

    return {
        "core_idea": (
            f"Use a {variation.lower()} approach to present {product} "
            f"for {audience}, while focusing on {objective.lower()}."
        ),
        "creative_format": template_name,
        "tone": tone,
        "platform": platform,
        "duration": f"{duration} seconds",
        "target_audience": audience,
        "main_objective": objective,
        "key_message": (
            f"{product} helps the target audience move from a common "
            f"challenge toward a clearer and more useful outcome."
        ),
        "content_structure": [
            "Grab attention immediately",
            "Introduce the audience problem or desire",
            "Present the product naturally",
            "Show the main benefit or use case",
            "End with a clear call to action"
        ],
        "visual_direction": (
            f"Use {tone.lower()} visuals with clear product visibility, "
            f"simple framing, and platform-friendly pacing."
        )
    }


# ---------------------------------------------------------
# Script Generation
# ---------------------------------------------------------

def generate_script(
    product,
    audience,
    objective,
    tone,
    duration,
    hook,
    template_name,
    variation,
    actor
):
    """
    Generate a short-form video script with scene-level details.
    """

    product = clean_text(product)
    audience = clean_text(audience)
    objective = clean_text(objective)
    tone = clean_text(tone)
    hook = clean_text(hook)
    template_name = clean_text(template_name)
    variation = clean_text(variation)
    actor = clean_text(actor)

    if duration <= 15:
        scene_count = 4
    elif duration <= 30:
        scene_count = 5
    else:
        scene_count = 6

    scenes = [
        {
            "scene": 1,
            "time": "0–3 seconds",
            "visual": f"{actor} opens with a strong attention-grabbing expression.",
            "dialogue": hook,
            "on_screen_text": "Wait — this is useful",
            "purpose": "Hook"
        },
        {
            "scene": 2,
            "time": "3–7 seconds",
            "visual": (
                f"Show the common problem or desire experienced by {audience}."
            ),
            "dialogue": (
                f"If you're dealing with this, you're definitely not alone."
            ),
            "on_screen_text": "A common everyday problem",
            "purpose": "Problem or desire"
        },
        {
            "scene": 3,
            "time": "7–12 seconds",
            "visual": f"Introduce {product} naturally in a real-life setting.",
            "dialogue": (
                f"That's where {product} comes in. "
                f"Here's how I would use it."
            ),
            "on_screen_text": product,
            "purpose": "Product introduction"
        },
        {
            "scene": 4,
            "time": "12–18 seconds",
            "visual": (
                f"Show the product being used with close-up shots "
                f"and a clear demonstration."
            ),
            "dialogue": (
                f"The main benefit is that it makes the experience "
                f"more simple, practical, and convenient."
            ),
            "on_screen_text": "Simple. Useful. Practical.",
            "purpose": "Benefit demonstration"
        },
        {
            "scene": 5,
            "time": "18–24 seconds",
            "visual": (
                "Show a positive reaction, product detail, or before-and-after "
                "context without making unsupported claims."
            ),
            "dialogue": (
                f"If your goal is to {objective.lower()}, "
                f"this is worth exploring."
            ),
            "on_screen_text": "Made for your everyday needs",
            "purpose": "Reinforcement"
        },
        {
            "scene": 6,
            "time": "24–30 seconds",
            "visual": "End with the product clearly visible and a direct gesture.",
            "dialogue": (
                f"Check out {product} and see if it fits your needs."
            ),
            "on_screen_text": "Explore it today",
            "purpose": "Call to action"
        }
    ]

    return {
        "actor": actor,
        "template": template_name,
        "variation": variation,
        "tone": tone,
        "duration": duration,
        "scenes": scenes[:scene_count]
    }


# ---------------------------------------------------------
# Shot Prompt Generation
# ---------------------------------------------------------

def generate_prompts(
    product,
    tone,
    platform,
    scenes,
    actor,
    visual_style
):
    """
    Generate AI image/video prompts for every script scene.
    """

    product = clean_text(product)
    tone = clean_text(tone)
    platform = clean_text(platform)
    actor = clean_text(actor)
    visual_style = clean_text(visual_style)

    prompts = []

    for scene in scenes:
        scene_number = scene["scene"]
        visual = scene["visual"]
        purpose = scene["purpose"]

        prompt = (
            f"Create a {tone.lower()} short-form advertising shot for {platform}. "
            f"Product: {product}. "
            f"Actor: {actor}. "
            f"Visual style: {visual_style}. "
            f"Scene {scene_number}: {visual}. "
            f"Purpose: {purpose}. "
            f"Use natural lighting, realistic composition, clear product visibility, "
            f"clean background, vertical 9:16 framing, and social-media-ready quality."
        )

        prompts.append({
            "scene": scene_number,
            "purpose": purpose,
            "prompt": prompt
        })

    return prompts


# ---------------------------------------------------------
# Quality Checks
# ---------------------------------------------------------

def run_quality_checks(package):
    """Run basic production checks on the generated package."""

    checks = []

    product = package.get("brief", {}).get("product", "")
    audience = package.get("brief", {}).get("audience", "")
    hooks = package.get("hooks", [])
    scenes = package.get("script", {}).get("scenes", [])
    prompts = package.get("shot_prompts", [])

    checks.append({
        "name": "Product information",
        "status": "PASS" if product else "FAIL",
        "message": "Product information is available."
        if product
        else "Add a product or service."
    })

    checks.append({
        "name": "Target audience",
        "status": "PASS" if audience else "WARNING",
        "message": "Target audience is defined."
        if audience
        else "Add a more specific target audience."
    })

    checks.append({
        "name": "Creative hooks",
        "status": "PASS" if len(hooks) >= 3 else "WARNING",
        "message": f"{len(hooks)} hooks generated."
    })

    checks.append({
        "name": "Video script",
        "status": "PASS" if len(scenes) >= 4 else "FAIL",
        "message": f"{len(scenes)} scenes generated."
    })

    checks.append({
        "name": "Shot prompt coverage",
        "status": "PASS" if len(prompts) == len(scenes) else "FAIL",
        "message": f"{len(prompts)} shot prompts for {len(scenes)} scenes."
    })

    has_cta = any(
        scene.get("purpose") == "Call to action"
        for scene in scenes
    )

    checks.append({
        "name": "Call to action",
        "status": "PASS" if has_cta else "WARNING",
        "message": "A call-to-action scene is included."
        if has_cta
        else "Add a clear call to action."
    })

    return checks


# ---------------------------------------------------------
# Complete Package Generator
# ---------------------------------------------------------

def generate_creative_package(
    brief,
    template_name,
    variation
):
    """
    Generate the complete production package.

    Expected brief format:

    {
        "product": "...",
        "audience": "...",
        "objective": "...",
        "tone": "...",
        "platform": "...",
        "duration": 30,
        "actor": "..."
    }
    """

    brief = deepcopy(brief)

    product = clean_text(brief.get("product"))
    audience = clean_text(brief.get("audience"))
    objective = clean_text(brief.get("objective"))
    tone = clean_text(brief.get("tone"))
    platform = clean_text(brief.get("platform"))
    duration = int(brief.get("duration", 30))
    actor = clean_text(brief.get("actor", "Creator"))

    template_data = TEMPLATES.get(template_name, {})
    variation_data = next(
        (
            item
            for item in template_data.get("variations", [])
            if item.get("name") == variation
        ),
        {}
    )

    if not actor:
        actor = variation_data.get(
            "actor",
            template_data.get("recommended_actor", "Creator")
        )

    visual_style = variation_data.get(
        "visual_style",
        "Natural, realistic, clean social media visuals"
    )

    hooks = generate_hooks(
        product=product,
        audience=audience,
        objective=objective,
        tone=tone,
        template_name=template_name,
        variation=variation
    )

    strategy = generate_strategy(
        product=product,
        audience=audience,
        objective=objective,
        tone=tone,
        platform=platform,
        duration=duration,
        template_name=template_name,
        variation=variation
    )

    script = generate_script(
        product=product,
        audience=audience,
        objective=objective,
        tone=tone,
        duration=duration,
        hook=hooks[0],
        template_name=template_name,
        variation=variation,
        actor=actor
    )

    shot_prompts = generate_prompts(
        product=product,
        tone=tone,
        platform=platform,
        scenes=script["scenes"],
        actor=actor,
        visual_style=visual_style
    )

    package = {
        "project": {
            "name": f"{product} Creative Campaign",
            "template": template_name,
            "variation": variation
        },
        "brief": brief,
        "creative_direction": {
            "actor": actor,
            "visual_style": visual_style,
            "tone": tone,
            "platform": platform
        },
        "strategy": strategy,
        "hooks": hooks,
        "script": script,
        "shot_prompts": shot_prompts
    }

    package["quality_checks"] = run_quality_checks(package)

    return package