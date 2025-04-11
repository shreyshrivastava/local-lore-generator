import gradio as gr
from prompt_builder import build_prompt
from groq_client import query_llama4_story

def generate_story(context, tone, audience):
    prompt = build_prompt(context, tone, audience)
    story = query_llama4_story(prompt)
    return story

iface = gr.Interface(
    fn=generate_story,
    inputs=[
        gr.Textbox(label="🗺️ Local Context", lines=5, placeholder="Enter landmarks, festivals, legends..."),
        gr.Radio(["whimsical", "cautionary", "humorous", "mystical"], label="🎭 Tone"),
        gr.Radio(["general", "children", "adults"], label="👥 Audience")
    ],
    outputs=gr.Textbox(label="📖 Your Story"),
    title="📜 Local Lore Generator",
    description="Powered by Groq LLaMA 4 Scout 🔥"
)


if __name__ == "__main__":
    iface.launch()
