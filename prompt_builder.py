def build_prompt(context, tone="whimsical", audience="general"):
    return (
        f"You are a storyteller AI. Create a short fable or myth set in Bhopal, Madhya Pradesh. "
        f"Blend real and imagined elements. Use the following context:\n\n{context}\n\n"
        f"The tone should be {tone}, and the story should be suitable for a {audience} audience. "
        f"Include vivid imagery, interesting characters, and optionally a moral or cultural insight at the end."
    )
