c = get_config()

c.NbConvertApp.notebooks = ['Part1Neat.ipynb']
c.NbConvertApp.export_format = 'html_toc'
c.Exporter.preprocessors = [
    'nbconvert.preprocessors.TagRemovePreprocessor',
    'nbconvert.preprocessors.RegexRemovePreprocessor',
    'nbconvert.preprocessors.coalesce_streams',
    'nbconvert.preprocessors.CSSHTMLHeaderPreprocessor',
    'nbconvert.preprocessors.HighlightMagicsPreprocessor',
    #'nbconvert.preprocessors.ExtractOutputPreprocessor',
]