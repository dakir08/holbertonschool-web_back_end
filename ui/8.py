import gradio as gr

def repeat_word(word, times):
    return ' '.join([word] * times)

app = gr.Interface(
    fn=repeat_word,
    inputs=[
        gr.components.Textbox(label="Object"),
        gr.components.Slider(minimum=1, maximum=10, label="Number of Repetitions")
    ],
    outputs=gr.components.Textbox(label="Output", lines=2),
    title="Word Repeater",
    description="Enter a word and choose how many times you want it repeated."
)

if __name__ == "__main__":
    app.launch()
