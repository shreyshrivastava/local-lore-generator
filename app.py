import gradio as gr
from prompt_builder import build_prompt
from groq_client import query_llama4_story, generate_image
from pathlib import Path

def generate_story_and_image(context, tone, audience):
    if not context.strip():
        return "Please provide some local context to generate a story.", None

    prompt = build_prompt(context, tone, audience)
    story = query_llama4_story(prompt)

    if story is None:
        story = "❌ Story generation failed."

    image_prompt = (
        f"A Google Doodle-style illustration for an Indian folk story: {context}. "
        f"Use soft colors, cartoon style, clean background, and whimsical Indian folk art elements."
    )
    image_url = generate_image(image_prompt)

    if not image_url or not image_url.startswith("http"):
        local_path = Path("placeholder.png").resolve()
        image_url = f"file={local_path}"
        story += (
            "\n\n🖼️ **Note:** Sorry! AI image generation is currently unavailable. "
            "We've hit our usage limit for today. Please try again tomorrow."
        )

    return story, image_url

iface = gr.Interface(
    fn=generate_story_and_image,
    inputs=[
        gr.Textbox(label="🗺️ Local Context", lines=5, placeholder="Enter landmarks, festivals, myths..."),
        gr.Radio(["whimsical", "cautionary", "humorous", "mystical"], label="🎭 Tone"),
        gr.Radio(["general", "children", "adults"], label="👥 Audience")
    ],
    outputs=[
        gr.Textbox(label="📖 Your Generated Story"),
        gr.Image(label="🎨 AI-Generated Illustration")
    ],
    title="📜 Local Lore Generator",
    description="Craft region-specific Indian fables using LLaMA 4 and DALL·E.",
    article="""
---

🔧 Built by **Shrey Shrivastava**  
[![GitHub](https://img.shields.io/badge/GitHub-shreyshrivastava-181717?style=flat&logo=github)](https://github.com/shreyshrivastava)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/shrey-shrivastava1)

Powered by [Groq](https://groq.com) · AI Art by [OpenAI DALL·E](https://platform.openai.com/) · UI by [Gradio](https://gradio.app)
"""
)

if __name__ == "__main__":
    iface.launch()
