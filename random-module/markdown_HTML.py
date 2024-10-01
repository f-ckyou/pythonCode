import markdown

def convert(intput_file, output_file):

    with open(input_file, 'r') as md_file:
        markdown_content = md_file.read()

    html_content = markdown.markdown(markdown_content) # markdown converted into HTML

    
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

    print("Converted")


input_file = 'random-module/input.md' # from: https://markdown-it.github.io/
output_file = 'random-module/output.html'


convert(input_file, output_file)