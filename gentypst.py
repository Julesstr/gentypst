import lorem
import random
import time
import os
def gen_title(level):
    title_name = lorem.get_word(count=1)
    title = f"{level*'='} {title_name}"
        
    return title, title_name    


def create_paragraph(reference_list):

    paragraph = lorem.get_paragraph(count=1)
    space_indeces = [i for i, char in enumerate(paragraph) if char == ' ']
    
    if not space_indeces:
        return paragraph
    
    indices_to_replace = random.sample(space_indeces, int(len(space_indeces)/10))

    char_list = list(paragraph)

    for index in indices_to_replace:
        char_list[index] = " ☂ "

    final_paragraph = "".join(char_list)

    return final_paragraph

def main():
    output = """#set page(
    paper: "a4",
    margin: (x: 1.8cm, y: 1.5cm)
    )

    #set text(
    font: "New Computer Modern",
    size: 10pt
    )

    #set par(
        justify: true,
        leading: 0.8em
        )

    #set heading(numbering: "1.1")
    #show heading: set block(below: 1.5em)
    """ 

    output += "= Title text \n"
    level = 2
    reference_list = []

    image_names =  [
    f for f in os.listdir("Images")
    if os.path.isfile(os.path.join("Images", f))
    ]
    print(image_names)
    while len(output) < 1000000:
        title, title_name = gen_title(level)
        output += f"{title} <{title_name}_{len(reference_list)}> \n"
        reference_list.append(f"{title_name}_{len(reference_list)}")
        level += 1

        while level == 3:
            title, title_name = gen_title(level)
            output += f"{title} <{title_name}_{len(reference_list)}> \n"
            reference_list.append(f"{title_name}_{len(reference_list)}")
            roll = random.random()

            if roll > 0.5:
                level -= 1

            paragraph = True
            while paragraph:
                para_text = create_paragraph(reference_list) 
                output += para_text
                output += "\\ "        
                output += f'#image("Images/{random.choice(image_names)}", width: 60%, height: 60%)'
                output += "\n"
                roll = random.random()
                if roll > 0.5:
                    paragraph = False

    output = "".join(f"@{random.choice(reference_list)}" if ch == "☂" else ch for ch in output)
    with open("output.typ", "w") as f:
        f.write(output)

if __name__ == "__main__":
    s = time.time()
    main()     
    e = time.time()
    print(e-s)

















































