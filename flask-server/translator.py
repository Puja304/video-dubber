from prompt_responder import *

def translate_text(text, previous_attempt, short, long, language):
    # General instructions
    if previous_attempt == "":
        instructions = [
            f"You are a professional translator for {language}.",
            f"Only output the {language} translation — no extra text, no explanation.",
            f"Keep the meaning accurate and natural in spoken {language}. Do not be overly formal.",
            "Now translate the following sentence:"
        ]
        body = f"\"{text}\""
    else:
        instructions = [
            f"You are a professional rephraser of {language} sentences.",
            "Only output the revised sentence — no extra text, no explanation."
        ]
        if short:
            instructions.append("Make this version a little longer to better match spoken timing.")
        elif long:
            instructions.append("Make this version a little shorter to better fit the timing.")

        instructions.append("Do not change the original meaning.")
        instructions.append("Now rephrase the following sentence:")
        body = f"\"{previous_attempt}\""

    # Combine everything
    prompt = "\n".join(instructions) + "\n\n" + body
    return gpt_modified(prompt, language)
