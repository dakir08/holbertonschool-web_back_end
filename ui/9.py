import gradio as gr

def reset_code():
    """Reset the code to the original snippet."""
    return "print('Hello World!')"

def clear_code():
    """Clear the code from the box."""
    return ""

with gr.Blocks() as app:
    gr.Markdown("# Python code scratch pad")
    code_block = gr.Code(value="print('Hello World!')", language="python", interactive=True)

    reset_button = gr.Button("Reset")
    clear_button = gr.Button("Clear")

    reset_button.click(fn=reset_code, inputs=None, outputs=code_block)
    clear_button.click(fn=clear_code, inputs=None, outputs=code_block)

app.launch()
