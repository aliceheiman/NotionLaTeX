import streamlit as st

header = st.container()
playground = st.container()

#### SETUP
textfonts = ["sf", "tt", "it", "rm", "bf"]
mathfonts = ["frak", "mathscr", "mathbb", "cal"]

colors = ["blue", "brown", "orange", "gray", "navy", "orchid", "red", "purple", "violet", "yellow", "cyan", "green", "skyblue", "olive", "teal", "magenta"]

with header:
    st.title("Notion LaTeX Generator")
    st.info(
        "Welcome to the **LaTeX Generator**! Type your message into the text box, pick your fonts and colors, and generate the corresponding LaTeX code!"
    )

with playground:
    with st.form("latex"):
        
        col1, col2 = st.columns(2)

        with col1:
            text = st.text_area("Original Text", placeholder="Type your original text here...")

            submitted = st.form_submit_button("Generate LaTeX Code")

        with col2:
            # Select
            font = st.selectbox(
                "Which font would you like to use?",
                ["Default"] + textfonts[:] + mathfonts[:]
            )

            color = st.selectbox(
                "Which color would you like to use?",
                ["black"] + colors[:]
            )

        

        if submitted:
            st.markdown("**LaTeX Code and Output:**")

            code = ''

            if color != "black":
                code += '\\color{' + color + '}'

            textlines = text.strip().split('\n')

            for i, line in enumerate(textlines):

                if font in textfonts:
                    code += '\\text{\\'
                    code += font + '{'
                    code += line
                    code += '}}'
                else:
                    code += '\\' + font + '{'
                    code += '\\ '.join(line.strip().split(" "))
                    code += '}'

                if i < len(textlines) - 1:
                    code += ' \\\\\n'
        
            st.code(code, language="latex")
            st.latex(code)