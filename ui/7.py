import gradio as gr

def hello_markdown():
    return "# Hello Markdown World!"

app = gr.Interface(
    fn=hello_markdown,
    inputs=[],
    outputs=gr.components.Markdown(),
    title="Markdown Display Example"
)

if __name__ == "__main__":
    app.launch()
