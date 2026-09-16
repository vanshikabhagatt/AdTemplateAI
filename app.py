
import json
from datetime import datetime

import streamlit as st
from creative_engine import (
    recommend_templates,
    recommend_variations,
    generate_creative_package
)
from templates import (
    ACTOR_OPTIONS,
    TONE_OPTIONS,
    PLATFORM_OPTIONS,
    OBJECTIVE_OPTIONS
)

def package_to_json(package):
    return json.dumps(
        package,
        indent=2,
        ensure_ascii=False
    )


def package_to_markdown(package):
    strategy = package["strategy"]
    script = package["script"]

    markdown = []

    markdown.append("# BriefFlow Creative Production Package\n")

    markdown.append("## Project\n")
    markdown.append(
        f"**Project:** {package['project']['name']}\n"
    )
    markdown.append(
        f"**Template:** {package['project']['template']}\n"
    )
    markdown.append(
        f"**Variation:** {package['project']['variation']}\n"
    )

    markdown.append("\n## Creative Strategy\n")
    markdown.append(
        f"**Core Idea:** {strategy['core_idea']}\n"
    )
    markdown.append(
        f"**Key Message:** {strategy['key_message']}\n"
    )
    markdown.append(
        f"**Visual Direction:** {strategy['visual_direction']}\n"
    )

    markdown.append("\n## Hooks\n")

    for index, hook in enumerate(
        package["hooks"],
        start=1
    ):
        markdown.append(f"{index}. {hook}\n")

    markdown.append("\n## Video Script\n")
    markdown.append(
        f"**Actor:** {script['actor']}\n"
    )
    markdown.append(
        f"**Duration:** {script['duration']} seconds\n"
    )

    for scene in script["scenes"]:
        markdown.append(
            f"\n### Scene {scene['scene']} — "
            f"{scene['purpose']}\n"
        )
        markdown.append(
            f"**Time:** {scene['time']}\n"
        )
        markdown.append(
            f"**Visual:** {scene['visual']}\n"
        )
        markdown.append(
            f"**Dialogue:** {scene['dialogue']}\n"
        )
        markdown.append(
            f"**On-screen Text:** "
            f"{scene['on_screen_text']}\n"
        )

    markdown.append("\n## AI Shot Prompts\n")

    for prompt in package["shot_prompts"]:
        markdown.append(
            f"\n### Scene {prompt['scene']}\n"
        )
        markdown.append(
            f"{prompt['prompt']}\n"
        )

    return "\n".join(markdown)

st.sidebar.header("Creative Brief")

product = st.sidebar.text_area(
    "What are you promoting?",
    placeholder="Example: AI study planner for college students"
)

audience = st.sidebar.text_area(
    "Who is the target audience?",
    placeholder="Example: College students aged 18–25"
)

objective = st.sidebar.selectbox(
    "Campaign objective",
    OBJECTIVE_OPTIONS
)

tone = st.sidebar.selectbox(
    "Creative tone",
    TONE_OPTIONS
)

platform = st.sidebar.selectbox(
    "Platform",
    PLATFORM_OPTIONS
)

duration = st.sidebar.slider(
    "Video duration",
    min_value=10,
    max_value=60,
    value=30,
    step=5
)

actor = st.sidebar.selectbox(
    "Preferred actor",
    ACTOR_OPTIONS
)

brief = {
    "product": product,
    "audience": audience,
    "objective": objective,
    "tone": tone,
    "platform": platform,
    "duration": duration,
    "actor": actor
}

st.header("Recommended Creative Templates")

if not product or not audience:
    st.warning(
        "Enter your product and target audience to receive recommendations."
    )
    st.stop()

recommendations = recommend_templates(brief)

template_names = [
    template["name"]
    for template in recommendations
]

selected_template = st.selectbox(
    "Choose a creative template",
    template_names
)

selected_template_data = next(
    template
    for template in recommendations
    if template["name"] == selected_template
)

st.info(
    selected_template_data["description"]
)

st.write("**Best for:**")
st.write(
    selected_template_data["best_for"]
)


st.subheader("Choose a Creative Variation")

variations = recommend_variations(
    selected_template,
    brief
)

variation_names = [
    variation["name"]
    for variation in variations
]

selected_variation = st.selectbox(
    "Creative angle",
    variation_names
)

selected_variation_data = next(
    variation
    for variation in variations
    if variation["name"] == selected_variation
)

st.write(
    f"**Variation description:** "
    f"{selected_variation_data['description']}"
)

st.write(
    f"**Visual style:** "
    f"{selected_variation_data['visual_style']}"
)

st.divider()

generate_button = st.button(
    "Generate Creative Production Package",
    type="primary",
    use_container_width=True
)

if generate_button:

    with st.spinner("Creating your production package..."):

        package = generate_creative_package(
            brief=brief,
            template_name=selected_template,
            variation=selected_variation
        )

    st.success("Your creative package is ready!")

    # -----------------------------------------------------
    # Strategy
    # -----------------------------------------------------

    st.header("1. Creative Strategy")

    strategy = package["strategy"]

    st.write("**Core Idea**")
    st.write(strategy["core_idea"])

    st.write("**Key Message**")
    st.write(strategy["key_message"])

    st.write("**Visual Direction**")
    st.write(strategy["visual_direction"])

    st.write("**Content Structure**")

    for item in strategy["content_structure"]:
        st.write(f"• {item}")

    # -----------------------------------------------------
    # Hooks
    # -----------------------------------------------------

    st.header("2. Creative Hooks")

    for index, hook in enumerate(package["hooks"], start=1):
        st.write(f"**Hook {index}:** {hook}")

    # -----------------------------------------------------
    # Script
    # -----------------------------------------------------

    st.header("3. Video Script")

    script = package["script"]

    st.write(f"**Actor:** {script['actor']}")
    st.write(f"**Tone:** {script['tone']}")
    st.write(f"**Duration:** {script['duration']} seconds")

    for scene in script["scenes"]:

        with st.expander(
            f"Scene {scene['scene']} — {scene['purpose']}"
        ):

            st.write(f"**Time:** {scene['time']}")
            st.write(f"**Visual:** {scene['visual']}")
            st.write(f"**Dialogue:** {scene['dialogue']}")
            st.write(
                f"**On-screen text:** "
                f"{scene['on_screen_text']}"
            )

    # -----------------------------------------------------
    # Shot Prompts
    # -----------------------------------------------------

    st.header("4. AI Shot Prompts")

    for prompt_data in package["shot_prompts"]:

        with st.expander(
            f"Scene {prompt_data['scene']} Prompt"
        ):

            st.write(prompt_data["prompt"])

            st.button(
                "Copy prompt manually",
                key=f"copy_prompt_{prompt_data['scene']}"
            )
    

    # -----------------------------------------------------
    # Quality Checks
    # -----------------------------------------------------

    st.header("5. Production Quality Checks")

    for check in package["quality_checks"]:

        status = check["status"]

        if status == "PASS":
            st.success(
                f"{check['name']}: {check['message']}"
            )

        elif status == "WARNING":
            st.warning(
                f"{check['name']}: {check['message']}"
            )

        else:
            st.error(
                f"{check['name']}: {check['message']}"
            )
            
    # ---------------------------------------------------------
    # Export
    # ---------------------------------------------------------

    st.header("6. Export Your Production Package")

    json_data = package_to_json(package)
    markdown_data = package_to_markdown(package)

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label="Download JSON",
            data=json_data,
            file_name="brief-flow-package.json",
            mime="application/json",
            use_container_width=True
        )

    with col2:
        st.download_button(
            label="Download Markdown",
            data=markdown_data,
            file_name="brief-flow-package.md",
            mime="text/markdown",
            use_container_width=True
        )
    