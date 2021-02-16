import pandas as pd

def dfToHTML(df):
    df = df.applymap(lambda x: str(round(x, 2)))
    html = (
        df.style
        .set_table_styles([{'selector': 'th', 'props': [('font-size', '14pt'),
                                                        ('font-family', 'Helvetica'),
                                                        ('text-align', 'center'),
                                                        ('border', '3px solid'),
                                                        ('padding', '10px'),
                                                        ('background-color', '#cfcfcf')]}])
        .set_properties(**{'font-size': '12pt', 'font-family': 'Helvetica', 'text-align': 'center', 'border': '2px solid', 'padding': '10px'})
        .render()
        )
    return html.replace('\n', '')

